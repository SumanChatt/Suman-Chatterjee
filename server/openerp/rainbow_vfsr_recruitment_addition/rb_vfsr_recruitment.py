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

class vfsr_recruitment_process(osv.osv):
    _name = "vfsr.recruitment.process"


    def call(self, cr, uid, ids, context=None):
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


		res = obj.read(cr, uid, ids, ['server_name','internal_number','id','last_lead_id','dial_state'], context)
		
		for r in res:
			if (r['id']==uid):
                            if r['last_lead_id']:
                                    last_lead_state = self.read(cr, uid, r['last_lead_id'], ['state'], context)
                                    if (last_lead_state and last_lead_state['state']=='Hangup'):
                                            raise osv.except_osv(('warning'),('Please Hangup Lead No:'+str(r['last_lead_id'])))
                            
                            getserver = r['server_name']
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
                        save_information = self.pool.get('vfsr.application.call.history')
                        last_id = save_information.create(cr, uid,{'name':str(var),'s_ip_address': var_ip,'s_agent_id':int(var),'s_user_name':int(uid),'s_lead_id':int(context['id']),'s_call_time':datetime.now(),'rela_lead':int(context['id']),'mobile':mobile}, context=None)
                        xmlvar = 'http://'+var_ip+'/'+var_callparam+'?xml=<request><security><username>'+var_uname+'</username><password>'+var_pswd+'</password></security><content><agent>'+var+'</agent><phoneNumber>'+mobile+'</phoneNumber><server>'+var_ip+'</server><leadId>'+str(context['id'])+'</leadId><callId>'+str(last_id)+'</callId></content></request>'
                        response=urllib2.urlopen(xmlvar)
                        #response.close()
                        self.global_saveid = last_id
                        self.write(cr, uid, context['id'], {'state': 'Hangup','last_call_id':last_id,'disposition':False,'subdisposition':False,'gate':'all'})
                        obj.write(cr, uid, ids, {'last_lead_id':context['id']})
                        #call end here
		
		return True


    def hangup(self, cr, uid, ids, context=None):
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


                obj_self = self.pool.get('vfsr.recruitment.process')
                obj_self_read = obj_self.read(cr, uid, ids, ['last_call_id','id'], context)
                for var_read_obj in obj_self_read:
                    if(var_read_obj['id']==context['id']):
                        global_last_call_id = var_read_obj['last_call_id']
                        

                

		ids = obj.search(cr, uid, [('id','=',uid)])


		res = obj.read(cr, uid, ids, ['server_name','internal_number','id','last_lead_id'], context) #---
		for r in res:
			if (r['id']==uid):
				
				getserver = r['server_name']
				#raise osv.except_osv(('warning'),(getserver[0]))
				var = r['internal_number']
				last_lead = r['last_lead_id']
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
		urllib2.urlopen(xmlvar)
                callend_information = self.pool.get('vfsr.application.call.history')
                if False in(context['disposition_status'], context['subdisposition_status']):
                    raise osv.except_osv(('warning'),('Select Disposition And SubDisposition'))
                #if context['disposition_status'] is 12:
                      #raise osv.except_osv(('warning'),('Dialed data cannot have a  "New Lead" status')) 

                vvar=callend_information.browse(cr, uid, global_last_call_id, context)

                call_start =vvar['s_call_time']
                call_start = datetime.strptime(call_start, "%Y-%m-%d %H:%M:%S.%f")

                differ = datetime.now() - call_start
                callend_information.write(cr, uid, global_last_call_id, {'differ_time':differ,'s_endcall_time':datetime.now(),'s_disposition_id':context['disposition_status'],'s_subdisposition_id':context['subdisposition_status']}, context=None)
                obj.write(cr, uid, uid, {'last_lead_id':context['id']}) #----------
		self.write(cr, uid, context['id'], {'state': 'draft','gate':''})
		
		return True 










    

    _columns = {
        'mobile' : fields.char("Mobile"),
        'vfsr_name': fields.char("VFSR"),
        'locaton': fields.char("Location"),
        'name' : fields.char("National ID"),
        'dob': fields.date("Date Of Birth"),
        'team_leader': fields.char("Team Leader"),
        'Project': fields.char("Project"),
        'profession': fields.char("Profession"),
        'province' : fields.char("Province"),
        'disposition': fields.many2one('vfsr.disposition',"Disposition"),
        'subdisposition':fields.many2one('vfsr.sub.disposition',"Suib Disposition",domain="[('disposition','=',disposition)]"),
        'description' : fields.char('Note'),
        'state': fields.char('State'),
        'last_call_id' : fields.integer("Last Call ID"),
        'gate' : fields.char('Gate'),
        'calling_history':fields.one2many('vfsr.application.call.history', 'rela_lead', 'Calling History', readonly = True),
        }
    _defaults = {'state': 'draft'}
vfsr_recruitment_process()


class vfsr_disposition(osv.osv):
    _name = "vfsr.disposition"

    _columns = {

                'name': fields.char("Disposition"),
                'description': fields.char("Description"),
        }
vfsr_disposition()


class vfsr_sub_disposition(osv.osv):

    _name = "vfsr.sub.disposition"

    _columns = {

                'name': fields.char("SubDisposition"),
                'disposition': fields.many2one('vfsr.disposition',"Disposition"),
                'description': fields.char("Description"),
        }
vfsr_sub_disposition()


class vfsr_application_call_history(osv.osv):
        
    

	_name = "vfsr.application.call.history"
	_columns = {
			'name':fields.char("Subject",),
			's_ip_address':fields.char("Server Ip Address"),
			's_agent_id':fields.integer("Agent ID", ),
			's_user_name':fields.integer("Agent Login ID",),
			's_lead_id':fields.integer('Application Reference'),
			's_call_time': fields.datetime('Calling Time'),
			's_endcall_time': fields.datetime('Ending Time'),
                        's_disposition_id': fields.many2one('vfsr.disposition',"Disposition ID"),
                        's_subdisposition_id': fields.many2one('vfsr.sub.disposition',"Sub Disposition ID"),
			'rela_lead':fields.many2one('vfsr.recruitment.process', 'Blank reference',select=False), ## Data <================================
			'differ_time':fields.char('Duration'),
			'mobile':fields.char('Mobile'),
                        'record_url':fields.char("Recording View"),
			}


vfsr_application_call_history()

