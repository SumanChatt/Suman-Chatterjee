# -*- coding: cp1252 -*-
from osv import fields, osv
from datetime import *
import webbrowser
import datetime
import time
import csv
from osv import fields, osv
from openerp.osv import fields, osv
from openerp import netsvc
from openerp import pooler
from datetime import datetime
from dateutil.relativedelta import relativedelta
import platform
import re
import logging
import urllib2



#######################################################################
class rb_vfsr_remarks(osv.osv):
    _description="Remarks"
    _name = 'rb.vfsr.remarks'


    _columns = {
        'name':fields.char('Remarks', size=64, required=True),
        'description':fields.text('Remarks Description', size=64)
        }

rb_vfsr_remarks()
    


#######################################################################


class rb_crm_vfsr(osv.osv):
    _description="VFSR Upload"
    _name = 'rb.crm.vfsr'

    def write(self, cr, uid, ids, values, context = None):
        #obj_grp = self.pool.get('res.groups')
        #grp_search = obj_grp.search(cr, uid, [('users','=',uid)])
        #grp_read = obj_grp.read(cr, uid, grp_search, ['name'], context)
        #for grp in grp_read:
        #    grp_name = grp['name']
         #   if grp_name == 'Sales Coordinator':
        #        check_flag = 1
         #   elif grp_name == 'Team Supervisor':
         #       check_flag = 2
        #    elif grp_name == 'VFSR QA':
        #        check_flag = 3
       # if (check_flag!=1) and (('correct_person' in values) or ('tl_met' in values) or ('agent_status_app' in values) or ('agent_status_loans' in values) or ('scheme_incentive' in values) or ('scheme_contest' in values) or ('app_till_date' in values) or ('case_apps_status' in values) or ('support_tl' in values) or ('received_payout' in values) or ('comment' in values) or ('loan_till_date' in values)):
        #    raise osv.except_osv(('warning'),('Only Sales Coordinator can change'))
       # if (('purpose_of_call' in values) or ('agent_status_app_ts' in values) or ('agent_status_loans_ts' in values) or ('scheme_incentive_ts' in values) or ('first_loan' in values) or ('training_recomendate' in values) or ('app_till_date_ts' in values) or ('loan_till_date_ts' in values) or ('received_payout_ts' in values) or ('notes_ts' in values)) and check_flag!=2:
        #    raise osv.except_osv(('warning'),('Only Team Supervisor can change'))
       # if (check_flag!=3) and (('cic_before_login_app' in values) or ('customer_personally' in values) or ('originals_documents' in values) or ('customer_eligibility' in values) or ('notes_qa' in values)):
        #    raise osv.except_osv(('warning'),('Only VFSR QA can change'))
        res = super(rb_crm_vfsr,self).write(cr, uid, ids, values, context = context)
        return res

    

    def end_call(self, cr, uid, ids, context=None):

                
		var='null'
		getserver = 'null'
		mobile = context['mobilex']
		xmlvar = 'null'

		var_ip = 'null'
		var_uname = 'null'
		var_pswd = 'null'
		var_callparam = 'null'
		var_endparam = 'null'
		global_last_call_id = 'null'
		last_lead = 0
		obj = self.pool.get('res.users')

		obj_astric = self.pool.get('rb.crm.call.server')


                obj_self = self.pool.get('rb.crm.vfsr')
                obj_self_read = obj_self.read(cr, uid, ids, ['last_call_id','id'], context)
                for var_read_obj in obj_self_read:
                    if(var_read_obj['id']==context['id']):
                        global_last_call_id = var_read_obj['last_call_id']
                ids = obj.search(cr, uid, [('id','=',uid)])


		res = obj.read(cr, uid, ids, ['server_name','internal_number','id','last_vfsr_id'], context) #---
		for r in res:
			if (r['id']==uid):
				
				getserver = r['server_name']
				#raise osv.except_osv(('warning'),(getserver[0]))
				var = r['internal_number']
				last_lead = r['last_vfsr_id']
				astric_id = obj_astric.search(cr, uid, [('id','=',getserver[0])])
				rs = obj_astric.read(cr, uid, astric_id, ['ip_address','server_user_id','server_user_pswd','api_url','api_url_realease'], context)
				for s in rs:

					if (s['id']==getserver[0]):
						#raise osv.except_osv(('warning'),('Inside If Block'))
						var_ip = s['ip_address']
						var_uname = s['server_user_id']
						var_pswd = s['server_user_pswd']
						var_callparam = s['api_url']
						var_endparam = s['api_url_realease']



				if(r['internal_number']==False):
					raise osv.except_osv(('warning'),('Agent No is Not Assigned'))
				var = r['internal_number']
		
		xmlvar = 'http://'+var_ip+'/'+var_endparam+'?xml=<request><security><username>'+var_uname+'</username><password>'+var_pswd+'</password></security><content><agent>'+var+'</agent></content></request>'
		#raise osv.except_osv(('warning'),(xmlvar))
		#urllib2.urlopen(xmlvar)
                callend_information = self.pool.get('crm.save.calldetails')
                #if False in(context['remarks']):
                    #raise osv.except_osv(('warning'),('Select Remarks')) 

                vvar=callend_information.browse(cr, uid, global_last_call_id, context)

                call_start =vvar['s_call_time']
                #raise osv.except_osv(('warning'),(datetime.datetime.now()))
                #call_start = call_start.replace(' ','')
                call_start = datetime.strptime(call_start, "%Y-%m-%d %H:%M:%S.%f")

                differ = datetime.now() - call_start

    

                callend_information.write(cr, uid, global_last_call_id, {'differ_time':differ,'s_endcall_time':datetime.now(),'remarks':context['remarks']}, context=None)
                #raise osv.except_osv(('warning'),(obj.search(cr, uid, [('last_vfsr_id','=',last_lead)])))
		obj.write(cr, uid, uid, {'last_vfsr_id':context['id']}) #----------
		self.write(cr, uid, context['id'], {'state': 'draft'})
		
		return True
		




		


	









    def custom_export(self, cr, uid, ids, context=None):
		var='null'
		getserver = 'null'
		mobile = context['mobilex']
		xmlvar = 'null'

		var_ip = 'null'
		var_uname = 'null'
		var_pswd = 'null'
		var_callparam = 'null'
		var_endparam = 'null'
		#domain = {'dispose':['disposition_status','in',context['disposition_status']]}
		obj = self.pool.get('res.users')
                
		obj_astric = self.pool.get('rb.crm.call.server')

	

		ids = obj.search(cr, uid, [('id','=',uid)])


		res = obj.read(cr, uid, ids, ['server_name','internal_number','id','last_vfsr_id','dial_state_vfsr'], context)
		
		for r in res:
			if (r['id']==uid):
                            if r['last_vfsr_id']:
                                    last_lead_state = self.read(cr, uid, r['last_vfsr_id'], ['state'], context)
                                    #raise osv.except_osv(('warning'),(r['last_vfsr_id']))
                                    if (last_lead_state and last_lead_state['state']=='Hangup'):
                                            raise osv.except_osv(('warning'),('Please Hangup Lead No:'+str(r['last_vfsr_id'])))
                            
                            getserver = r['server_name']
                            #raise osv.except_osv(('warning'),(str(r['internal_number'])))
                            var = r['internal_number']
				
                            astric_id = obj_astric.search(cr, uid, [('id','=',getserver[0])])
                            rs = obj_astric.read(cr, uid, astric_id, ['ip_address','server_user_id','server_user_pswd','api_url','api_url_realease'], context)
                            for s in rs:

                                        if (s['id']==getserver[0]):
                                                #raise osv.except_osv(('warning'),('Inside If Block'))
                                                var_ip = s['ip_address']
                                                var_uname = s['server_user_id']
                                                var_pswd = s['server_user_pswd']
                                                var_callparam = s['api_url']
                                                var_endparam = s['api_url_realease']



                            if(r['internal_number']==False):
                                    raise osv.except_osv(('warning'),('Agent No is Not Assigned'))
                            var = r['internal_number']
                        save_information = self.pool.get('crm.save.calldetails')
                        last_id = save_information.create(cr, uid,{'name':str(var),'s_ip_address': var_ip,'s_agent_id':int(var),'s_user_name':int(uid),'remarks':int(context['remarks']),'s_call_time':datetime.now(),'rela_vfsr':int(context['id']),'mobile':mobile}, context=None)
                        xmlvar = 'http://'+var_ip+'/'+var_callparam+'?xml=<request><security><username>'+var_uname+'</username><password>'+var_pswd+'</password></security><content><agent>'+var+'</agent><phoneNumber>'+mobile+'</phoneNumber><server>'+var_ip+'</server><leadId>'+str(context['id'])+'</leadId><callId>'+str(last_id)+'</callId></content></request>'
    
                        response=urllib2.urlopen(xmlvar)
                        self.global_saveid = last_id
                        #raise osv.except_osv(('warning'),(last_id))
                        self.write(cr, uid, context['id'], {'state': 'Hangup','last_call_id':last_id,'remarks':False})
                        obj.write(cr, uid, ids, {'last_vfsr_id':context['id']})
		
		return True



    def default_get(self, cr, uid, fields, context=None):
        check_flag = 0
        obj_grp = self.pool.get('res.groups')
        data = super(rb_crm_vfsr, self).default_get(cr, uid, fields, context=context)
        grp_search = obj_grp.search(cr, uid, [('users','=',uid)])
        grp_read = obj_grp.read(cr, uid, grp_search, ['name'], context)
        for grp in grp_read:
            grp_name = grp['name']
            if grp_name == 'Sales Coordinator':
                check_flag = 1
            if grp_name == 'Team Supervisor':
                check_flag = 2
        if check_flag == 1:
            data['vfsr_state']='SC'
            #obj_sales_team = self.pool.get('rb.vfsr.team')
            #team_search = obj_sales_team.search(cr, uid, [('sales_coordenater','=',uid)])
            #team_read = obj_sales_team.read(cr, uid, team_search, ['name','id'], context)
            #data['vfsr_team_id']=team_read
        elif check_flag == 2:
            data['vfsr_state']='TS'
            #obj_sales_team = self.pool.get('rb.vfsr.team')
            #team_search = obj_sales_team.search(cr, uid, [('sales_coordenater','=',uid)])
            #team_read = obj_sales_team.read(cr, uid, team_search, ['name','id'], context)
            #data['vfsr_team_id']=team_read
        data['fsr_assign']=uid
        data['state']="draft"
        
        return data

    def onchange_get_phone(self,cr,uid,ids,vfsr_id,context=None):
        res_object = self.pool.get('res.users')
        phone_info = res_object.read(cr, uid,vfsr_id, ['mobile'], context)
        #raise osv.except_osv(('warning'),(phone_info['mobile']))
        val = {'mobile':phone_info['mobile']}                                
	return {'value': val}



    def send_function(self,cr,uid,ids,context=None):
            create_uid = self.read(cr, uid, ids, ['create_uid'], context)
            if create_uid[0]['create_uid'][0] == uid:
                self.write(cr, uid, ids, {'vfsr_state': 'qa'})
            else:
                raise osv.except_osv(('warning'),('You can not forward'))
            
	    return True


    
    _columns = {
        'name': fields.char('VFSR Subject', size=64, required=True),
	'mobile':fields.char("Mobile"),
        'create_uid' : fields.many2one('res.users', 'by User', readonly=True),
	'vfsr_team_id':fields.many2one('rb.vfsr.team','VFSR Team',change_default=True),
        'remarks':fields.many2one('rb.vfsr.remarks',"Remarks"),
        'fsr_assign':fields.many2one('res.users','Team Supervisor/Sales Coordinator'),
        'vfsr_state':fields.char("VFSR State"),
        'state':fields.char("state"),
        'last_call_id':fields.integer("Last Call ID"),
        'comment':fields.text("Note Sales Coordinator"),
        'rela2saveCall':fields.one2many('crm.save.calldetails', 'rela_vfsr', 'VFS Call History'),
        'vfsr':fields.many2one('res.users','VFSR'),
        'create_date' : fields.datetime('Date Created', readonly=True),
        'followup_date' : fields.datetime('Follow up date'),
        'call_date':fields.selection([('selection of date','selection of date'),('Followup date','Followup date'),('Review date','Review date')],'Call date / Last call date'),
        'correct_person':fields.selection([('VFSR','VFSR'),('other than VFSR','other than VFSR'),('VFSR family','VFSR family')],'Correct person?'),
        'tl_met':fields.selection([('0','0'),('1','1 -- 5'),('5','>5')],'how many time TL met in 1 month?'),
        'agent_status_app':fields.selection([('Active Agent Apps','Active Agent Apps'),('Non Active Agent Apps','Non Active Agent Apps'),('Resigned apps','Resigned apps')],'Agent Status - Apps'),
        'agent_status_loans':fields.selection([('Active Agent Apps','Active Agent Apps'),('Non Active Agent Apps','Non Active Agent Apps'),('Resigned apps','Resigned apps')],'Agent Status - Loans'),
        'scheme_incentive':fields.selection([('Yes','Yes'),('No','No'),('Not clear','Not clear')],'Scheme incentive'),
        'scheme_contest':fields.selection([('Yes','Yes'),('No','No'),('Not clear','Not clear')],'Scheme Contest'),
        'support_tl':fields.selection([('Good','Good'),('Average Support','Average Support'),('Worst','Worst')],'Support from TL?'),
        'case_apps_status':fields.selection([('Yes','Yes'),('No','No'),('huge followup','Huge Followup')],'Did you know your case/apps status ?'),
        'app_till_date':fields.selection([('Upto 5','Upto 5'),('Upto 10','Upto 10'),('Upto 15','Upto 15'),('Upto 25','Upto 25')],'how many App till th end of month?'),
        'loan_till_date':fields.selection([('Upto 5','Upto 5'),('Upto 10','Upto 10'),('Upto 15','Upto 15'),('Upto 25','Upto 25')],'how many Loans till th end of month?'),
        'received_payout':fields.selection([('Yes','Yes'),('No','No'),('Always late','Always late')],'Did you received your payout.'),

       
        
        
        'last_call_date':fields.selection([('selection of date','selection of date'),('Followup date','Followup date'),('Review date','Review date')],'Last Call date'),
        'purpose_of_call':fields.selection([('Followup/Review','Followup/Review'),('Apps status update','Apps status update'),('Loans status update','Loans status update')],'Purpose of call'),
        'agent_status_app_ts':fields.selection([('Active Agent Apps','Active Agent Apps'),('Non Active Agent Apps','Non Active Agent Apps'),('Resigned apps','Resigned apps')],'Agent Status - Apps'),
        'agent_status_loans_ts':fields.selection([('Active Agent Apps','Active Agent Apps'),('Non Active Agent Apps','Non Active Agent Apps'),('Resigned apps','Resigned apps')],'Agent Status - Loans'),
        'scheme_incentive_ts':fields.selection([('Yes','Yes'),('No','No'),('Not clear','Not clear')],'Scheme Contest / Incentives '),
        'first_loan':fields.selection([('First Loan','First Loan'),('Next slab','Next slab'),('Not clear','Not clear')],'First Loan / next slab intimation'),
        'training_recomendate':fields.selection([('Product / Policy','Product / Policy'),('Apps filling','Apps filling'),('Not Required','Not Required')],'Training recomemded by Team sup'),
        'app_till_date_ts':fields.selection([('Upto 5','Upto 5'),('Upto 10','Upto 10'),('Upto 15','Upto 15'),('Upto 25','Upto 25')],'how many App till th end of month?'),
        'loan_till_date_ts':fields.selection([('Upto 5','Upto 5'),('Upto 10','Upto 10'),('Upto 15','Upto 15'),('Upto 25','Upto 25')],'how many Loans till th end of month?'),
        'received_payout_ts':fields.selection([('Yes','Yes'),('No','No'),('Always late','Always late')],'Did you received your payout.'),

        'call_date_qa':fields.selection([('selection of date','selection of date'),('Followup date','Followup date'),('Review date','Review date')],'Call Date'),
        'notes_ts':fields.text("Note For Team Supervisor"),
        'notes_qa':fields.text("Note For QA"),
        'cic_before_login_app':fields.selection([('Yes','Yes'),('No','No'),('Donknow','Dont know')],'Did you check CIC before login apps'),
        'customer_personally':fields.selection([('Yes','Yes'),('No','No'),('Donknow','Dont know')],'Have you meet Customer  personally'),
        'originals_documents':fields.selection([('Yes','Yes'),('No','No'),('Donknow','Dont know')],'Did you check Originals Documents'),
        'customer_eligibility':fields.selection([('Yes','Yes'),('No','No'),('Dontknow','Dont know')],'Did Check customer eligibility'),

        'bcbtl' : fields.selection([('Yes','Yes'),('No','No')],'Ban co biet TL ?'),
        'know_about_rainbow' : fields.selection([('Yes','Yes'),('No','No')],'Do you know about Rainbow company?'),
        'loan_lst_3m': fields.selection([('Upto 5','Upto 5'),('Upto 10','Upto 10'),('Upto 15','Upto 15'),('Upto 25','Upto 25'),('More than 25','More than 25')],'How many Loans of the last 3 months?'),
        'app_end_month' : fields.selection([('Upto 5','Upto 5'),('Upto 10','Upto 10'),('Upto 15','Upto 15'),('Upto 25','Upto 25'),('More than 25','More than 25')],'How many App till the end of month?'),
        'loan_end_month': fields.selection([('Upto 5','Upto 5'),('Upto 10','Upto 10'),('Upto 15','Upto 15'),('Upto 25','Upto 25'),('More than 25','More than 25')],'How many Loans till the end of month?'),
        'face_difficult' : fields.selection([('Yes','Yes'),('No','No')],'Do you face any dificulties in work?'),
        'support_from_tl' : fields.selection([('Yes','Yes'),('No','No')],'Do you get the support from TL?'),
        'working_on_rainbow' : fields.selection([('Yes','Yes'),('No','No')],'Are you working in Rainbow?'),
        'notesforsc' : fields.char ('Note For Central Sales Coordinator'),

        
        }
rb_crm_vfsr()   
class crm_save_calldetails_inherit(osv.osv):
    
    _inherit = 'crm.save.calldetails'


    _columns = {
        'remarks':fields.many2one('rb.vfsr.remarks',"Remarks"),
        'rela_vfsr':fields.many2one('rb.crm.vfsr', 'Blank reference',select=False), ## Data <================================
        }

crm_save_calldetails_inherit()

###################################################

class res_users_inherit_view(osv.osv):
    
    _inherit = 'res.users'


    _columns = {
        'last_vfsr_id':fields.integer("Last VFSR Call ID"),
        'dial_state_vfsr':fields.char('Agent VFSR ID'),
        'vfsr_team':fields.many2many('rb.vfsr.team','rb_vfsr_team_rel','res_users_id','vfsr_team_id','VFSR Team'),
        'vfsr':fields.many2many('rb.vfsr.team','rb_vfsr_rel','res_users_id','vfsr_team_id','VFSR'),
        }

res_users_inherit_view()

###################################################

class rb_vfsr_team(osv.osv):
    _description="VFSR Team"
    _name = 'rb.vfsr.team'


    _columns = {
        'name':fields.char('Team Name', size=64, required=True),
        'description':fields.text('Team Description', size=64),
        #'sales_coordenater':fields.many2one('res.users','Sales Coordinator'),
        'sales_coordenater':fields.many2many('res.users','rb_vfsr_sc_team_rel','vfsr_team_id','res_users_id','Sales Coordinator'),
        'team_supervisor':fields.many2one('res.users','Team Supervisor'),
        'vfsr_qa':fields.many2many('res.users','rb_vfsr_team_rel','vfsr_team_id','res_users_id','VFSR QA'),
        'vfsr':fields.many2many('res.users','rb_vfsr_rel','vfsr_team_id','res_users_id','VFSR'),
        }

rb_vfsr_team()
