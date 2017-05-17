# -*- coding: utf-8 -*-
from osv import fields, osv
from datetime import datetime, timedelta
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
from time import gmtime, strftime


AVAILABLE_PRIORITIES = [
    ('1', 'Highest'),
    ('2', 'High'),
    ('3', 'Normal'),
    ('4', 'Low'),
    ('5', 'Lowest'),
]

_logger = logging.getLogger(__name__)


  #This class is for  Disposition fields


class rb_city(osv.osv):

			
	_name = "rb.city"		
	
	_columns = {
			'name':fields.char("City Name",required=True)
			   }
rb_city()
  
class rb_campaign_crm(osv.osv):

			
	_name = "rb.campaign.crm"		
	
	_columns = {
			'name':fields.char("Campaign Name", required=True),
			
			'description':fields.char("Description", required=True),
                        'start_date':fields.date("Start Date"),
                        'end_date':fields.date("End Date"),
			'active':fields.boolean("Active")
			   }
rb_campaign_crm()	  
  
  
  
class rb_sales_team(osv.osv):
    _description="Sales Team"
    _name = 'rb.sales.team'
    _columns = {
        'name': fields.char('Sales Team', size=64, required=True),
	'description':fields.char("Project"),
	'team_member':fields.many2many('res.users','rb_sales_team_rel','sales_team_id','res_users_id','TSR'),
        'fpc_member':fields.many2many('res.users','rb_fpc_rel','sales_team_id','res_users_id','FPC'),
        'data_entry_group':fields.many2many('res.users','rb_data_entry_rel','dataentry_team_id','res_users_id','Data Entry Members'),
	'quality_asur_group':fields.many2one('rb.qa.team', 'QA Group'),
        'quality_doc_group':fields.many2one('rb.doc.qa.team', 'QA Doc Group'),
	'team_lead_group':fields.many2one('rb.tl.team', 'TL Group'),
        'sales_mgr_group':fields.many2one('rb.sm.team', 'PM Group'),
	'sales_admin_group':fields.many2one('rb.sa.team', 'SA Group'),
	'financial_conlt_group':fields.many2one('rb.fpc.team', 'FPC DE Group'),
	'campaign_name_id':fields.many2many('rb.campaign.crm','rb_campaign_team_rel','team_id','campaign_id','Campaign Name:'),
    #'enabled':fields.selection([('true','True'),('false','False')],string='Enabled'),
	'active':fields.boolean("Active")
    }

rb_sales_team()


class rb_team_campaign(osv.osv):

	_inherit = 'rb.campaign.crm'

	_columns = {

				
			'campaign_relation':fields.many2many('rb.sales.team','rb_campaign_team_rel','campaign_id','team_id','Team Name:')
					


	}

rb_team_campaign()


class rb_team_relation(osv.osv):

	_inherit = 'res.users'

	_columns = {

				
			'sales_team':fields.many2many('rb.sales.team','rb_sales_team_rel','res_users_id','sales_team_id','TSR Team Mapping'),
			'usr_lvl':fields.selection([('TSR','TSR'),('QA','QA')],string='User Level',required=True),
			'fpc_group':fields.many2many('rb.sales.team','rb_fpc_rel','res_users_id','sales_team_id','FPC Team Mapping'),		


	}

rb_team_relation()


class rb_qa_team(osv.osv):
    _description="QA Team"
    _name = 'rb.qa.team'
    _columns = {
        'name': fields.char('QA Team Name', size=64, required=True),
	'description':fields.char("Description"),
	'quality_asur':fields.many2many('res.users','rb_qa_team_rel','qa_team_id','res_users_id','QA'),
    }

rb_qa_team()


class rb_qa_team_relation(osv.osv):

	_inherit = 'res.users'

	_columns = {

				
			'qa_team':fields.many2many('rb.qa.team','rb_qa_team_rel','res_users_id','qa_team_id','Team Name'),
					


	}

rb_qa_team_relation()

class rb_doc_qa_team(osv.osv):
    _description="QA Team"
    _name = 'rb.doc.qa.team'
    _columns = {
        'name': fields.char('QA Doc Group Name', size=64, required=True),
	'description':fields.char("Description"),
	'quality_asur_doc':fields.many2many('res.users','rb_doc_qa_team_rel','doc_qa_team_id','res_users_id','QA Doc'),
    }

rb_qa_team()


class rb_doc_qa_team_relation(osv.osv):

	_inherit = 'res.users'

	_columns = {

				
			'qa_team':fields.many2many('rb.doc.qa.team','rb_doc_qa_team_rel','res_users_id','doc_qa_team_id','Team Name'),
					


	}

rb_qa_team_relation()

class rb_tl_team(osv.osv):
    _description="TL Team"
    _name = 'rb.tl.team'
    _columns = {
        'name': fields.char('TL Group Name', size=64, required=True),
	'description':fields.char("Description"),
	'tl_team':fields.many2many('res.users','rb_tl_team_rel','tl_team_id','res_users_id','TL'),
    }

rb_tl_team()









class rb_tl_team_relation(osv.osv):

	_inherit = 'res.users'

	_columns = {

				
			'tl_team':fields.many2many('rb.tl.team','rb_tl_team_rel','res_users_id','tl_team_id','TL Team Name'),
					


	}

rb_tl_team_relation()

class rb_sm_team(osv.osv):
    _description="PM Team"
    _name = 'rb.sm.team'
    _columns = {
        'name': fields.char('PM Group Name', size=64, required=True),
	'description':fields.char("Description"),
	'sm_team':fields.many2many('res.users','rb_sm_team_rel','sm_team_id','res_users_id','SM'),
    }

rb_tl_team()









class rb_sm_team_relation(osv.osv):

	_inherit = 'res.users'

	_columns = {

				
			'sm_team':fields.many2many('rb.sm.team','rb_sm_team_rel','res_users_id','sm_team_id','PM Team Name'),
					


	}

rb_tl_team_relation()

class rb_sa_team(osv.osv):
    _description="SA Team"
    _name = 'rb.sa.team'
    _columns = {
        'name': fields.char('SA Group Name', size=64, required=True),
	'description':fields.char("Description"),
	'sa_team':fields.many2many('res.users','rb_sa_team_rel','sa_team_id','res_users_id','SA'),
    }

rb_sa_team()









class rb_sa_team_relation(osv.osv):

	_inherit = 'res.users'

	_columns = {

				
			'sa_team':fields.many2many('rb.sa.team','rb_sa_team_rel','res_users_id','sa_team_id','SA Team Name'),
					


	}

rb_sa_team_relation()


class rb_fpc_team(osv.osv):
    _description="FPC Team"
    _name = 'rb.fpc.team'
    _columns = {
        'name': fields.char('FPC Group Name', size=64, required=True),
	'description':fields.char("Description"),
	'fpc_team':fields.many2many('res.users','rb_fpc_group_rel','fpc_team_id','res_users_id','FPC'),
    }

rb_fpc_team()









class rb_fpc_group_relation(osv.osv):

	_inherit = 'res.users'

	_columns = {

				
			'fpc_team':fields.many2many('rb.fpc.team','rb_fpc_group_rel','res_users_id','fpc_team_id','FPC Team Name'),
					


	}

rb_fpc_group_relation()











class rb_crm_disposition(osv.osv):




                


        _name = 'rb.crm.disposition'
        _description = 'Disposition'
        _columns = {
                        'name': fields.char('Disposition Name', size=64,help='The full name of the country.', required=True, translate=True),
                        'short_code':fields.char('Short Code', size=64, required=True),
			'dis_type':fields.selection([('tsr','TSR'),('qa','QA'),('tl','TL'),('sa','SA'),('fpc','FPC'),('qa doc','QA Doc'),('all','All')],string='Type')
                   }

        _sql_constraints = [
                             ('name_uniq', 'unique (name)','must be unique !'),
                             ('code_uniq', 'unique (short_code)','must be unique !')
                           ]


        _order='name'

    #    name_search = location_name_search
           
rb_crm_disposition()





   #This class is for Sub Disposition fields


class rb_crm_sub_dispotion(osv.osv):
    _description="Sub Disposition"
    _name = 'rb.crm.sub.disposition'
    _columns = {
        'disposition_status': fields.many2one('rb.crm.disposition', 'Disposition',required=True),
        'name': fields.char('Sub Disposition Name', size=64, required=True),
		'short_code':fields.char('Short Code', size=64, required=True),
	'rank':fields.integer("Rank",size=64,required=True),
	'description':fields.char("Description"),
        'forwardable':fields.boolean("Forward able")
    }		
	 

rb_crm_sub_dispotion()





class rb_crm_batch_code(osv.osv):




                


        _name = 'rb.crm.batch.code'
        _description = 'Batch Code'
        _columns = {
                        'name': fields.char('Batch Code', size=64, required=True, translate=True),
						'vendore':fields.char('Vendor', size=64),
						'description':fields.char('Desciption', size=64, required=True, translate=True),
						'db_cost':fields.float('Cost'),
						'db_date':fields.date('Date'),
                                                'database_name':fields.char('Database Name', size=64),
                                                'qty':fields.integer("Quantity"),
                                                'batch_no':fields.char('Batch No', size=64)
                   }

    #    name_search = location_name_search
           
rb_crm_batch_code()



class rb_crm_call_server(osv.osv):

    _name = "rb.crm.call.server"
    _columns = {
            'name':fields.char("Server Name",size=64, required=True),
			'ip_address':fields.char("IP addr. or DNS",size=64, required=True),
			'server_user_id':fields.char("Server User ID", required=True),
			'server_user_pswd':fields.char("Server User Password", required=True),
			'api_url':fields.text('API URL (Make Call)'),
			'api_url_realease':fields.text('API URL (Release Call) '),
			'active_stat':fields.selection([('1','Active'),('0','Inavtive')],"Status",size=64, required=True)
            }

rb_crm_call_server()

class rb_create_agent_id(osv.osv):

	_inherit = 'res.users'

	_columns = {

				'internal_number':fields.char('Agent ID'),
				'server_name':fields.many2one('rb.crm.call.server', 'Call Server',domain="[('active_stat','=','1')]"),
                                'last_lead_id':fields.integer("Last Call ID"),
                                'dial_state':fields.char('Agent ID'),
                                'national_id':fields.char('National ID'),
                                'employee_code':fields.char('Employee Code'),
                                'joining_date':fields.datetime('Joining Date'),
                                'resigned_date':fields.datetime('Resigned Date'),
                                'mobile':fields.char('Mobile'),

	}

rb_create_agent_id()


class rb_file_export(osv.osv):


        def func_lead_export_sa(self, cr, uid, ids, context=None):
                lst = []
                m_lst = []
                t_id = []
                fiel_name = datetime.now().strftime('%Y-%m-%d-%H:%M:%S')+'.csv'
                file_path = '/var/www/report/reportdaily'+fiel_name
                #raise osv.except_osv(('warning'),(file_path))
                file_obj = self.pool.get('rb.crm.lead')
                resultFile = open(file_path,'wb')
                wr = csv.writer(resultFile,dialect='excel')
                ids = context['active_ids']
                k= []
                k=['ID','Name','Contact Persion','Mobile','Phone','Campaign','Sales Team','QA Group','TL','SALES MANAGER GROUP','Sales Admin Group','QA Doc Group','FPC Group','TSR','Disposition','Sub Disposition','Batch Code','Company','Callback Date','Appo Date','Birthday','Home Phone','Age','Email ID','Gender','Street','LandMark','Zip','City','State Id','Country ID','Title','FPC','ID Card','Voter Id Card','Passport','Pan Card','Residence','Occupation','Own Company','Type Of Company','Designation','Employee Type','Taxable','PaySlip','Maritorial Status','Degree','Monthly Income','Anul Income','Experience','No Of Family','No Of Employers','No Of Child','Education','Billing Address','Permanent Address','Dist Type','Description']
                for p in k:
                        m_lst.append(p)
                wr.writerow(m_lst)
                m_lst=[]
                for var in ids:
                        x = file_obj.read(cr, uid, var,[],context)
			m_lst.append(x['id'])
                        m_lst.append(x['name'].encode("utf-8"))
                        if(x['contact_persion'] !=False):
                            m_lst.append(x['contact_persion'].encode("utf-8"))
                        else:
                            m_lst.append('False')
                        m_lst.append(str(x['mobile']))
                        m_lst.append(str(x['phone']))
                        m_lst.append(x['campaign_team'][1].encode("utf-8"))
                        m_lst.append(x['sale_team_name'][1].encode("utf-8"))
                        if(x['quality_asur'] !=False):m_lst.append(x['quality_asur'][1].encode("utf-8"))
                        if(x['team_lead'] !=False):m_lst.append(x['team_lead'][1].encode("utf-8"))
                        if(x['sales_mngr'] !=False):m_lst.append(x['sales_mngr'][1].encode("utf-8"))
                        if(x['sales_admin'] !=False):m_lst.append(x['sales_admin'][1].encode("utf-8"))
                        if(x['quality_doc_group'] !=False):m_lst.append(x['quality_doc_group'][1].encode("utf-8"))
                        if(x['financial_p_conlt'] !=False):m_lst.append(x['financial_p_conlt'][1].encode("utf-8"))
                        if(x['sales_team_r'] !=False):m_lst.append(x['sales_team_r'][1].encode("utf-8"))
                        if(x['disposition_status'] !=False):m_lst.append(str(x['disposition_status'][1]))
                        if(x['subdisposition_status'] !=False):m_lst.append(str(x['subdisposition_status'][1]))
                        if(x['batch_code'] !=False):m_lst.append(x['batch_code'][1].encode("utf-8"))
                        if(x['company_name'] !=False):
                            m_lst.append(x['company_name'].encode("utf-8"))
                        else:
                            m_lst.append('False')
                        m_lst.append(str(x['callback_date']))
                        m_lst.append(str(x['appo_date']))
                        m_lst.append(str(x['birth_date']))
                        m_lst.append(str(x['home_phone']))
                        m_lst.append(str(x['age']))
                        if(x['email_id'] !=False):
                            m_lst.append(x['email_id'].encode("utf-8"))
                        else:
                            m_lst.append('False')
                        m_lst.append(str(x['gender']))
                        if(x['street'] !=False):
                            m_lst.append(x['street'].encode("utf-8"))
                        else:
                            m_lst.append('False')
                        if(x['street2'] !=False):
                            m_lst.append(x['street2'].encode("utf-8"))
                        else:
                            m_lst.append('False')
                        if(x['zip'] !=False):
                            m_lst.append(x['zip'].encode("utf-8"))
                        else:
                            m_lst.append('False')
                        if(x['city'] !=False):
                            m_lst.append(x['city'].encode("utf-8"))
                        else:
                            m_lst.append('False')
                        if(x['state_id'] !=False):
                            m_lst.append(x['state_id'][1].encode("utf-8"))
                        else:
                            m_lst.append('False')
                        if(x['country_id'] !=False):
                            m_lst.append(x['country_id'][1].encode("utf-8"))
                        else:
                            m_lst.append('False')
                        if(x['title'] !=False):
                            m_lst.append(x['title'][1].encode("utf-8"))
                        else:
                            m_lst.append('False')
                        if(x['fpc_user'] !=False):
                            m_lst.append(x['fpc_user'][1].encode("utf-8"))
                        else:
                            m_lst.append('False')
                        m_lst.append(str(x['id_card_no']))
                        m_lst.append(str(x['voter_id']))
                        m_lst.append(str(x['passport_id']))
                        m_lst.append(str(x['pan_no']))
                        m_lst.append(str(x['residence_type']))
                        m_lst.append(str(x['occupation']))
                        if(x['company_name'] !=False):
                            m_lst.append(x['company_name'].encode("utf-8"))
                        else:
                            m_lst.append('False')
                        m_lst.append(str(x['type_company']))
                        if(x['designation'] !=False):
                            m_lst.append(x['designation'].encode("utf-8"))
                        else:
                            m_lst.append('False')
                        m_lst.append(str(x['employee_type']))
                        m_lst.append(str(x['taxable']))
                        m_lst.append(str(x['pay_slip']))
                        m_lst.append(str(x['marital_status']))
                        if(x['degree'] !=False):
                            m_lst.append(x['degree'].encode("utf-8"))
                        else:
                            m_lst.append('False')
                        m_lst.append(str(x['monthly_income']))
                        m_lst.append(str(x['annual_income']))
                        if(x['exprience'] !=False):
                            m_lst.append(x['exprience'].encode("utf-8"))
                        else:
                            m_lst.append('False')
                        m_lst.append(str(x['no_of_family']))
                        m_lst.append(str(x['no_of_employeed']))
                        m_lst.append(str(x['no_of_child']))
                        if(x['education_institution'] !=False):
                            m_lst.append(x['education_institution'].encode("utf-8"))
                        else:
                            m_lst.append('False')
                        if(x['billing_add'] !=False):
                            m_lst.append(x['billing_add'].encode("utf-8"))
                        else:
                            m_lst.append('False')
                        if(x['permanent_add'] !=False):
                            m_lst.append(x['permanent_add'].encode("utf-8"))
                        else:
                            m_lst.append('False')
                        if(x['dis_type'] !=False):
                            m_lst.append(x['dis_type'].encode("utf-8"))
                        else:
                            m_lst.append('False')
                        #if(x['description'] !=False):
                            #m_lst.append(((str(x['description'])).replace('\n', '')).encode("utf-8"))
                        #else:
                            #m_lst.append('False')
                        wr.writerow(m_lst)
                        m_lst = []
                webbrowser.open_new_tab('http://10.0.0.1/report/report83473785.csv')
                url = 'http://10.0.0.1/report/reportdaily'+fiel_name
                if url:
                        return { 'type': 'ir.actions.act_url', 'url': url, 'nodestroy': True, 'target': 'new' }
                else:
                        return True


                


	_name = 'rb.file.export'


rb_file_export()



class rb_crm_lead(osv.osv):


        check_group = 0
        #####################################################################################################################
                         
        #####################################################################################################################


        def  group_featch_sales(self,cr,uid,domain,context=None):                             
                ids_campaign = []
                campaign_select = []
                lst_of_campaign = [] ##consist dictionary of disposition based on state change
                obj_sales_team =  self.pool.get('rb.sales.team')
                _logger.error('-----------Campaign Group------------>>>'+str(domain))
                ids_sales_team = obj_sales_team.search(cr, uid,domain) ##Dynamic key here
                rs_lst_campaign = obj_sales_team.read(cr, uid, ids_sales_team, ['quality_asur_group','quality_doc_group','team_lead_group','sales_mgr_group','sales_admin_group','financial_conlt_group'], context)
                _logger.error('Campaign--->>>'+str(rs_lst_campaign))
                for drs in rs_lst_campaign:
                        obj_dyn_group = self.pool.get('rb.sales.team')

                        
                        quality_asur_group = drs['quality_asur_group']
                        if(quality_asur_group != False):
                                get_group = obj_dyn_group.read(cr, uid,quality_asur_group[0],['name','id'], context)
                                get_group_name = get_group['name']
                                get_group_id = get_group['id']
                                pair_dispo = "("+str(get_group_name)+","+str(get_group_id)+")"
                                campaign_select.append(pair_dispo)

                        
                        quality_doc_group = drs['quality_doc_group']
                        if(quality_doc_group != False):
                                get_group = obj_dyn_group.read(cr, uid,quality_doc_group[0],['name','id'], context)
                                get_group_name = get_group['name']
                                get_group_id = get_group['id']
                                pair_dispo = "("+str(get_group_name)+","+str(get_group_id)+")"
                                campaign_select.append(pair_dispo)
                        
                        team_lead_group = drs['team_lead_group']
                        if(team_lead_group != False):
                                get_group = obj_dyn_group.read(cr, uid,team_lead_group[0],['name','id'], context)
                                get_group_name = get_group['name']
                                get_group_id = get_group['id']
                                pair_dispo = "("+str(get_group_name)+","+str(get_group_id)+")"
                                campaign_select.append(pair_dispo)
                        
                        sales_mgr_group = drs['sales_mgr_group']
                        if(sales_mgr_group != False):
                                get_group = obj_dyn_group.read(cr, uid,sales_mgr_group[0],['name','id'], context)
                                get_group_name = get_group['name']
                                get_group_id = get_group['id']
                                pair_dispo = "("+str(get_group_name)+","+str(get_group_id)+")"
                                campaign_select.append(pair_dispo)
                        
                        sales_admin_group = drs['sales_admin_group']
                        if(sales_admin_group != False):
                                get_group = obj_dyn_group.read(cr, uid,sales_admin_group[0],['name','id'], context)
                                get_group_name = get_group['name']
                                get_group_id = get_group['id']
                                pair_dispo = "("+str(get_group_name)+","+str(get_group_id)+")"
                                campaign_select.append(pair_dispo)
                        
                        financial_conlt_group = drs['financial_conlt_group']
                        if(financial_conlt_group != False):
                                get_group = obj_dyn_group.read(cr, uid,financial_conlt_group[0],['name','id'], context)
                                get_group_name = get_group['name']
                                get_group_id = get_group['id']
                                pair_dispo = "("+str(get_group_name)+","+str(get_group_id)+")"
                                campaign_select.append(pair_dispo)

                        #pair_dispo = "("+str(quality_asur_group)+","+str(quality_doc_group)+","+str(team_lead_group)+","+str(sales_mgr_group)+","+str(sales_admin_group)+")"
                        #campaign_select.append(pair_dispo)
                _logger.error('Campaign--->>>'+str(campaign_select))
                return campaign_select


        
        #####################################################################################################################
                         
        #####################################################################################################################


        def  get_tsr_campaign(self,cr,uid,domain,context=None):                             
                ids_campaign = []
                campaign_select = []
                lst_of_campaign = [] ##consist dictionary of disposition based on state change
                obj_campaign =  self.pool.get('rb.campaign.crm')
                obj_sales_team =  self.pool.get('rb.sales.team')
                ids_sales_team = obj_sales_team.search(cr, uid,domain) ##Dynamic key here
                rs_lst_campaign = obj_sales_team.read(cr, uid, ids_sales_team, ['campaign_name_id'], context)
                for camp in rs_lst_campaign:
                        campaignNo = camp.get('campaign_name_id')
                        for campaign_lst in campaignNo:
                                lst_of_campaign.append(campaign_lst) 
                _logger.error('List Of Campaign--->>>'+str(lst_of_campaign))
                
                
                rs_campaign = obj_campaign.read(cr, uid, lst_of_campaign, ['name','id'], context)
                _logger.error('Campaign--->>>'+str(rs_campaign))
                for drs in rs_campaign:
                        dsname = drs['name']
                        dsid = drs['id']
                        pair_dispo = "("+str(dsname)+","+str(dsid)+")"
                        campaign_select.append(pair_dispo)
                _logger.error('Campaign--->>>'+str(campaign_select))
                return campaign_select

       
        ###################################################################################################################
                                                                                                                                                                                
        ###################################################################################################################
        def  get_sales_team_tsr(self,cr,uid,domain,context=None):                             
                ids_sales_team = []
                lst_of_sales_team = [] ##consist dictionary of disposition based on state change
                obj_sales_team =  self.pool.get('rb.sales.team')
                ids_sales_team = obj_sales_team.search(cr, uid,domain) ##Dynamic key here
                rs_sales_team = obj_sales_team.read(cr, uid, ids_sales_team, ['name','id'], context)
                for drs in rs_sales_team:
                        dsname = drs['name']
                        dsid = drs['id']
                        pair_dispo = "("+str(dsname)+","+str(dsid)+")"
                        lst_of_sales_team.append(pair_dispo)
                return lst_of_sales_team

        #####################################################################################################################
                         
        #####################################################################################################################
        def get_total_lead(self,cr,uid,domain,context=None):
              _logger.error('Domain'+str(domain))  
              id_list =  super(rb_crm_lead, self).search(cr, uid, [],context=None,count=True)
              _logger.error('Total Lead No Of Leads--->>>'+str(id_list))
              return id_list
                
        ###################################################################################################################

        ###################################################################################################################

        ##################################################################################################################

        ##################################################################################################################

        def feedback_send_to(self,cr,uid,ids,context=None):
                _logger.error('#################    Feed Back'+str(ids))
                self.write(cr, uid, ids['id'], {'callback_state':'close'})
                return 'ok'
        

        ###################################################################################################################

        def get_user_name(self,cr,uid,context=None):
                obj_users = self.pool.get('res.users')
                patner = obj_users.read(cr, uid, uid, ['partner_id'], context)
                patner_id = patner['partner_id'][0]
                _logger.error('#################    Patner'+str(patner_id))
                obj_patner = self.pool.get('res.partner')
                search_user_details = obj_patner.read(cr, uid, patner_id, ['name'], context)
                user_name = search_user_details['name']
                return user_name

        #####################################################################################################################

        ###################################################################################################################

        def get_subdisposition(self,cr,uid,dispo_id,context=None):
                lst_of_subdispo_pair = []
                obj_subdisposition = self.pool.get('rb.crm.sub.disposition')
                ids_sub_disposition = obj_subdisposition.search(cr, uid, [])
                rs_sub_disposition = obj_subdisposition.read(cr, uid, ids_sub_disposition, ['name','id','disposition_status'], context)
                for each in rs_sub_disposition:
                        if(dispo_id == each['disposition_status'][0]):
                                sdname = each['name']
                                sdid = each['id']
                                pair_sub_dispo = "("+str(sdname)+","+str(sdid)+")"
                                lst_of_subdispo_pair.append(pair_sub_dispo)
                _logger.error(str(dispo_id)+'List Of Disposition'+str(lst_of_subdispo_pair))
                return lst_of_subdispo_pair

        #####################################################################################################################
        
        def convert_to_qa(self, cr, uid, ctxval, context=None):
                obj_dispo_history = self.pool.get('rb.crm.disposition.history')
                state_change_date = datetime.now().strftime('%Y-%m-%d 00:00:00')
                disposition = ctxval['disposition_status']
                subdisposition = ctxval['subdisposition_status']
                lead_id = ctxval['id']
                state = ctxval['state_change']
                obj_dispo = self.pool.get('rb.crm.disposition')
                obj_state_change_history = self.pool.get('rb.crm.stage.history')
		ids_dispo = obj_dispo.search(cr, uid, [('id','=',disposition)])
                obj_dispo_read = obj_dispo.read(cr, uid, ids_dispo, ['dis_type','id'], context)
                for dispo_stat in obj_dispo_read:
                        #raise osv.except_osv(('warning'),(dispo_stat['dis_type'])) 
                        if dispo_stat['dis_type'] not in state:
                                #self.write(cr, uid, ids, {'disposition_status':False,'subdisposition_status':False})
                                return 'Please Select Correct Disposition'              
                obj_subdisposition = self.pool.get('rb.crm.sub.disposition')
                
                subDisposition_search = obj_subdisposition.search(cr, uid, [('id','=',subdisposition)])
                obj_subdisposition_read = obj_subdisposition.read(cr, uid, subDisposition_search, ['forwardable','name'], context)
                #raise osv.except_osv(('warning'),(submition_date))
                for subdispo_stat in obj_subdisposition_read:
                        if subdispo_stat['forwardable'] is False:
                                return "Please Choose Correct Disposition For Forwarding"
                _logger.error('Total convert_to_qa--->>>'+str(ctxval))
                ctxval['state_change'] = 'qa'
                self.write(cr, uid, ctxval['id'],ctxval)
                obj_dispo_history.create(cr, uid,{'name':str(lead_id),'user_name':uid,'disposition_code':disposition,'subdisposition_code':subdisposition,'related_lead':lead_id,'submition_date':state_change_date}, context = context)
		obj_state_change_history.create(cr, uid,{'related_lead':lead_id,'previous_stage':state,'current_stage':'qa','concatination_field':str(state_change_date)+'qa'}, context = context)
		return 'ok'

        
        ###################################################################################################################
                                                                                                                                                                                
        ###################################################################################################################
        def  get_disposition(self,cr,uid,context=None):                             
                ids_disposition = []
                lst_of_dispo_pair = [] ##consist dictionary of disposition based on state change
                obj_disposition =  self.pool.get('rb.crm.disposition')
                ids_disposition = obj_disposition.search(cr, uid, ['|',('dis_type','=','tsr'),('dis_type','=','all')]) ##Dynamic key here
                rs_disposition = obj_disposition.read(cr, uid, ids_disposition, ['name','id'], context)
                for drs in rs_disposition:
                        dsname = drs['name']
                        dsid = drs['id']
                        pair_dispo = "("+str(dsname)+","+str(dsid)+")"
                        lst_of_dispo_pair.append(pair_dispo)
                return lst_of_dispo_pair
                         
        #####################################################################################################################
                         
        #####################################################################################################################
        def get_no_ofresults(self,cr,uid,domain,context=None):
              _logger.error('Domain'+str(domain))  
              id_list =  super(rb_crm_lead, self).search(cr, uid, domain,context=None,count=True)
              _logger.error('Total Lead with tsr--->>>'+str(id_list))
              return id_list
                
        ###################################################################################################################

        ###################################################################################################################
        def customtest(self, csr, uid,domain,offset,limit,field, context=None):
                _logger.error('Domain'+str(domain))
                _logger.error('Offset'+str(offset))
                _logger.error('Limit'+str(limit))
                _logger.error('Limit'+str(field))
                id_list = super(rb_crm_lead, self).search(csr, uid, domain, offset, limit,context=None)
                _logger.error('Total List'+str(id_list))
                return super(rb_crm_lead, self).read(csr, uid, id_list, field, context)
                
        ###################################################################################################################
        def totalCustomsearch(self, csr, uid,domain,context=None):
                id_list = super(rb_crm_lead, self).search(csr, uid, domain,context=None,count=True)
                _logger.error('No Of Search'+str(id_list))
                return id_list        
                   
        
        #######################################################################################

        def end_call_tab(self, cr, uid, ctxval, context=None):

                
		var='null'
		getserver = 'null'
		mobile = ctxval['mobilex']
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


                obj_self = self.pool.get('rb.crm.lead')
                obj_self_read = obj_self.read(cr, uid, ctxval['id'], ['last_call_id','id'], context)
                _logger.error(obj_self_read)
                if(obj_self_read['id']==ctxval['id']):
                        global_last_call_id = obj_self_read['last_call_id']
                #for var_read_obj in obj_self_read:
                   # _logger.error(var_read_obj['id'])    
                    #if(var_read_obj['id']==ctxval['id']):
                        #global_last_call_id = var_read_obj['last_call_id']
                        #raise osv.except_osv(('warning'),(global_last_call_id))

                

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
					return 'Agent No is Not Assigned'
				var = r['internal_number']
		
		xmlvar = 'http://'+var_ip+'/'+var_endparam+'?xml=<request><security><username>'+var_uname+'</username><password>'+var_pswd+'</password></security><content><agent>'+var+'</agent></content></request>'
		#raise osv.except_osv(('warning'),(xmlvar))
		#raise osv.except_osv(('warning'),(self.global_saveid))
                callend_information = self.pool.get('crm.save.calldetails')
                if False in(ctxval['disposition_status'], ctxval['subdisposition_status']):
                    return 'Select Disposition And SubDisposition'
                if ctxval['disposition_status'] is 12:
                      return 'Dialed data cannot have a  "New Lead" status' 

                vvar=callend_information.browse(cr, uid, global_last_call_id, context)

                call_start =vvar['s_call_time']
                #raise osv.except_osv(('warning'),(datetime.datetime.now()))
                #call_start = call_start.replace(' ','')
                call_start = datetime.strptime(call_start, "%Y-%m-%d %H:%M:%S.%f")

                differ = datetime.now() - call_start



                callend_information.write(cr, uid, global_last_call_id, {'differ_time':differ,'s_endcall_time':datetime.now(),'s_disposition_id':ctxval['disposition_status'],'s_subdisposition_id':ctxval['subdisposition_status']}, context=None)
                
		webbrowser.open(xmlvar)
		
		#search_dial_ids[] = obj.search(cr, uid, [('last_lead_id','=',last_lead)])   #--------
		#raise osv.except_osv(('warning'),(obj.search(cr, uid, [('last_lead_id','=',last_lead)])))
		obj.write(cr, uid, uid, {'last_lead_id':ctxval['id']}) #----------
		self.write(cr, uid, ctxval['id'], {'state': 'draft','gate':''})
		
		return 'ok'


	
		

        #######################################################################################
	def erp_call(self, cr, uid,ctxval,context=None):
		var='null'
		getserver = 'null'
		mobile = ctxval['mobilex']
		xmlvar = 'null'

		var_ip = 'null'
		var_uname = 'null'
		var_pswd = 'null'
		var_callparam = 'null'
		var_endparam = 'null'
		last_lead_id = 'null'
		#domain = {'dispose':['disposition_status','in',ctxval['disposition_status']]}
		obj = self.pool.get('res.users')
                
		obj_astric = self.pool.get('rb.crm.call.server')

	

		ids = obj.search(cr, uid, [('id','=',uid)])


		res = obj.read(cr, uid, ids, ['server_name','internal_number','id','last_lead_id','dial_state'], ctxval)
		
		for r in res:
			if (r['id']==uid):
                            if r['last_lead_id']:
                                    last_lead_state = self.read(cr, uid, r['last_lead_id'], ['state'], ctxval)
                                    #raise osv.except_osv(('warning'),(r['last_lead_id']))
                                    if (last_lead_state and last_lead_state['state']=='Hangup'):
                                            last_lead_id = str(r['last_lead_id'])
                                            return last_lead_id
                                            #raise osv.except_osv(('warning'),('Please Hangup Lead No:'+str(r['last_lead_id'])))
                            
                            getserver = r['server_name']
                            #raise osv.except_osv(('warning'),(str(r['internal_number'])))
                            var = r['internal_number']
				
                            astric_id = obj_astric.search(cr, uid, [('id','=',getserver[0])])
                            rs = obj_astric.read(cr, uid, astric_id, ['ip_address','server_user_id','server_user_pswd','api_url','api_url_realease'], ctxval)
                            for s in rs:

                                        if (s['id']==getserver[0]):
                                                #raise osv.except_osv(('warning'),('Inside If Block'))
                                                var_ip = s['ip_address']
                                                var_uname = s['server_user_id']
                                                var_pswd = s['server_user_pswd']
                                                var_callparam = s['api_url']
                                                var_endparam = s['api_url_realease']



                            if(r['internal_number']==False):
                                    return 'Agent No is Not Assigned'
                            var = r['internal_number']
		
                        xmlvar = 'http://'+var_ip+'/'+var_callparam+'?xml=<request><security><username>'+var_uname+'</username><password>'+var_pswd+'</password></security><content><agent>'+var+'</agent><phoneNumber>'+mobile+'</phoneNumber></content></request>'
                        #raise osv.except_osv(('warning'),(xmlvar))
                        webbrowser.open(xmlvar)
                        #lead_id_information = self.pool.get('crm.lead')
                        #var_info = self.browse(cr, uid, ids, ctxval=ctxval)
                        #raise osv.except_osv(('warning'),(ctxval['id']))
                        #present_lead_id = lead_id_information.browse(cr, uid, ids, ctxval=ctxval)
                        #raise osv.except_osv(('warning'),(present_lead_id.id))
                        save_information = self.pool.get('crm.save.calldetails')
                        #raise osv.except_osv(('warning'),(ctxval['id']))
                        last_id = save_information.create(cr, uid,{'name':str(var),'s_ip_address': var_ip,'s_agent_id':int(var),'s_user_name':int(uid),'s_lead_id':int(ctxval['id']),'s_call_time':datetime.now(),'rela_lead':int(ctxval['id']),'mobile':mobile}, context=None)
                        #raise osv.except_osv(('warning'),(global_var))
                        self.global_saveid = last_id
                        #raise osv.except_osv(('warning'),(last_id))
                        self.write(cr, uid, ctxval['id'], {'state': 'Hangup','last_call_id':last_id,'disposition_status':False,'subdisposition_status':False,'gate':'all'})
                        obj.write(cr, uid, ids, {'last_lead_id':ctxval['id']})
		
		return last_lead_id

	#######################################################################################
        def get_last_lead(self, cr, uid, ids, context=None):
                obj = self.pool.get('res.users')
                ids = obj.search(cr, uid, [('id','=',uid)])
                res = obj.read(cr, uid, ids, ['last_lead_id','dial_state'], context)
                #return res['last_lead_id']
                
	##########################################################################################

##        def search(self, cr, user, args, offset=0, limit=None, order=None, context=None, count=False, xtra=None):
##                #raise osv.except_osv(('warning'),(args))
##                if (args and len(args)>0 and str(args[0]) == "['state', '=', 'today']"):
##                        args=[]
##                        newStartPeriod=datetime.today()
##                        newStartPeriod = newStartPeriod.replace(hour=0) #i wanted everything today, not just from this minute
##                        newStartPeriod = newStartPeriod.replace(minute=0) #if you want you can remove these and you
##                        newStartPeriod = newStartPeriod.replace(second=0) #will just get stuff after this second
##                        _logger.error('Todays Date-------'+str(newStartPeriod))
##                        args = [('date_convert_opp', '>=', newStartPeriod.strftime('%Y-%m-%d %H:%M:%S'))] 
##                        ret = super(rb_crm_lead,self).search(cr, user, args, offset, limit, order, context, count)
##                        
##                elif (args and len(args)>0 and str(args[0]) == "['state', '=', 'notcontact']"):
##                        args=[]
##                        ret=[]
##                        ret2=[]
##                        connectList=[]
##                        obj_sub_dispo_history = self.pool.get('rb.crm.disposition.history')
##                        newStartPeriod=datetime.today()
##                        newStartPeriod = newStartPeriod.replace(hour=0) #i wanted everything today, not just from this minute
##                        newStartPeriod = newStartPeriod.replace(minute=0) #if you want you can remove these and you
##                        newStartPeriod = newStartPeriod.replace(second=0) #will just get stuff after this second
##                        _logger.error('Todays Date-------'+str(newStartPeriod))
##                        ids = obj_sub_dispo_history.search(cr, user,[('create_date', '>=', newStartPeriod.strftime('%Y-%m-%d %H:%M:%S'))])
##                        _logger.error('Todays Date-------'+str(ids))
##                        disposition_read = obj_sub_dispo_history.read(cr, user, ids, ['disposition_code','related_lead'], context)
##                        _logger.error('Tupale-------'+str(disposition_read))
##                                
##                        for dispo in disposition_read:
##                                get_dispo_code = dispo.get('disposition_code')
##                                _logger.error('Disposition ********'+str(get_dispo_code[0]))
##                                if(get_dispo_code[0]==2):
##                                        get_lead_id = dispo.get('related_lead')
##                                        _logger.error('Lead Id'+str(get_lead_id[0]))
##                                        args = [('id', '=', get_lead_id[0])]
##                                else:
##                                        get_lead_id = dispo.get('related_lead')
##                                        connectList = [get_lead_id[0]] + connectList
##                                        args = [('id', '=', 0)]
##                                
##                                ret1 = super(rb_crm_lead,self).search(cr, user, args, offset, limit, order, context, count)
##                                ret = ret + ret1
##                        ret = list(set(ret))
##                        connectList = list(set(connectList))
##                        
##                        _logger.error('After Sorting-------'+str(connectList))
##                        _logger.error('After Sorting-------'+str(ret))
##                        
##                elif (args and len(args)>0 and str(args[0]) == "['state', '=', 'contact']"):
##                       
##                        args=[]
##                        ret=[]
##                        obj_sub_dispo_history = self.pool.get('rb.crm.disposition.history')
##                        newStartPeriod=datetime.today()
##                        newStartPeriod = newStartPeriod.replace(hour=0) #i wanted everything today, not just from this minute
##                        newStartPeriod = newStartPeriod.replace(minute=0) #if you want you can remove these and you
##                        newStartPeriod = newStartPeriod.replace(second=0) #will just get stuff after this second
##                        _logger.error('Todays Date-------'+str(newStartPeriod))
##                        ids = obj_sub_dispo_history.search(cr, user,[('create_date', '>=', newStartPeriod.strftime('%Y-%m-%d %H:%M:%S'))])
##                        _logger.error('Todays Date-------'+str(ids))
##                        disposition_read = obj_sub_dispo_history.read(cr, user, ids, ['disposition_code','related_lead'], context)
##                        _logger.error('Disposition-------'+str(disposition_read))
##                        for dispo in disposition_read:
##                                get_dispo_code = dispo.get('disposition_code')
##                                _logger.error('Disposition ********'+str(get_dispo_code[0]))
##                                if(get_dispo_code[0]!=2):
##                                        get_lead_id = dispo.get('related_lead')
##                                        _logger.error('Lead Id'+str(get_lead_id[0]))
##                                        args = [('id', '=', get_lead_id[0])]
##                                else:
##                                        args = [('id', '=', 0)]
##                                ret1 = super(rb_crm_lead,self).search(cr, user, args, offset, limit, order, context, count)
##                                ret = ret + ret1
##                        ret = list(set(ret))
##                        _logger.error('After Sorting-------'+str(ret))
##
##                elif (args and len(args)>0 and str(args[0]) == "['state', '=', 'yesterday']"):
##                        args=[]
##                        newStartPeriod=datetime.today() - timedelta(hours=24)
##                        #raise osv.except_osv(('warning'),(newStartPeriod))
##                        newStartPeriod = newStartPeriod.replace(hour=0) #i wanted everything today, not just from this minute
##                        newStartPeriod = newStartPeriod.replace(minute=0) #if you want you can remove these and you
##                        newStartPeriod = newStartPeriod.replace(second=0) #will just get stuff after this second
##                        _logger.error('Todays Date-------'+str(newStartPeriod))
##                        todaysDate=datetime.today()
##                        #raise osv.except_osv(('warning'),(newStartPeriod))
##                        todaysDate = todaysDate.replace(hour=0) #i wanted everything today, not just from this minute
##                        todaysDate = todaysDate.replace(minute=0) #if you want you can remove these and you
##                        todaysDate = todaysDate.replace(second=0) #will just get stuff after this second
##                        args = [('relation2statechange.concatination_field', '=', newStartPeriod.strftime('%Y-%m-%d %H:%M:%S')+'fpc')]  
##                        ret = super(rb_crm_lead,self).search(cr, user, args, offset, limit, order, context, count)
##                        
##                elif (args and len(args)>0 and str(args[0]) == "['state', '=', 'mtd']"):
##                        obj_stage_history = self.pool.get('rb.crm.stage.history')
##                        args=[]
##                        ret=[]
##                        today = date.today()
##                        currentYear = today.year + 1
##                        currentMonth = today.month
##                        currentDay = 1
##                        currentPeriod = date(today.year, today.month,currentDay)
##                        #raise osv.except_osv(('warning'),(currentPeriod))
##                        newStartPeriod=datetime.today()
##                        newStartPeriod = newStartPeriod.replace(hour=0) #i wanted everything today, not just from this minute
##                        newStartPeriod = newStartPeriod.replace(minute=0) #if you want you can remove these and you
##                        newStartPeriod = newStartPeriod.replace(second=0) #will just get stuff after this second
##                        day_diffrence = (today-currentPeriod).days
##                        args = ['&',('date_convert_opp', '>=', currentPeriod.strftime('%Y-%m-%d %H:%M:%S')),('state_change','!=','Reject')] 
##                        ret = super(rb_crm_lead,self).search(cr, user, args, offset, limit, order, context, count)
##
##
##
##
##
##
##
##                elif (args and len(args)>0 and str(args[0]) == "['state', '=', 'notcontactyesterday']"):
##                       
##                        args=[]
##                        ret=[]
##                        obj_sub_dispo_history = self.pool.get('rb.crm.disposition.history')
##                        newStartPeriod=datetime.today() -  timedelta(hours=24)
##                        newStartPeriod = newStartPeriod.replace(hour=0) #i wanted everything today, not just from this minute
##                        newStartPeriod = newStartPeriod.replace(minute=0) #if you want you can remove these and you
##                        newStartPeriod = newStartPeriod.replace(second=0) #will just get stuff after this second
##                        today=datetime.today()
##                        today = today.replace(hour=0) #i wanted everything today, not just from this minute
##                        today = today.replace(minute=0) #if you want you can remove these and you
##                        today = today.replace(second=0) #will just get stuff after this second
##                        _logger.error('Todays Date-------'+str(newStartPeriod))
##                        ids = obj_sub_dispo_history.search(cr, user,['&',('create_date', '>=', newStartPeriod.strftime('%Y-%m-%d %H:%M:%S')),('create_date', '<', today.strftime('%Y-%m-%d %H:%M:%S'))])
##                        _logger.error('Todays Date-------'+str(ids))
##                        disposition_read = obj_sub_dispo_history.read(cr, user, ids, ['disposition_code','related_lead'], context)
##                        _logger.error('Disposition-------'+str(disposition_read))
##                        for dispo in disposition_read:
##                                get_dispo_code = dispo.get('disposition_code')
##                                _logger.error('Disposition ********'+str(get_dispo_code[0]))
##                                if(get_dispo_code[0]==2):
##                                        get_lead_id = dispo.get('related_lead')
##                                        _logger.error('Lead Id'+str(get_lead_id[0]))
##                                        args = [('id', '=', get_lead_id[0])]
##                                else:
##                                        args = [('id', '=', 0)]
##                                ret1 = super(rb_crm_lead,self).search(cr, user, args, offset, limit, order, context, count)
##                                ret = ret + ret1
##                        ret = list(set(ret))
##                        _logger.error('After Sorting-------'+str(ret))
##
##                elif (args and len(args)>0 and str(args[0]) == "['state', '=', 'contactyesterday']"):
##                       
##                        args=[]
##                        ret=[]
##                        obj_sub_dispo_history = self.pool.get('rb.crm.disposition.history')
##                        newStartPeriod=datetime.today() -  timedelta(hours=24)
##                        newStartPeriod = newStartPeriod.replace(hour=0) #i wanted everything today, not just from this minute
##                        newStartPeriod = newStartPeriod.replace(minute=0) #if you want you can remove these and you
##                        newStartPeriod = newStartPeriod.replace(second=0) #will just get stuff after this second
##                        today=datetime.today()
##                        today = today.replace(hour=0) #i wanted everything today, not just from this minute
##                        today = today.replace(minute=0) #if you want you can remove these and you
##                        today = today.replace(second=0) #will just get stuff after this second
##                        _logger.error('Todays Date-------'+str(newStartPeriod))
##                        ids = obj_sub_dispo_history.search(cr, user,['&',('create_date', '>=', newStartPeriod.strftime('%Y-%m-%d %H:%M:%S')),('create_date', '<', today.strftime('%Y-%m-%d %H:%M:%S'))])
##                        _logger.error('Todays Date-------'+str(ids))
##                        disposition_read = obj_sub_dispo_history.read(cr, user, ids, ['disposition_code','related_lead'], context)
##                        _logger.error('Disposition-------'+str(disposition_read))
##                        for dispo in disposition_read:
##                                get_dispo_code = dispo.get('disposition_code')
##                                _logger.error('Disposition ********'+str(get_dispo_code[0]))
##                                if(get_dispo_code[0]!=2):
##                                        get_lead_id = dispo.get('related_lead')
##                                        _logger.error('Lead Id'+str(get_lead_id[0]))
##                                        args = [('id', '=', get_lead_id[0])]
##                                else:
##                                        args = [('id', '=', 0)]
##                                ret1 = super(rb_crm_lead,self).search(cr, user, args, offset, limit, order, context, count)
##                                ret = ret + ret1
##                        ret = list(set(ret))
##                        _logger.error('After Sorting-------'+str(ret))
##
##                else:
##                        ret = super(rb_crm_lead,self).search(cr, user, args, offset, limit, order, context, count)
##                return ret
                

        def write(self, cr, uid, ids, values, context = None):
                #raise osv.except_osv(('warning'),(ids))
                var_for_wiz_1 = self.browse(cr, uid, ids, context=context) #@%@%@%
		#raise osv.except_osv(('warning'),(var_for_wiz_1['tsr_change_flag']))
                get_group_name = 'null'
                get_all_grp = []
                current_grp = 0
                prev_grp = 0
                var_status = 'null'
                res = False
                lead_id = 0
                dispo_id = 0
                remarks = ' '
                get_disposition_status = ''
                submition_date = date.today().strftime('%Y-%m-%d')
                obj_dispo_history = self.pool.get('rb.crm.disposition.history')
                obj_disposition = self.pool.get('rb.crm.disposition')
                if 'sales_team_r' in values:
                        if var_for_wiz_1['tsr_change_flag'] !=True: #********** Tweak Here ***** 7
                                raise osv.except_osv(('warning'),('You have no permission to change TSR'))
                if 'state_change' in values:
                        res = super(rb_crm_lead,self).write(cr, uid, ids, values, context = context)
                        return res
                elif ('rela2fpcvisit' in values):
                        size = len(values['rela2fpcvisit']) - 1
                        get_disposition = values['rela2fpcvisit'][size][2]
                        res = super(rb_crm_lead,self).write(cr, uid, ids, {'submition_date':submition_date,'disposition_status':get_disposition['disposition_status'],'subdisposition_status':get_disposition['subdisposition_status']}, context = context)
                        #res = super(rb_crm_lead,self).write(cr, uid, ids,{'submition_date':submition_date}, context = context)
                        if 'remarks' in values:
                                remarks = values['remarks']
                        #_logger.error('State Stae-------'+var_status)
                        #raise osv.except_osv(('warning'),(ids))        
                        obj_dispo_history.create(cr, uid,{'name':str(lead_id),'user_name':uid,'disposition_code':get_disposition['disposition_status'],'subdisposition_code':get_disposition['subdisposition_status'],'related_lead':ids[0],'submition_date':submition_date,'remarks':remarks}, context = context)
                        #raise osv.except_osv(('warning'),(get_disposition['disposition_status']))
                        
                elif ('state' not in values) and ('callback_state' not in values):
                        
                        #raise osv.except_osv(('warning'),(values))
                        cr.execute('select gid from res_groups_users_rel where uid=%s',(uid,))
                        group_id = cr.fetchall()
                        for all_grp in group_id:
                                cr.execute('select name from res_groups where id=%s',(all_grp,))
                                group_name = cr.fetchone()[0]
                                if group_name == 'TSR' or group_name == 'QA' or group_name == 'FPC DE' or group_name == 'QA Doc' or group_name == 'SA' or group_name == 'TL' or group_name == 'FPC Users':
                                        rs_approve = self.read(cr, uid,ids, ['state_change','id','disposition_status'], context)
                                        #false_lst = [] #** MOD FOR WIZARD
                                        #false_lst.extend(rs_approve) #** MOD FOR WIZARD
					#raise osv.except_osv(('warning'),(rs_approve))
                                        if ("<type 'dict'>" in str(type(rs_approve))): #************* ADD 1  *************
                                                tmp_rs_approve =  rs_approve #************* ADD 2  *************
                                                rs_approve = [] #************* ADD 3
                                                rs_approve.append(tmp_rs_approve) #************* ADD 4  *************
					#raise osv.except_osv(('warning'),(rs_approve))
                                        for var in rs_approve:
                                                
                                                var_status= var['state_change']
                                                _logger.error('State Stae'+var_status)
						#gate_status =  var['gate']
                                                lead_id = var['id']
                                                if var['disposition_status']:
                                                        dispo_id = var['disposition_status'][0]
                                                if 'disposition_status' in values :        
                                                        dispo_stat_read =  obj_disposition.read(cr, uid,values['disposition_status'], ['dis_type'], context)
                                                        get_disposition_status = dispo_stat_read['dis_type']
                                                        if (values['disposition_status']==35 and var_status=='tsr'):
                                                                raise osv.except_osv(('Warning!'),("Please select Proper Disposition This disposition is only for Follow Up Stage"))
                                                        #for dispo in dispo_stat_read:
                                                        #raise osv.except_osv(('Warning!'),( get_disposition_status)) 
                                                                #get_disposition_status = str(dispo['dis_type'])
                                                         
                                                if (group_name == 'TSR' and var_status=='tsr') or (group_name == 'TSR' and var_status=='customer') or (group_name == 'TSR' and var_status=='qa') or (group_name == 'TSR' and var_status=='fpc') or (group_name == 'TSR' and var_status=='qa doc') or (group_name == 'TSR' and var_status=='sa') or (group_name == 'TSR' and var_status=='Reject'):
                                                        #raise osv.except_osv(('Warning!'),(dispo_id,get_group_name,var_status)) 
                                                        #res = super(rb_crm_lead,self).write(cr, uid, ids, values, context = context)
                                                        current_grp = 1
                                                        if 'disposition_status' in values : 
                                                                if (get_disposition_status != 'tsr' and group_name == 'TSR') and (get_disposition_status != 'all' and group_name == 'TSR'):     
                                                                        raise osv.except_osv(('Warning!'),("Please Select Correct Disposition"))
                                                elif group_name == 'QA' and var_status=='qa':
                                                        #res = super(rb_crm_lead,self).write(cr, uid, ids, values, context = context)
                                                        current_grp = 1
                                                        
                                                        if 'disposition_status' in values :
                                                                #raise osv.except_osv(('Warning!'),(get_disposition_status))
                                                                if (get_disposition_status != 'qa' and group_name == 'QA'):       
                                                                        raise osv.except_osv(('Warning!'),("Please Select Correct Disposition"))
                                                elif (group_name == 'FPC DE' and (var_status=='fpc' or var_status=='sa' or var_status=='qa doc')) or (group_name == 'FPC Users' and var_status=='fpc')  :
                                                        #res = super(rb_crm_lead,self).write(cr, uid, ids, values, context = context)
                                                        current_grp = 1
                                                        if 'disposition_status' in values : 
                                                                if (get_disposition_status != 'fpc' and group_name == 'FPC DE'):
                                                                        raise osv.except_osv(('Warning!'),("Please Select Correct Disposition"))
                                                elif (group_name == 'QA Doc' and var_status=='qa doc'):
                                                        #res = super(rb_crm_lead,self).write(cr, uid, ids, values, context = context)
                                                        current_grp = 1
                                                        if 'disposition_status' in values : 
                                                                if (get_disposition_status != 'qa doc' and group_name == 'QA Doc'):
                                                                        raise osv.except_osv(('Warning!'),("Please Select Correct Disposition"))
                                                elif (group_name == 'SA' and var_status=='sa'):
                                                        #res = super(rb_crm_lead,self).write(cr, uid, ids, values, context = context)
                                                        current_grp = 1
                                                        if 'disposition_status' in values : 
                                                                if (get_disposition_status != 'sa' and group_name == 'SA'):
                                                                        raise osv.except_osv(('Warning!'),("Please Select Correct Disposition"))
                        if current_grp == 1:
                                if 'disposition_status' in values or 'subdisposition_status' in values:
                                                                res_write = super(rb_crm_lead,self).write(cr, uid, ids, values, context = context)
                                                                res = super(rb_crm_lead,self).write(cr, uid, ids,{'submition_date':submition_date}, context = context)
                                                                if 'disposition_status' in values:
                                                                        dispo_id = values['disposition_status']
                                                                if 'remarks' in values:
                                                                        remarks = values['remarks']
                                                                _logger.error('State Stae-------'+var_status)
                                                                obj_dispo_history.create(cr, uid,{'name':str(lead_id),'user_name':uid,'disposition_code':dispo_id,'subdisposition_code':values['subdisposition_status'],'related_lead':lead_id,'submition_date':submition_date,'remarks':remarks}, context = context)
                                                                return res
                        else:
                                raise osv.except_osv(('Warning!'),("Yo don't have permission to change or modify"))
                
                #raise osv.except_osv(('Warning!'),(values))
                res = super(rb_crm_lead,self).write(cr, uid, ids, values, context = context)
                return res
                        
                                                

        def calculate_age(self,cr,uid,ids,field,context=None):
                #raise osv.except_osv(('warning'),(field)) 2014-03-17
                year, month, day = [int(x) for x in str(field).split("-")]
                born = date(year, month, day)
                
                today = date.today()
                try: 
                        birthday = born.replace(year=today.year)
                except ValueError:
                        birthday = born.replace(year=today.year, day=born.day-1)
                if birthday > today:
                        val = today.year - born.year - 1
                else:
                        val = today.year - born.year
                if val<0:
                	raise osv.except_osv(('Warning'),('You are not Eligible.'))
                else:
                	age = {'age': val}
                return {'value': age}

        def create(self, cr, uid, values, context=None):
                    state_change_date = datetime.now().strftime('%Y-%m-%d 00:00:00')
                    new_id = super(rb_crm_lead, self).create(cr, uid, values, context)
                    #self.write(cr, uid, int(new_id), {'date_convert_opp':state_change_date,'remarks':'Direct Lead'})
                    if ('state_change' in values and values['state_change'] == 'fpc'):
                            obj_state_change_history = self.pool.get('rb.crm.stage.history')
                            submition_date = date.today().strftime('%Y-%m-%d')
                            obj_dispo_history = self.pool.get('rb.crm.disposition.history')
                            obj_dispo_history.create(cr, uid,{'name':str(new_id),'user_name':uid,'disposition_code':3,'subdisposition_code':13,'related_lead':new_id,'submition_date':submition_date,'remarks':'Direct Lead'}, context = context)
                            obj_dispo_history.create(cr, uid,{'name':str(new_id),'user_name':uid,'disposition_code':6,'subdisposition_code':28,'related_lead':new_id,'submition_date':submition_date,'remarks':'Direct Lead'}, context = context)
                            obj_dispo_history.create(cr, uid,{'name':str(new_id),'user_name':uid,'disposition_code':values['disposition_status'],'subdisposition_code':values['subdisposition_status'],'related_lead':new_id,'submition_date':submition_date,'remarks':'Direct Lead'}, context = context)
                            obj_state_change_history.create(cr, uid,{'related_lead':new_id,'previous_stage':'tsr','current_stage':'qa','concatination_field':str(state_change_date)+'qa'}, context = context)
                            obj_state_change_history.create(cr, uid,{'related_lead':new_id,'previous_stage':'qa','current_stage':'fpc','concatination_field':str(state_change_date)+'fpc'}, context = context)
                    return new_id



        def default_get(self, cr, uid, fields, context=None):
                    check_flag = 0
                    obj_grp = self.pool.get('res.groups')
                    data = super(rb_crm_lead, self).default_get(cr, uid, fields, context=context)
                    if uid == 1:
                        data['state_change']='tsr'
                        data['state']='draft'
                        data['callback_state']='close'
                        return data
                        
                    grp_search = obj_grp.search(cr, uid, [('users','=',uid)])
                    grp_read = obj_grp.read(cr, uid, grp_search, ['name'], context)
                    for grp in grp_read:
                                grp_name = grp['name']
                                if grp_name == 'FPC DE' or grp_name == 'TL' or grp_name=='FPC Users':
                                        check_flag = 1
                                if grp_name == 'QA Doc':
                                        check_flag = 2
                    
                     
                    if check_flag == 1:
                            data['state_change']='fpc'
                            data['sales_team_r']=False
                            data['date_convert_opp'] = datetime.now().strftime('%Y-%m-%d 00:00:00')
                            #data['remarks'] = 'Direct Lead'
                            obj_sales_team = self.pool.get('rb.sales.team')
                            team_search = obj_sales_team.search(cr, uid, [('financial_conlt_group.fpc_team','=',uid)])
                            team_read = obj_sales_team.read(cr, uid, team_search, ['name','id'], context)
                            #data['sale_team_name']=team_read
                            if grp_name=='FPC Users':
                                    data['fpc_user']=uid
                    elif check_flag == 2:
                            data['state_change']='qa doc'
                            data['sales_team_r']=False
                            data['date_convert_opp'] = datetime.now().strftime('%Y-%m-%d 00:00:00')
                    else:
                            data['state_change']='tsr'
                            data['sales_team_r']=uid
                    data['state']='draft'
                    data['callback_state']='close'
                    
                    return data







        def _getTSR(self,cr,uid,context=None):
                lead_state = 'null'
                check_flag = 0
                obj_grp = self.pool.get('res.groups')
                grp_search = obj_grp.search(cr, uid, [('users','=',uid)])
                grp_read = obj_grp.read(cr, uid, grp_search, ['name'], context)
                for grp in grp_read:
                        grp_name = grp['name']
                        if grp_name == 'FPC DE' or grp_name == 'TL':
                                self.check_group =1
                                check_flag = 1

                if check_flag == 1:
                        return False
                else:
                        return uid
                






        def callback_tsr(self,cr,uid,ids,context=None):
                lead_state = 'null'
                check_flag = 0
                obj_grp = self.pool.get('res.groups')
                grp_search = obj_grp.search(cr, uid, [('users','=',uid)])
                rs_state = self.read(cr, uid,ids, ['state_change'], context)
                for state in rs_state:
                        lead_state = state['state_change']
                grp_read = obj_grp.read(cr, uid, grp_search, ['name'], context)
                for grp in grp_read:
                        grp_name = grp['name']
                        if grp_name == 'QA' and lead_state=='qa':
                                check_flag=1
                        elif (grp_name == 'SA' and lead_state=='sa') or (grp_name == 'SA' and lead_state=='customer'):
                                check_flag=1
                        elif grp_name == 'FPC DE' and lead_state=='fpc':
                                check_flag=1
                        elif grp_name == 'QA Doc' and lead_state=='qa doc':
                                check_flag=1        
                if check_flag == 0:
                        raise osv.except_osv(('warning'),('Please Select Only Your State lead'))
				#Modified by Sanjit
                self.write(cr, uid, context['id'], {'state_change': 'tsr'})        
                return {
                        'name':"Call Back Reason",
                        'view_mode': 'form',
                        'view_type': 'tree,form',
                        'res_model': 'rb.crm.callback.stage',
                        'type': 'ir.actions.act_window',
                        'nodestroy': True,
                        'target': 'new',
			'context': context.update({'send_user_id': uid,'id':id})
                        }


        def feedback_send(self,cr,uid,ids,context=None):
                #obj_stages = self.pool.get('rb.crm.callback.stage')
                self.write(cr, uid, ids, {'callback_state':'close'})
                return True

        def _total_score(self, cr, uid, ids, name, arg, context = None):
                res = { }
                for lead in self.browse(cr, uid, ids, context = context):
                    res[lead.id] = lead.score_income + lead.score_age + lead.score_occupation + lead.score_interest_level + lead.score_appoint_quality + lead.score_product + lead.score_call_length + lead.time_of_scoring + lead.score_income_range
                return res


        def func_lead_export_sa(self,cr,uid,ids,context):
                lst = []
                m_lst = []
                t_id = []
                resultFile = open("/opt/openerp/list.csv",'wb')
                wr = csv.writer(resultFile,dialect='excel')
                ids = context['active_ids']
                k= []
                k=['Name','Contact Persion','Mobile','Phone','Campaign','Sales Team','QA Group','TL','SALES MANAGER GROUP','Sales Admin Group','QA Doc Group','FPC Group','TSR','Disposition','Sub Disposition','Batch Code','Company','Callback Date','Appo Date','Birthday','Home Phone','Age','Email ID','Gender','Street','LandMark','Zip','City','State Id','Country ID','Title','FPC','ID Card','Voter Id Card','Passport','Pan Card','Residence','Occupation','Own Company','Type Of Company','Designation','Employee Type','Taxable','PaySlip','Maritorial Status','Degree','Monthly Income','Anul Income','Experience','No Of Family','No Of Employers','No Of Child','Education','Billing Address','Permanent Address','Dist Type','Description']
                for p in k:
                        m_lst.append(p)
                wr.writerow(m_lst)
                m_lst=[]
                for var in ids:
                        x = self.read(cr, uid, var,[],context)
                        m_lst.append(x['name'].encode("utf-8"))
                        m_lst.append(x['contact_persion'].encode("utf-8"))
                        m_lst.append(str(x['mobile']))
                        m_lst.append(str(x['phone']))
                        m_lst.append(x['campaign_team'][1].encode("utf-8"))
                        m_lst.append(x['sale_team_name'][1].encode("utf-8"))
                        if(x['quality_asur'] !=False):m_lst.append(x['quality_asur'][1].encode("utf-8"))
                        if(x['team_lead'] !=False):m_lst.append(x['team_lead'][1].encode("utf-8"))
                        if(x['sales_mngr'] !=False):m_lst.append(x['sales_mngr'][1].encode("utf-8"))
                        if(x['sales_admin'] !=False):m_lst.append(x['sales_admin'][1].encode("utf-8"))
                        if(x['quality_doc_group'] !=False):m_lst.append(x['quality_doc_group'][1].encode("utf-8"))
                        if(x['financial_p_conlt'] !=False):m_lst.append(x['financial_p_conlt'][1].encode("utf-8"))
                        if(x['sales_team_r'] !=False):m_lst.append(x['sales_team_r'][1].encode("utf-8"))
                        if(x['disposition_status'] !=False):m_lst.append(str(x['disposition_status'][1]))
                        if(x['subdisposition_status'] !=False):m_lst.append(str(x['subdisposition_status'][1]))
                        if(x['batch_code'] !=False):m_lst.append(x['batch_code'][1].encode("utf-8"))
                        if(x['company_name'] !=False):
                            m_lst.append(x['company_name'].encode("utf-8"))
                        else:
                            m_lst.append('False')
                        m_lst.append(str(x['callback_date']))
                        m_lst.append(str(x['appo_date']))
                        m_lst.append(str(x['birth_date']))
                        m_lst.append(str(x['home_phone']))
                        m_lst.append(str(x['age']))
                        if(x['email_id'] !=False):
                            m_lst.append(x['email_id'].encode("utf-8"))
                        else:
                            m_lst.append('False')
                        m_lst.append(str(x['gender']))
                        if(x['street'] !=False):
                            m_lst.append(x['street'].encode("utf-8"))
                        else:
                            m_lst.append('False')
                        if(x['street2'] !=False):
                            m_lst.append(x['street2'].encode("utf-8"))
                        else:
                            m_lst.append('False')
                        if(x['zip'] !=False):
                            m_lst.append(x['zip'].encode("utf-8"))
                        else:
                            m_lst.append('False')
                        if(x['city'] !=False):
                            m_lst.append(x['city'].encode("utf-8"))
                        else:
                            m_lst.append('False')
                        if(x['state_id'] !=False):
                            m_lst.append(x['state_id'][1].encode("utf-8"))
                        else:
                            m_lst.append('False')
                        if(x['country_id'] !=False):
                            m_lst.append(x['country_id'][1].encode("utf-8"))
                        else:
                            m_lst.append('False')
                        if(x['title'] !=False):
                            m_lst.append(x['title'][1].encode("utf-8"))
                        else:
                            m_lst.append('False')
                        if(x['fpc_user'] !=False):
                            m_lst.append(x['fpc_user'][1].encode("utf-8"))
                        else:
                            m_lst.append('False')
                        m_lst.append(str(x['id_card_no']))
                        m_lst.append(str(x['voter_id']))
                        m_lst.append(str(x['passport_id']))
                        m_lst.append(str(x['pan_no']))
                        m_lst.append(str(x['residence_type']))
                        m_lst.append(str(x['occupation']))
                        if(x['company_name'] !=False):
                            m_lst.append(x['company_name'].encode("utf-8"))
                        else:
                            m_lst.append('False')
                        m_lst.append(str(x['type_company']))
                        m_lst.append(str(x['designation']))
                        m_lst.append(str(x['employee_type']))
                        m_lst.append(str(x['taxable']))
                        m_lst.append(str(x['pay_slip']))
                        m_lst.append(str(x['marital_status']))
                        m_lst.append(str(x['degree']))
                        m_lst.append(str(x['monthly_income']))
                        m_lst.append(str(x['annual_income']))
                        m_lst.append(str(x['exprience']))
                        m_lst.append(str(x['no_of_family']))
                        m_lst.append(str(x['no_of_employeed']))
                        m_lst.append(str(x['no_of_child']))
                        if(x['education_institution'] !=False):
                            m_lst.append(x['education_institution'].encode("utf-8"))
                        else:
                            m_lst.append('False')
                        if(x['billing_add'] !=False):
                            m_lst.append(x['billing_add'].encode("utf-8"))
                        else:
                            m_lst.append('False')
                        if(x['permanent_add'] !=False):
                            m_lst.append(x['permanent_add'].encode("utf-8"))
                        else:
                            m_lst.append('False')
                        if(x['dis_type'] !=False):
                            m_lst.append(x['dis_type'].encode("utf-8"))
                        else:
                            m_lst.append('False')
                        if(x['description'] !=False):
                            m_lst.append(x['description'].encode("utf-8"))
                        else:
                            m_lst.append('False')
                        wr.writerow(m_lst)
                        m_lst = []





        def disposition_onchange(self,cr,uid,ids,context=None):
                var_subdisposition = False
                val = {'subdisposition_status':var_subdisposition,'remarks':False}

                return {'value': val}



        def fun_disposition(self,cr,uid,ids,dispo_stat,state_change,gate,context=None):
                val = {'remarks':False}                                
		return {'value': val}
        


        def returnyear(self, cursor, user_id, context=None):
                lst=[]
                var_rainbow_commission = 0.00
                toup=()
                for k in range(1,50):
                        toup=(str(k),str(k))
                        lst.append(toup)
                return lst
                
                

        def genarate_customer(self, cr, uid, ids,sub_disposition,id,context=None):
                    customer_lst='null'
                    obj_customer = self.pool.get('rb.customer.sale')
                    obj_lead = self.pool.get('rb.crm.lead')
                    ids = obj_lead.search(cr, uid, [('id','=',id)])
                    res_customer = obj_lead.read(cr, uid, ids, ['contact_persion'], context)
                    for r in res_customer:
                            customer_lst = r['contact_persion']
                            if sub_disposition == 48:
                                obj_customer.create(cr, uid,{'name':customer_lst,'details':id}, context=None)						
								
		    return True                                 

        

                
	def onchange_getage_qa(self,cr,uid,ids,team_id,context=None):
		var_qa = 'null'
		var_tl = 'null'
		var_sa = 'null'
		var_sm = 'null'
		obj = self.pool.get('res.users')
		obj_team = self.pool.get('rb.sales.team')
		ids = obj_team.search(cr, uid, [('id','=',team_id)])
		
		res = obj_team.read(cr, uid, ids, ['quality_asur_group','sales_mgr_group','team_lead_group','sales_admin_group','financial_conlt_group','quality_doc_group','id'], context)
		
		for r in res:

					var_qa = r['quality_asur_group']
					var_tl = r['team_lead_group']
					var_sa = r['sales_admin_group']
					var_fpc = r['financial_conlt_group']
					var_qa_doc = r['quality_doc_group']
					var_sm = r['sales_mgr_group']
					#raise osv.except_osv(('warning'),(r['sales_mgr_group']))
		val = {
            'quality_asur':var_qa,
			'sales_admin':var_sa,
			'team_lead':var_tl,
			'financial_p_conlt':var_fpc,
			'quality_doc_group':var_qa_doc,
                        'sales_mngr':var_sm    
        }
		return {'value': val}
		
		
	def approved_func(self,cr,uid,ids,context=None):
                state_change_date = datetime.now().strftime('%Y-%m-%d 00:00:00')
                disposition = context['disposition_status']
                subdisposition = context['subdisposition_status']
                state = context['state_change']
                obj_dispo = self.pool.get('rb.crm.disposition')
                #raise osv.except_osv(('warning'),(dispo_stat)) 
		ids_dispo = obj_dispo.search(cr, uid, [('id','=',disposition)])
                obj_dispo_read = obj_dispo.read(cr, uid, ids_dispo, ['dis_type','id'], context)
                for dispo_stat in obj_dispo_read:
                        #raise osv.except_osv(('warning'),(dispo_stat['dis_type'])) 
                        if dispo_stat['dis_type'] not in state:
                                #self.write(cr, uid, ids, {'disposition_status':False,'subdisposition_status':False})
                                raise osv.except_osv(('warning'),('Please Select Correct Disposition'))
                obj_subdisposition = self.pool.get('rb.crm.sub.disposition')
                subDisposition_search = obj_subdisposition.search(cr, uid, [('id','=',subdisposition)])
                obj_subdisposition_read = obj_subdisposition.read(cr, uid, subDisposition_search, ['forwardable','name'], context)
                for subdispo_stat in obj_subdisposition_read:
                        if subdispo_stat['forwardable'] is False:
                                raise osv.except_osv(('warning'),("Please Choose Correct Disposition For Forwarding"))    
		self.write(cr, uid, context['id'], {'state_change': 'fpc','date_convert_opp':state_change_date})
		obj_state_change_history = self.pool.get('rb.crm.stage.history')
                obj_state_change_history.create(cr, uid,{'related_lead':context['id'],'previous_stage':state,'current_stage':'fpc','concatination_field':str(state_change_date)+'fpc'}, context = context)
		return True


	def send_back_func(self,cr,uid,ids,context=None):
                state_change_date = datetime.now().strftime('%Y-%m-%d 00:00:00')
                disposition = context['disposition_status']
                subdisposition = context['subdisposition_status']
                state = context['state_change']
                obj_dispo = self.pool.get('rb.crm.disposition')
                #raise osv.except_osv(('warning'),(dispo_stat)) 
		ids_dispo = obj_dispo.search(cr, uid, [('id','=',disposition)])
                obj_dispo_read = obj_dispo.read(cr, uid, ids_dispo, ['dis_type','id'], context)
                for dispo_stat in obj_dispo_read:
                        #raise osv.except_osv(('warning'),(dispo_stat['dis_type'])) 
                        if dispo_stat['dis_type'] not in state:
                                #self.write(cr, uid, ids, {'disposition_status':False,'subdisposition_status':False})
                                raise osv.except_osv(('warning'),('Please Select Correct Disposition'))
                obj_subdisposition = self.pool.get('rb.crm.sub.disposition')
                subDisposition_search = obj_subdisposition.search(cr, uid, [('id','=',subdisposition)])
                obj_subdisposition_read = obj_subdisposition.read(cr, uid, subDisposition_search, ['forwardable','name'], context)
                for subdispo_stat in obj_subdisposition_read:
                        if subdispo_stat['forwardable'] :
                                raise osv.except_osv(('warning'),("Please Choose Correct Disposition For Forwarding")) 
		self.write(cr, uid, context['id'], {'state_change': 'tsr'})
		obj_state_change_history = self.pool.get('rb.crm.stage.history')
                obj_state_change_history.create(cr, uid,{'related_lead':context['id'],'previous_stage':state,'current_stage':'tsr','concatination_field':str(state_change_date)+'tsr'}, context = context)
		return True

        def reject_func(self,cr,uid,ids,context=None):
                state_change_date = datetime.now().strftime('%Y-%m-%d 00:00:00')
                disposition = context['disposition_status']
                subdisposition = context['subdisposition_status']
                state = context['state_change']
                obj_dispo = self.pool.get('rb.crm.disposition')
                #raise osv.except_osv(('warning'),(dispo_stat)) 
		ids_dispo = obj_dispo.search(cr, uid, [('id','=',disposition)])
                obj_dispo_read = obj_dispo.read(cr, uid, ids_dispo, ['dis_type','id'], context)
                for dispo_stat in obj_dispo_read:
                        #raise osv.except_osv(('warning'),(dispo_stat['dis_type'])) 
                        if dispo_stat['dis_type'] not in state:
                                #self.write(cr, uid, ids, {'disposition_status':False,'subdisposition_status':False})
                                raise osv.except_osv(('warning'),('Please Select Correct Disposition'))
                obj_subdisposition = self.pool.get('rb.crm.sub.disposition')
                subDisposition_search = obj_subdisposition.search(cr, uid, [('id','=',subdisposition)])
                obj_subdisposition_read = obj_subdisposition.read(cr, uid, subDisposition_search, ['forwardable','name'], context)
                for subdispo_stat in obj_subdisposition_read:
                        if subdispo_stat['forwardable'] :
                                raise osv.except_osv(('warning'),("Please Choose Correct Disposition For Forwarding")) 
		self.write(cr, uid, context['id'], {'state_change': 'Reject'})
		obj_state_change_history = self.pool.get('rb.crm.stage.history')
                obj_state_change_history.create(cr, uid,{'related_lead':context['id'],'previous_stage':state,'current_stage':'Reject','concatination_field':str(state_change_date)+'Reject'}, context = context)

		return True

        def send_back_QADoc(self,cr,uid,ids,context=None):
                state_change_date = datetime.now().strftime('%Y-%m-%d 00:00:00')
                disposition = context['disposition_status']
                subdisposition = context['subdisposition_status']
                state = context['state_change']
                obj_dispo = self.pool.get('rb.crm.disposition')
                #raise osv.except_osv(('warning'),(dispo_stat)) 
		ids_dispo = obj_dispo.search(cr, uid, [('id','=',disposition)])
                obj_dispo_read = obj_dispo.read(cr, uid, ids_dispo, ['dis_type','id'], context)
                for dispo_stat in obj_dispo_read:
                        #raise osv.except_osv(('warning'),(dispo_stat['dis_type'])) 
                        if dispo_stat['dis_type'] not in state:
                                #self.write(cr, uid, ids, {'disposition_status':False,'subdisposition_status':False})
                                raise osv.except_osv(('warning'),('Please Select Correct Disposition'))
                obj_subdisposition = self.pool.get('rb.crm.sub.disposition')
                subDisposition_search = obj_subdisposition.search(cr, uid, [('id','=',subdisposition)])
                obj_subdisposition_read = obj_subdisposition.read(cr, uid, subDisposition_search, ['forwardable','name'], context)
                for subdispo_stat in obj_subdisposition_read:
                        if subdispo_stat['forwardable'] :
                                raise osv.except_osv(('warning'),("Please Choose Correct Disposition For Forwarding")) 
		self.write(cr, uid, context['id'], {'state_change': 'fpc'})
		obj_state_change_history = self.pool.get('rb.crm.stage.history')
                obj_state_change_history.create(cr, uid,{'related_lead':context['id'],'previous_stage':state,'current_stage':'fpc','concatination_field':str(state_change_date)+'fpc'}, context = context)
		return True

        def reject_func_QADoc(self,cr,uid,ids,context=None):
                state_change_date = datetime.now().strftime('%Y-%m-%d 00:00:00')
                disposition = context['disposition_status']
                subdisposition = context['subdisposition_status']
                state = context['state_change']
                obj_dispo = self.pool.get('rb.crm.disposition')
                #raise osv.except_osv(('warning'),(dispo_stat)) 
		ids_dispo = obj_dispo.search(cr, uid, [('id','=',disposition)])
                obj_dispo_read = obj_dispo.read(cr, uid, ids_dispo, ['dis_type','id'], context)
                for dispo_stat in obj_dispo_read:
                        #raise osv.except_osv(('warning'),(dispo_stat['dis_type'])) 
                        if dispo_stat['dis_type'] not in state:
                                #self.write(cr, uid, ids, {'disposition_status':False,'subdisposition_status':False})
                                raise osv.except_osv(('warning'),('Please Select Correct Disposition'))
                obj_subdisposition = self.pool.get('rb.crm.sub.disposition')
                subDisposition_search = obj_subdisposition.search(cr, uid, [('id','=',subdisposition)])
                obj_subdisposition_read = obj_subdisposition.read(cr, uid, subDisposition_search, ['forwardable','name'], context)
                for subdispo_stat in obj_subdisposition_read:
                        if subdispo_stat['forwardable'] :
                                raise osv.except_osv(('warning'),("Please Choose Correct Disposition For Forwarding")) 
		self.write(cr, uid, context['id'], {'state_change': 'Reject'})
		obj_state_change_history = self.pool.get('rb.crm.stage.history')
                obj_state_change_history.create(cr, uid,{'related_lead':context['id'],'previous_stage':state,'current_stage':'Reject','concatination_field':str(state_change_date)+'Reject'}, context = context)
		return True

        
	def convert_qa(self, cr, uid, ids, context=None):
                # raise osv.except_osv(('Warning!'),(ids))
                customer_product_obj = self.pool.get('rb.crm.customer.product')
                customer_product_search = customer_product_obj.search(cr, uid, [('related_lead','=',ids[0])])
                
                if not customer_product_search:
                    raise osv.except_osv(('Warning!'),('Please enter the product details'))
                else:
                    customer_product_data = customer_product_obj.read(cr, uid, customer_product_search,['product_ammount'], context=None)
                    # raise osv.except_osv(('Warning!'),(customer_product_data[0].values()[1]))
                    if customer_product_data[0].values()[1] == 0:
                        raise osv.except_osv(('Warning!'),('Expected/Premium amount must be greater than 0.'))
                state_change_date = datetime.now().strftime('%Y-%m-%d 00:00:00')
                disposition = context['disposition_status']
                subdisposition = context['subdisposition_status']
                lead_id = context['id']
                state = context['state_change']
                obj_dispo = self.pool.get('rb.crm.disposition')
                obj_state_change_history = self.pool.get('rb.crm.stage.history')
		ids_dispo = obj_dispo.search(cr, uid, [('id','=',disposition)])
                obj_dispo_read = obj_dispo.read(cr, uid, ids_dispo, ['dis_type','id'], context)
                for dispo_stat in obj_dispo_read:
                        #raise osv.except_osv(('warning'),(dispo_stat['dis_type'])) 
                        if dispo_stat['dis_type'] not in state:
                                #self.write(cr, uid, ids, {'disposition_status':False,'subdisposition_status':False})
                                raise osv.except_osv(('warning'),('Please Select Correct Disposition'))               
                obj_subdisposition = self.pool.get('rb.crm.sub.disposition')
                #raise osv.except_osv(('warning'),(dispo_stat))
                subDisposition_search = obj_subdisposition.search(cr, uid, [('id','=',subdisposition)])
                obj_subdisposition_read = obj_subdisposition.read(cr, uid, subDisposition_search, ['forwardable','name'], context)
                #raise osv.except_osv(('warning'),(submition_date))
                for subdispo_stat in obj_subdisposition_read:
                        if subdispo_stat['forwardable'] is False:
                                raise osv.except_osv(('warning'),("Please Choose Correct Disposition For Forwarding"))
                self.write(cr, uid, context['id'], {'state_change': 'qa'})
		obj_state_change_history.create(cr, uid,{'related_lead':lead_id,'previous_stage':state,'current_stage':'qa','concatination_field':str(state_change_date)+'qa'}, context = context)
		return True

	def approved_func_fpc(self,cr,uid,ids,context=None):
                state_change_date = datetime.now().strftime('%Y-%m-%d 00:00:00')
                disposition = context['disposition_status']
                subdisposition = context['subdisposition_status']
                state = context['state_change']
                obj_dispo = self.pool.get('rb.crm.disposition')
                #raise osv.except_osv(('warning'),(dispo_stat))
                obj_crm_read = self.read(cr, uid,ids,['fpc_user'], context)
                if obj_crm_read is None:
                        raise osv.except_osv(('warning'),('Please Select Your Following FPC'))
		ids_dispo = obj_dispo.search(cr, uid, [('id','=',disposition)])
                obj_dispo_read = obj_dispo.read(cr, uid, ids_dispo, ['dis_type','id'], context)
                for dispo_stat in obj_dispo_read:
                        #raise osv.except_osv(('warning'),(dispo_stat['dis_type'])) 
                        if dispo_stat['dis_type'] not in state:
                                #self.write(cr, uid, ids, {'disposition_status':False,'subdisposition_status':False})
                                raise osv.except_osv(('warning'),('Please Select Correct Disposition'))
                obj_subdisposition = self.pool.get('rb.crm.sub.disposition')
                subDisposition_search = obj_subdisposition.search(cr, uid, [('id','=',subdisposition)])
                obj_subdisposition_read = obj_subdisposition.read(cr, uid, subDisposition_search, ['forwardable','name'], context)
                for subdispo_stat in obj_subdisposition_read:
                        if subdispo_stat['forwardable'] is False:
                                raise osv.except_osv(('warning'),("Please Choose Correct Disposition For Forwarding")) 
		self.write(cr, uid, context['id'], {'state_change': 'qa doc'})
		obj_state_change_history = self.pool.get('rb.crm.stage.history')
                obj_state_change_history.create(cr, uid,{'related_lead':context['id'],'previous_stage':state,'current_stage':'qa doc','concatination_field':str(state_change_date)+'qa doc'}, context = context)
		return True

        def approved_func_QADoc(self,cr,uid,ids,context=None):
                state_change_date = datetime.now().strftime('%Y-%m-%d 00:00:00')
                disposition = context['disposition_status']
                subdisposition = context['subdisposition_status']
                state = context['state_change']
                obj_dispo = self.pool.get('rb.crm.disposition')
                submition_date = date.today().strftime('%Y-%m-%d')
                #raise osv.except_osv(('warning'),(submition_date)) 
		ids_dispo = obj_dispo.search(cr, uid, [('id','=',disposition)])
                obj_dispo_read = obj_dispo.read(cr, uid, ids_dispo, ['dis_type','id'], context)
                for dispo_stat in obj_dispo_read:
                        #raise osv.except_osv(('warning'),(dispo_stat['dis_type'])) 
                        if dispo_stat['dis_type'] not in state:
                                #self.write(cr, uid, ids, {'disposition_status':False,'subdisposition_status':False})
                                raise osv.except_osv(('warning'),('Please Select Correct Disposition'))
                obj_subdisposition = self.pool.get('rb.crm.sub.disposition')
                subDisposition_search = obj_subdisposition.search(cr, uid, [('id','=',subdisposition)])
                obj_subdisposition_read = obj_subdisposition.read(cr, uid, subDisposition_search, ['forwardable','name'], context)
                for subdispo_stat in obj_subdisposition_read:
                        if subdispo_stat['forwardable'] is False:
                                raise osv.except_osv(('warning'),("Please Choose Correct Disposition For Forwarding")) 
		self.write(cr, uid, context['id'], {'state_change': 'sa','submition_date':submition_date})
		obj_state_change_history = self.pool.get('rb.crm.stage.history')
                obj_state_change_history.create(cr, uid,{'related_lead':context['id'],'previous_stage':state,'current_stage':'sa','concatination_field':str(state_change_date)+'sa'}, context = context)
		return True
		
	def reject_func_tl(self,cr,uid,ids,context=None):
                state_change_date = datetime.now().strftime('%Y-%m-%d 00:00:00')
                disposition = context['disposition_status']
                subdisposition = context['subdisposition_status']
                state = context['state_change']
                obj_dispo = self.pool.get('rb.crm.disposition')
                #raise osv.except_osv(('warning'),(dispo_stat)) 
		ids_dispo = obj_dispo.search(cr, uid, [('id','=',disposition)])
                obj_dispo_read = obj_dispo.read(cr, uid, ids_dispo, ['dis_type','id'], context)
                for dispo_stat in obj_dispo_read:
                        #raise osv.except_osv(('warning'),(dispo_stat['dis_type'])) 
                        if dispo_stat['dis_type'] not in state:
                                #self.write(cr, uid, ids, {'disposition_status':False,'subdisposition_status':False})
                                raise osv.except_osv(('warning'),('Please Select Correct Disposition'))
                obj_subdisposition = self.pool.get('rb.crm.sub.disposition')
                subDisposition_search = obj_subdisposition.search(cr, uid, [('id','=',subdisposition)])
                obj_subdisposition_read = obj_subdisposition.read(cr, uid, subDisposition_search, ['forwardable','name'], context)
                for subdispo_stat in obj_subdisposition_read:
                        if subdispo_stat['forwardable'] :
                                raise osv.except_osv(('warning'),("Please Choose Correct Disposition For Forwarding"))
		self.write(cr, uid, context['id'], {'state_change': 'Reject'})
		obj_state_change_history = self.pool.get('rb.crm.stage.history')
                obj_state_change_history.create(cr, uid,{'related_lead':context['id'],'previous_stage':state,'current_stage':'Reject','concatination_field':str(state_change_date)+'Reject'}, context = context)
		return True
		
	def approved_func_sa(self,cr,uid,ids,context=None):
                state_change_date = datetime.now().strftime('%Y-%m-%d 00:00:00')
		#customer_lst='null'
                in_no = ''
                disposition = context['disposition_status']
                subdisposition = context['subdisposition_status']
                state = context['state_change']
                obj_dispo = self.pool.get('rb.crm.disposition')
                #raise osv.except_osv(('warning'),(dispo_stat)) 
		ids_dispo = obj_dispo.search(cr, uid, [('id','=',disposition)])
                obj_dispo_read = obj_dispo.read(cr, uid, ids_dispo, ['dis_type','id'], context)
                #for dispo_stat in obj_dispo_read:
                        #raise osv.except_osv(('warning'),(dispo_stat['dis_type'])) 
                        #if dispo_stat['dis_type'] not in state:
                                #self.write(cr, uid, ids, {'disposition_status':False,'subdisposition_status':False})
                                #raise osv.except_osv(('warning'),('Please Select Correct Disposition'))
                obj_subdisposition = self.pool.get('rb.crm.sub.disposition')
                subDisposition_search = obj_subdisposition.search(cr, uid, [('id','=',subdisposition)])
                obj_subdisposition_read = obj_subdisposition.read(cr, uid, subDisposition_search, ['forwardable','name'], context)
                #for subdispo_stat in obj_subdisposition_read:
                        #if subdispo_stat['forwardable'] is False:
                               # raise osv.except_osv(('warning'),("Please Choose Correct Disposition For Forwarding")) 
                obj_customer = self.pool.get('rb.customer.sale')
                obj_lead = self.pool.get('rb.crm.lead')
                #ids = obj_lead.search(cr, uid, [('id','=',id)])
                res_customer = obj_lead.read(cr, uid,ids, ['contact_persion','state_change'], context)
                for r in res_customer:
                        #customer_lst = r['contact_persion']
                        #raise osv.except_osv(('warning'),(r['contact_persion']))
                        try:
                               max_id = str(max(self.pool.get("rb.customer.sale").search(cr, uid, [])))
                               max_id=int(max_id)+1
                               max_id=str(max_id)
                               in_no = 'CUST-'+str(datetime.now().month)+'-'+str(datetime.now().day)+'-'+str(datetime.now().year)+'-'+max_id
                        except Exception:
                               in_no = 'CUST-'+str(datetime.now().month)+'-'+str(datetime.now().day)+'-'+str(datetime.now().year)+'-'+'1'
                        obj_customer.create(cr, uid,{'name': r['contact_persion'],'details':context['id'],'customer_id':in_no}, context=None)
			self.write(cr, uid, context['id'], {'state_change': 'customer'})
		obj_state_change_history = self.pool.get('rb.crm.stage.history')
                obj_state_change_history.create(cr, uid,{'related_lead':context['id'],'previous_stage':state,'current_stage':'customer','concatination_field':str(state_change_date)+'customer'}, context = context)
		return True	
			
	def reject_func_sa(self,cr,uid,ids,context=None):
                state_change_date = datetime.now().strftime('%Y-%m-%d 00:00:00')
                disposition = context['disposition_status']
                subdisposition = context['subdisposition_status']
                state = context['state_change']
                obj_dispo = self.pool.get('rb.crm.disposition')
                #raise osv.except_osv(('warning'),(dispo_stat)) 
		ids_dispo = obj_dispo.search(cr, uid, [('id','=',disposition)])
                obj_dispo_read = obj_dispo.read(cr, uid, ids_dispo, ['dis_type','id'], context)
                #for dispo_stat in obj_dispo_read:
                        #raise osv.except_osv(('warning'),(dispo_stat['dis_type'])) 
                        #if dispo_stat['dis_type'] not in state:
                                #self.write(cr, uid, ids, {'disposition_status':False,'subdisposition_status':False})
                                #raise osv.except_osv(('warning'),('Please Select Correct Disposition'))
                obj_subdisposition = self.pool.get('rb.crm.sub.disposition')
                subDisposition_search = obj_subdisposition.search(cr, uid, [('id','=',subdisposition)])
                obj_subdisposition_read = obj_subdisposition.read(cr, uid, subDisposition_search, ['forwardable','name'], context)
                #for subdispo_stat in obj_subdisposition_read:
                        #if subdispo_stat['forwardable'] :
                                #raise osv.except_osv(('warning'),("Please Choose Correct Disposition For Forwarding")) 
		self.write(cr, uid, context['id'], {'state_change': 'tsr'})
		obj_state_change_history = self.pool.get('rb.crm.stage.history')
                obj_state_change_history.create(cr, uid,{'related_lead':context['id'],'previous_stage':state,'current_stage':'Reject','concatination_field':str(state_change_date)+'Reject'}, context = context)
		return True


        def _getTeam(self,cr,uid,context=None):
                obj_team = 'null'
                cr.execute('select sales_team_id from rb_sales_team_rel where res_users_id=%s',(uid,))
                sales_team = cr.fetchone()[0]
                
                #raise osv.except_osv(('warning'),(sales_team))
                return sales_team

        def _getCampaign(self,cr,uid,context=None):
                cr.execute('select sales_team_id from rb_sales_team_rel where res_users_id=%s',(uid,))
                obj_team = cr.fetchone()[0]
                obj_campaign = self.pool.get('rb.sales.team')
                ids_campaign = obj_campaign.search(cr, uid, [('id','=',obj_team)])
                obj_campaign_read = obj_campaign.read(cr, uid, ids_campaign, ['campaign_name_id'], context)

                for var_read_campaign in obj_campaign_read:
                        return var_read_campaign['campaign_name_id']



	def end_call(self, cr, uid, ids, context=None):

                start_time = datetime.now()
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


                obj_self = self.pool.get('rb.crm.lead')
                obj_self_read = obj_self.read(cr, uid, ids, ['last_call_id','id'], context)
                for var_read_obj in obj_self_read:
                    if(var_read_obj['id']==context['id']):
                        global_last_call_id = var_read_obj['last_call_id']
                        #raise osv.except_osv(('warning'),(global_last_call_id))

                

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
		#raise osv.except_osv(('warning'),(xmlvar))
		urllib2.urlopen(xmlvar)
                callend_information = self.pool.get('crm.save.calldetails')
                if False in(context['disposition_status'], context['subdisposition_status']):
                    raise osv.except_osv(('warning'),('Select Disposition And SubDisposition'))
                if context['disposition_status'] is 12:
                      raise osv.except_osv(('warning'),('Dialed data cannot have a  "New Lead" status')) 

                vvar=callend_information.browse(cr, uid, global_last_call_id, context)

                call_start =vvar['s_call_time']
                #raise osv.except_osv(('warning'),(datetime.datetime.now()))
                #call_start = call_start.replace(' ','')
                call_start = datetime.strptime(call_start, "%Y-%m-%d %H:%M:%S.%f")

                differ = datetime.now() - call_start

		#SUDIPTA
                #request_url = 'http://'+var_ip+'/dialer/play.php?leadid='+str(context['id'])+'&callid='+str(global_last_call_id)
		#callend_information.write(cr, uid, global_last_call_id, {'differ_time':differ,'s_endcall_time':datetime.now(),'s_disposition_id':context['disposition_status'],'s_subdisposition_id':context['subdisposition_status'],'record_url':request_url}, context=None)

                callend_information.write(cr, uid, global_last_call_id, {'differ_time':differ,'s_endcall_time':datetime.now(),'s_disposition_id':context['disposition_status'],'s_subdisposition_id':context['subdisposition_status']}, context=None)
                
		
		
		#search_dial_ids[] = obj.search(cr, uid, [('last_lead_id','=',last_lead)])   #--------
		#raise osv.except_osv(('warning'),(obj.search(cr, uid, [('last_lead_id','=',last_lead)])))
		obj.write(cr, uid, uid, {'last_lead_id':context['id']}) #----------
		self.write(cr, uid, context['id'], {'state': 'draft','gate':''})
		end_time = datetime.now()
                difference = (end_time-start_time)
                        
                self.pool.get('x_rb.performance.log').create(cr, uid,{'x_modle_name':'rb.crm.lead','x_time_start':str(start_time),'x_time_end':str(end_time),'x_difference':float(difference.microseconds),'x_view':'Call Hangup',}, context = context)
		
		return True
		




		


	









        def custom_export(self, cr, uid, ids, context=None):
                start_time = datetime.now()
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
                                    #raise osv.except_osv(('warning'),(r['last_lead_id']))
                                    if (last_lead_state and last_lead_state['state']=='Hangup'):
                                            raise osv.except_osv(('warning'),('Please Hangup Lead No:'+str(r['last_lead_id'])))
                            
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
                        last_id = save_information.create(cr, uid,{'name':str(var),'s_ip_address': var_ip,'s_agent_id':int(var),'s_user_name':int(uid),'s_lead_id':int(context['id']),'s_call_time':datetime.now(),'rela_lead':int(context['id']),'mobile':mobile}, context=None)
                        xmlvar = 'http://'+var_ip+'/'+var_callparam+'?xml=<request><security><username>'+var_uname+'</username><password>'+var_pswd+'</password></security><content><agent>'+var+'</agent><phoneNumber>'+mobile+'</phoneNumber><server>'+var_ip+'</server><leadId>'+str(context['id'])+'</leadId><callId>'+str(last_id)+'</callId></content></request>'
                        #raise osv.except_osv(('warning'),(xmlvar))
                        response=urllib2.urlopen(xmlvar)
                        #response.close()
                        #var_info = self.browse(cr, uid, ids, context=context)
                        #raise osv.except_osv(('warning'),(context['id']))
                        #present_lead_id = lead_id_information.browse(cr, uid, ids, context=context)
                        #raise osv.except_osv(('warning'),(present_lead_id.id))
                        #save_information = self.pool.get('crm.save.calldetails')
                        #raise osv.except_osv(('warning'),(context['id']))
                        
                        #raise osv.except_osv(('warning'),(global_var))
                        self.global_saveid = last_id
                        #raise osv.except_osv(('warning'),(last_id))
                        self.write(cr, uid, context['id'], {'state': 'Hangup','last_call_id':last_id,'disposition_status':False,'subdisposition_status':False,'gate':'all'})
                        obj.write(cr, uid, ids, {'last_lead_id':context['id']})
                        end_time = datetime.now()
                        difference = (end_time-start_time)
                        
                        self.pool.get('x_rb.performance.log').create(cr, uid,{'x_modle_name':'rb.crm.lead','x_time_start':str(start_time),'x_time_end':str(end_time),'x_difference':float(difference.microseconds),'x_view':'Call Connect',}, context = context)
		return True
						 
						 

        
		
	
	
	
	
	
	
	


	_name = "rb.crm.lead"

	_columns = {
				'name':fields.char("Subject", required=True),
                                'state': fields.char("State"),
				'contact_persion':fields.char("Contact Name"),
				'mobile':fields.char("Mobile"),
				'create_date' : fields.datetime('Date Created', readonly=True),
				'phone':fields.char("Phone"),
				'campaign_team':fields.many2one('rb.campaign.crm','Campaign',change_default=True,required=True),
				'sale_team_name':fields.many2one('rb.sales.team','Sales Team',change_default=True,domain="[('campaign_name_id','=',campaign_team)]",required=True),
				'quality_asur':fields.many2one('rb.qa.team', 'QA Group',domain="[('id','=',sale_team_name)]"),
				'team_lead':fields.many2one('rb.tl.team', 'TL Group',domain="[('id','=',sale_team_name)]"),
                                'sales_mngr':fields.many2one('rb.sm.team', 'PM Group',domain="[('id','=',sale_team_name)]"),
				'sales_admin':fields.many2one('rb.sa.team', 'SA Group',domain="[('id','=',sale_team_name)]"),
                                'quality_doc_group':fields.many2one('rb.doc.qa.team', 'QA Doc Group',domain="[('id','=',sale_team_name)]"),
				'financial_p_conlt':fields.many2one('rb.fpc.team','FPC DE Group',domain="[('id','=',sale_team_name)]"),
				'sales_team_r':fields.many2one('res.users','TSR',domain="[('sales_team','=',sale_team_name)]"),
				'disposition_status':fields.many2one('rb.crm.disposition','Disposition',change_default=True),
                 	'subdisposition_status':fields.many2one('rb.crm.sub.disposition','Sub Disposition Status',domain="[('disposition_status','=',disposition_status)]"),
				'batch_code':fields.many2one('rb.crm.batch.code','Batch Code',change_default=True),	
				'company_name':fields.char('Company Name'),
				'callback_date':fields.datetime('Callback Date'),
				'appo_date':fields.datetime('Appointment Date'),
				'birth_date':fields.date('Date Of Birth'),
				#'work_phone':fields.integer('Work Whone'),
				'home_phone':fields.char('Home Phone'),
				'age':fields.integer('Age'),
				'email_id':fields.char('Email'),
                                'gender':fields.selection([('male','Male'),('female','Female')],'Gender'),
				#'priority': fields.selection(AVAILABLE_PRIORITIES, 'Priority', select=True),
                                #'all_user':fields.function(_get_representative_areas, method=True, type="one2many", readonly=True, store=False,relation='res.users'),
                                #'allowed_ids': fields.function (_get_representative_areas, type="one2many", method=True, relation='res.users'),
                                #'which_user_id': fields.many2one("res.users", string="Selected User",domain="[('id','in',[x[1] for x in all_user])]"),
				'street': fields.char('Street'),
				'street2': fields.char('Street2'),
				'zip': fields.char('Zip', change_default=True),
				'city': fields.char('City'),
                                'city_id':fields.many2one('rb.city','City'),
				'state_id': fields.many2one("res.country.state", 'State'),
				'country_id': fields.many2one('res.country', 'Country'),
				'title': fields.many2one('res.partner.title', 'Title'),
				#'company_id': fields.many2one('res.company', 'Company', select=1),
				#'payment_mode': fields.many2one('crm.payment.mode', 'Payment Mode',domain="[('section_id','=',section_id)]"),
				'fpc_user': fields.many2one('res.users', 'FPC',domain="[('fpc_group','=',sale_team_name)]"),
				
				#For Personal Details
				
				'id_card_no':fields.char('ID Card No'),
				'last_call_id':fields.integer("Last Call ID"),
				'voter_id':fields.selection([('yes','Yes'),('no','No')],'Voter ID'),
				'passport_id':fields.selection([('yes','Yes'),('no','No')],'Passport'),
				'pan_no':fields.char('Pan No'),
				'residence_type':fields.selection([('owned','Owned'),('rented','Rented'),('employer','Employer'),('mortgagged','Mortgagged'),('parental','Parental')],'Residence Type'),
				'occupation':fields.selection([('primary','Primary'),('secondary','Secondary')],'Occupation'),
				'company_name':fields.char('Company Name'),
				'type_company':fields.selection([('govtment','Goverment'),('private','Private')],'Type of Company'),
				'designation':fields.char('Designation'),
				'employee_type':fields.selection([('blanked','Blanked'),('salaried','Salaried'),('self employed','Self Employed')],'Employment Type'),
				'taxable':fields.selection([('yes','Yes'),('no','No')],'Taxable'),
				'pay_slip':fields.selection([('yes','Yes'),('no','No')],'Pay Slip'),
				'marital_status':fields.selection([('married','Married'),('single','Single'),('separated','Separated'),('widowd','Widowd')],'Marital Status'),
				'degree':fields.char('Degree',readonly=True),
				'monthly_income':fields.float('Monthly Income'),
				'annual_income':fields.float('Annual Income'),
				'exprience':fields.char('Exprience',readonly=True),
				'no_of_family':fields.char('No Of Family Member'),
				'no_of_employeed':fields.char('No Of Employeed Member'),
				'no_of_child':fields.char('No Of Child'),
				'education_institution':fields.char('Education Institution',readonly=True),
				'billing_add':fields.char('Billing Address',readonly=True),
				'permanent_add':fields.char('Permanent Address'),
				'state_change':fields.char('State'),
				'dis_type':fields.char('State'),
				'description': fields.text('Notes'),
				'gate':fields.char('GATE'),
				#For client info
				'lead_source':fields.char('Lead Source'),
				'new_id_card_number':fields.char('New ID Card Number'),
				'insurance':fields.char('Insurance'),
				'expected_close_date':fields.date('Expected Close Date'),
				'status_f1':fields.char('Status F1'),
				'old_product_name':fields.char('Old Product Name'),
				'product_name':fields.char('Product Name'),
				'old_product_code':fields.char('Old Product Code'),
				'outstanding_amount':fields.char('Outstanding Amount'),
				'loan_amount':fields.char('Loan Amount'),
				'loan_turn':fields.char('Loan Turn'),
				'interest_amounts':fields.char('Interest Amounts'),
				'interes_rate':fields.char('Interes Rate'),
				'principal':fields.char('Principal'),
				'due_date':fields.date('Due Date'),
				'next_due_date':fields.date('Next Due Date'),
				'last_payment_date':fields.date('Last Payment Date'),
				'product_name_1':fields.char('Product Name 1'),
				'product_name_2':fields.char('Product Name 2'),
				'product_code_1':fields.char('Product Code 1'),
				'product_code_2':fields.char('Product Code 2'),
				'min_turn_1':fields.char('Min Turn 1'),
				'min_turn_2':fields.char('Min Turn 2'),
				'max_turn_1':fields.char('Max Turn 1'),
				'max_turn_2':fields.char('Max Turn 2'),
				'min_loan_amount_1':fields.char('Min Loan Amount 1'),
				'min_loan_amount_2':fields.char('Min Loan Amount 2'),
				'max_loan_amount_1':fields.char('Max Loan Amount 1'),
				'max_loan_amount_2':fields.char('Max Loan Amount 2'),
				'approved_payment_1':fields.char('Approved Payment 1'),
				'approved_payment_2':fields.char('Approved Payment 2'),
				'max_payment_1':fields.char('Max Payment 1'),
				'max_payment_2':fields.char('Max Payment 2'),
				'interest_rate_1':fields.char('Interest Rate 1'),
				'interest_rate_2':fields.char('Interest Rate 2'),
				'pos_name':fields.char('POS Name'),
				'cc_code':fields.char('CC Code'),
				'cc_name_':fields.char('CC Name '),
				'loan_amout_request':fields.char('Loan Amout Request'),
				'dsa_code':fields.char('DSA Code'),
				'dsa_name':fields.char('DSA Name'),
				'disb_channel':fields.char('DISB_Channel'),
				'no_agreement_id':fields.char('No. Agreement ID'),
				'date_of_closure':fields.char('Date of Closure'),
				'branch_code':fields.char('Branch Code'),
				'loan_term_request':fields.char('Loan Term Request'),
				'referee_1':fields.char('Referee_1'),
				'referee_2':fields.char('Referee_2'),
				'spouse_name':fields.char('Spouse Name'),
				'date_of_issue':fields.date('Date of Issue'),
				'place_of_issue':fields.char('Place of Issue'),
				'actual_address':fields.char('Actual Address'),
				'monthly_costs':fields.char('Monthly Costs'),
				'monthly_income_family':fields.char('Monthly Income Family'),
				'monthly_costs_family':fields.char('Monthly Costs Family'),
				'run_date':fields.date('RUN DATE'),
				'mob':fields.char('MOB'),
				'visit_no':fields.selection([('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8')],'No. of Visit'),
				'description_for_client': fields.char('Description'),
				'region': fields.char('Region'),
				'meeting_city': fields.char('Meeting City'),
				'related_phone_1': fields.char('Related Phone 1'),
				'related_phone_2': fields.char('Related Phone 2'),

                                'remarks':fields.char('Remarks'),
                                'relation2disposition':fields.one2many('rb.crm.disposition.history', 'related_lead', 'Disposition History'),
                                'relation2statechange':fields.one2many('rb.crm.stage.history', 'related_lead', 'Stage History'),
                                #Expected Revenue
                                'relation2product':fields.one2many('rb.crm.customer.product', 'related_lead', 'Expected Sale'),
                                #'product_name':fields.many2one('new.product.registration', 'Product Name'),
                                #'product_ammount':fields.float('Expected Ammount/Premium'),
                                #'product_term': fields.selection(returnyear,'Durartion In Year'),
                                'relation2savecall':fields.one2many('crm.save.calldetails', 'rela_lead', 'Call History'),## Data to show on xml <================================
                                ##Starting of oadoc tab

                                'select_cust_type':fields.selection([('1','Vietnamese'),('2','Foreigner')],'Type Of Customer'),
                                'nid':fields.boolean('National ID'),
                                'psprt':fields.boolean('Passport'),
                                'frb':fields.boolean('Family Registration Book'),
                                'rc':fields.boolean('Residence Card '),
                                'wp':fields.boolean('Work Permit'),
                                'hcl':fields.boolean('HR Confirmation Letter'),
                                'dlc':fields.boolean('Definite Labor Contract'),
                                'ilc':fields.boolean('Indefinite Labor Contract'),
                                'others': fields.text('Others'),
                                'frb':fields.boolean('Family Registration Book'),
                                'kt3':fields.boolean('KT3'),
                                'mrvb':fields.boolean('Most Recent Valid Bills'),
                                'mrvb_selection':fields.selection([('1','Electricity'),('2','Water'),('3','Mobile phone'),('4','Others')],'Type Of Bill'),
                                'mrvb_others':fields.text('Description Of Proof'),
                                'hod':fields.boolean('House Ownership Document'),
                                'omrbs':fields.boolean('Original Most Recent Bank Statement'),
                                'lcscra':fields.boolean('Labor  Contract Showing Current Residential Address'),
                                'mrrc':fields.boolean('Most recent Rental Contract'),
                                'sfbsscra':fields.boolean('Screenshot From Banking System Showing Current Residential Address'),
                                'otr':fields.text('Others'),
                                'select_income_type':fields.selection([('1','Salaried'),('2','Self Employed')],'Type Of Customer'),
                                'xobs':fields.boolean('Original Bank Statement'),
                                'xps':fields.boolean('Pay Slip'),
                                'xlc':fields.boolean('Labor Contract'),
                                'xes':fields.boolean('E-Statement'),
                                'xccl':fields.boolean('Company Confirmation Letter'),
                                'xnc':fields.boolean('Name Card'),
                                'xsc':fields.boolean('Staff Card'),
                                'xbrc':fields.boolean('Business Registration Certificate'),
                                'xafs':fields.boolean('Audited Financial Statement for the last financial year'),
                                'xlmti':fields.boolean('Latest 6 Months Tax Invoices'),
                                'xlmbs':fields.boolean('Latest 6 Months Bank Statements'),
                                'xothers':fields.text('Others'),
                                'ycpaaaof':fields.boolean('Citibank Product Application and Account Opening Form'),
                                'ydm':fields.text('Documents Missing'),
                                'yc':fields.text('Comments'),

                                #Lead scoring

                                'time_of_scoring': fields.float('Time of Scoring'),
                                'score_income': fields.float('Income'),
                                'score_age': fields.float('Age'),
                                'score_occupation': fields.float('Occupation'),
                                'score_interest_level': fields.float('Interest Level'),
                                'score_appoint_quality': fields.float('Appoint Quality'),
                                'score_product': fields.float('Product'),
                                'score_call_length': fields.float('Call Length'),
                                'score_income_range': fields.float('Income Range'),
                                'total': fields.function(_total_score, string = 'Total Score', type = 'float', store = True),
                                'result': fields.selection([('Pass', 'Pass'),('Fail', 'Fail')], 'Result'),
                                'score_note': fields.text('Resean For Fail'),


                                #Tale calling questions

                                'cstep_is_call_connected': fields.selection([('1', 'Yes'),('0', 'No')], 'Is the call connected'),
                                'cstep_speaking2name': fields.selection([('1', 'Yes'),('2', 'No')], 'Am I speaking to Mr/Mrs/Ms?'),
                                'cstep_know_your_name': fields.char('If No, May I know your name?', size = 128),
                                'cstep_telephone_number': fields.char('Shall we call back at the same number ? & which number should i call you back?', size = 32),
                                'cstep_precious_time': fields.selection([('1', 'Yes'),('0', 'No')], 'May i please take 5 minuits of your precious time to take you through the world of unlimited privileges?'),
                                'cstep_call_back_day': fields.datetime('If the answer is No, while you asked for time. Ask when can we call back.'),
                                'cstep_ask_appropriate_time_to_call': fields.text('Also ask for an appropriate time to call.'),
                                'eligibility_interested':fields.selection([('1', 'Yes'),('2', 'No')], 'I am sure you are interested in this product?'),
                                'eligibility_not_suitable':fields.selection([('1', 'Yes'),('2', 'No')], 'May i know why you feel this product is not suitable for you?'),
                                'eligibility_no_of_children':fields.selection([('1', 'Yes'),('2', 'No')], 'How many children do you have?'),
                                'eligibility_eligibility':fields.selection([('1', 'Yes'),('2', 'No')], 'ELIGIBLE?'),
                                'preeligibility_salaried':fields.selection([('1', 'Yes'),('0', 'No')], 'Are you salaried?'),
                                'preeligibility_degination':fields.char('What is your degination?'),
                                'preeligibility_few_qustion':fields.selection([('1', 'Yes'),('0', 'No')], 'May i ask you few qustions to choose the best product for your requirements?'),
                                'cstep_reason_rejection':fields.char('Please may i know the reason why you would not be interested in the special product being offered only to you'),
                                'cstep_ask2choose': fields.selection([('1', 'Yes'),('0', 'No')], 'May I call you back soon to explain this useful product?'),
                                'cstep_reason_not_proceeding': fields.selection([('Busy', 'Busy'),('Callback Late', 'Callback Late'),('Not Interested', 'Not Interested')], 'If No then reason for not proceeding further'),
                                'cstep_which_company': fields.char('Which company do you work for?', size = 128),
                                'cstep_is_married': fields.selection([('1', 'Yes'),('0', 'No')], 'Are You Married?'),
                                'cstep_income': fields.char('What is your gross Monthly income?', size = 128),
                                'cstep_location_stay': fields.char('Which location do stay in?', size = 128),
                                'cstep_date_of_birth': fields.date('May I have your date of birth?'),
                                'cstep_travel_flights': fields.char('How frequently do you travel through flights domestically or internationally?', size = 128),
                                'cstep_often_dine_out_someone': fields.char('How often do you dine out with friends and family?', size = 128),
                                'cstep_eligible': fields.selection([('1', 'Yes'),('0', 'No')], 'Ready to introduce product?'),
                                'cstep_is_schedule': fields.selection([('1', 'Yes'),('0', 'No')], ' May I fix a time for our sales representative to come and meet you for competing the documentation?'),
                                'cstep_call_back_date': fields.datetime('If No, the please note the reason of no appointment and also go to the call back page to record the call back date'),
                                'cstep_call_back_no_reason': fields.char('Reason for No'),
                                'cstep_address2visit': fields.char('Record address', size = 128),
                                'cstep_date_fix_appointment': fields.datetime('What Date should I fix the appointment and time?'),
                                'cstep_id_proof': fields.selection([('1', 'Yes'),('0', 'No')], 'May i ask acme additional questions that might help me strengthen your application and help me include some special offers for you?'),
                                'cstep_labour': fields.selection([('1', 'Yes'),('0', 'No')], 'Labour contract or business registration certificate?'),
                                'cstep_bank_account': fields.selection([('1', 'Yes'),('0', 'No')], 'Bank account statement'),
                                'cstep_pay_receipt': fields.selection([('1', 'Yes'),('0', 'No')], 'Pay Slip/Tax receipt'),
                                'cstep_family_registration': fields.selection([('1', 'Yes'),('0', 'No')], 'Family registration Book'),
                                'cstep_spouse_details': fields.selection([('1', 'Yes'),('0', 'No')], 'May I ask your spouse details?'),
                                'cstep_name_spouse': fields.char('Name of the spouse', size = 128),
                                'cstep_sure_have_friends': fields.selection([('1', 'Yes'),('0', 'No')], 'Do you have two friends to refer?'),
                                'cstep_friends': fields.text('Friend 1, Friend 2 and Friend 3'),
                                'cstep_contact_detail_friends': fields.text('Contact details of friends 1,2 and 3'),
                                'state_id': fields.many2one('res.country.state', 'Province', domain = "[('country_id','=',country_id)]"),
                                'channel':fields.selection([('telesales', 'Telesales'),('fsr', ' FSR'),('vfsr', ' VFSR')], 'Channel'),
                                'lead_id': fields.char('Lead ID', size = 30, readonly = True),
                                'opp_id': fields.char('Opportunity ID', size = 30, readonly = True),
                                'date_convert_opp': fields.datetime('Date Convert To Opportunity'),
                                'last_user_modify_lead': fields.many2one('res.users', 'Last User Modify Lead'),
                                'last_date_modify_lead': fields.datetime('Last Date Modify Lead'),
                                'last_user_modify_opp': fields.many2one('res.users', 'Last User Modify Opportunity'),
                                'last_date_modify_opp': fields.datetime('Last Date Modify Opportunity'),
                                'post_paid': fields.boolean('Post-Paid'),
                                'permanent_street': fields.char('Permanent Address', size = 128),
                                'permanent_phone': fields.char('Permanent Address Phone', size = 64),
                                'company_street': fields.char('Company Address', size = 128),
                                'apply_for': fields.selection([('Secured Card', 'Secured Card'),('CEO Test', 'CEO Test'),('Car Text', 'Car Text')], 'Apply For (If any)'),
                                'financial_status': fields.char('Financial Status', size = 128),
                                'time_travel_abroad': fields.text('How many times do you travel abroad a year?'),
                                'monthly_mobile_bill': fields.text('What is your monthly mobile bill (VND)?'),
                                'lead_referral': fields.one2many('rb.crm.lead.referral', 'opportunity_id', 'Referrals'),
                                'bank_account': fields.text('Bank Account'),
                                #one to many
                                'rela2customer_profiling' : fields.one2many('customer.profiling.form', 'rela_to_crm_lead', 'Customer Profiling'),
                                'submition_date': fields.date('Modyfied Date'),
                                'callback_state':fields.char('Call Back Status'),
                                'rela2callback_stages':fields.one2many('rb.crm.callback.stage', 'related_lead', 'Callback Summary'),
                                'rela2application':fields.one2many('rb.lead.application', 'related_lead', 'Application For VPB'),
                                'rela2citiapplication':fields.one2many('rb.lead.citi.application', 'related_lead', 'Application For CITI'),
                                'rela2fpcvisit':fields.one2many('rb.fpc.visit', 'related_lead', ''),
                                'lead_ref_stat' : fields.boolean('Lead reference status'), #************* ADD 5  *************
                                'tsr_change_flag' : fields.boolean('TSR Change Flag') #************* ADD 6  *************
                                
				
	}
	_order = "appo_date asc"
	#_defaults = {'state_change': 'tsr','state': 'draft','callback_state':'close','sales_team_r':_getTSR}

rb_crm_lead()

#######################################################################
class rb_crm_callback_stage(osv.osv):



        def relatedId(self,cr,uid,context=None):
                lead_id = context.get('id')
                
                return lead_id


        
        def submit_to(self, cr, uid, ids, context=None):
               
                
                obj_crm = self.pool.get('rb.crm.lead')
                obj_crm.write(cr, uid, context.get('id'), {'callback_state':'followup'})
                return {'type': 'ir.actions.act_window_close'}

        

        
        def _getUsersId(self,cr,uid,context=None):
                user_id =  uid
        
                return user_id

	_name = "rb.crm.callback.stage"
	_columns = {
			'callback_reason':fields.text("Call back Query:"),
			'feedback':fields.text('Feedback:'),
                        'callback_send_date':fields.date('Call Back date',readonly=True),
                        'send_user_name':fields.many2one('res.users',"Send By"),
                        'feedback_send_date':fields.date('Feedback Date',readonly=True),
                        'stage_id':fields.integer("Last Count"),
			'related_lead':fields.many2one('rb.crm.lead', 'Blank reference',select=False), ## Data <================================
			}
        _defaults = {'callback_send_date': fields.date.context_today,'send_user_name':_getUsersId,'related_lead':relatedId} 

rb_crm_callback_stage()
#######################################################################
class crm_save_calldetails(osv.osv):
        
    

	_name = "crm.save.calldetails"
	_columns = {
			'name':fields.char("Subject",required=True),
			's_ip_address':fields.char("Server Ip Address",size=64, required=True),
			's_agent_id':fields.integer("Agent ID", required=True),
			's_user_name':fields.integer("Agent Login ID", required=True),
			's_lead_id':fields.integer('Lead ID'),
			's_call_time': fields.datetime('Calling Time'),
			's_endcall_time': fields.datetime('Ending Time'),
                        's_disposition_id': fields.many2one('rb.crm.disposition',"Disposition ID"),
                        's_subdisposition_id': fields.many2one('rb.crm.sub.disposition',"Sub Disposition ID"),
						'rela_lead':fields.many2one('rb.crm.lead', 'Blank reference',select=False), ## Data <================================
						'differ_time':fields.char('Duration'),
						'mobile':fields.char('Mobile'),
                        'record_url':fields.char("Recording View"),
			}


crm_save_calldetails()
#######################################################################
class rb_crm_customer_product(osv.osv):

        def returnyear(self, cursor, user_id, context=None):
                lst=[]
                var_rainbow_commission = 0.00
                toup=()
                for k in range(1,50):
                        toup=(str(k),str(k))
                        lst.append(toup)
                return lst

	_name = "rb.crm.customer.product"
	_columns = {
                        'select_product': fields.many2one('new.product.registration',"Product Name",required=True),
			'product_ammount':fields.float('Expected Ammount/Premium',required=True),
                        'product_term': fields.selection(returnyear,'Durartion In Year',required=True),
			'related_lead':fields.many2one('rb.crm.lead', 'Blank reference',select=False), ## Data <================================
			}


rb_crm_customer_product()
#######################################################################
class rb_crm_stage_history(osv.osv):

        def _get_concat_val(self, cr, uid, ids, name, arg, context = None):
                res = { }
                for lead in self.browse(cr, uid, ids, context = context):
                        res[lead.id] = str(date(lead.create_date)) + lead.current_stage
                        #raise osv.except_osv(('warning'),( str(date(lead.create_date)) + lead.current_stage))
                return res
                
        

	_name = "rb.crm.stage.history"
	_columns = {
			'previous_stage':fields.char("Previous Stage"),
			'current_stage':fields.char('Current Stage'),
                        'create_date':fields.datetime('Convert Date',readonly=True),
                        'concatination_field':fields.char("Concat"),
			'related_lead':fields.many2one('rb.crm.lead', 'Blank reference',select=False), ## Data <================================
			}


rb_crm_stage_history()
#######################################################################
class rb_crm_disposition_history(osv.osv):

	_name = "rb.crm.disposition.history"
	_columns = {
			'name':fields.char("Subject",required=True),
			'user_name':fields.many2one('res.users',"Edited By"),
                        'disposition_code': fields.many2one('rb.crm.disposition',"Disposition Code"),
                        'subdisposition_code': fields.many2one('rb.crm.sub.disposition',"Sub Disposition Code"),
                        'remarks':fields.char("Remarks"),
                        'state_change':fields.char("State"),
                        'submition_date': fields.date('Submission Date'),
			'related_lead':fields.many2one('rb.crm.lead', 'Blank reference',select=False), ## Data <================================
			}


rb_crm_disposition_history()
#######################################################################



class rb_customer_sale(osv.osv):

	_name = "rb.customer.sale"
	_columns = {
                        'name':fields.char("Name",size=64, required=True),
                        'details':fields.many2one('rb.crm.lead','Customer Details'),
                        'customer_id':fields.char("Customer Ref ID",size=64, required=True)
			}
rb_customer_sale()	
########################################################################
class product_catagories(osv.osv):

    _name = "product.catagories"
    _columns = {
            'name': fields.char("Category",size=64, required=True),
            'product_description': fields.text("Product Description", required=True),
            'filter_for_yn_1': fields.selection([('1','Yes'),('2','No')],'Available Approved/Login',required=True),
            'filter_for_yn_2': fields.selection([('1','Yes'),('2','No')],'Available Disburst',required=True)

            }

product_catagories()

########################################################################
class new_product_registration(osv.osv):

    _name = "new.product.registration"

    

    _columns = {

                    'name' : fields.char("Product Name",required=True),
                    'product_type' : fields.many2one('product.catagories','Select Product Type',required=True),
                    'product_fixorperse' : fields.selection([('1','Percentage'),('2','Fixed')],'Type of Profit'),
                    'product_persamt' : fields.float("Rainbow Commission",digits=(12,2)),
                    'product_taxable' : fields.selection([('1','Yes'),('2','No')],'Product Taxable'),
                    'product_service_tax' : fields.float("Service tax in %",digits=(12,2)),
                    'product_notes' : fields.text("Product Description")
                    
                    
                    
                    


        }
    _defaults = {'product_persamt': 0.000,'product_service_tax': 0.000}
    
new_product_registration()
########################################################################

class customer_registration(osv.osv):

    _name = "customer.registration"
    _columns = {
            'name': fields.char("Customer Name",size=64, required=True),
            'customer_description': fields.text("Customer Description")

            }
customer_registration()
########################################################################
class rb_crm_lead_referral(osv.osv):

    _name = "rb.crm.lead.referral"
    _columns = {
            'name': fields.char("Customer Name",size=64, required=True),
            'customer_description': fields.text("Customer Description"),
            'mobile_no':fields.char("Mobile No:",size=64, required=True),
            'email_id':fields.char("Email Id:",size=64, required=True),
            'address':fields.text("Address"),
            'opportunity_id':fields.many2one('rb.crm.lead', 'Blank reference',select=False)

            }
rb_crm_lead_referral()


##########################        Customer Profiling Form          ##############################################

class customer_profiling_form(osv.osv):

        _name = "customer.profiling.form"

        _columns = {
                'name' : fields.char('Subject'),
                'first' : fields.char('First'),
                'middle' : fields.char('Middle'),
                'surname' : fields.char('Surname'),
                'salutation' : fields.char('Salutation'),
                'gender' : fields.selection([('Male','Male'),('Female','Female')],'Gender'),
                'status' : fields.char('Status'),
                'children' : fields.integer("Children"),
                'type' : fields.char('Type'),
                'nid' : fields.char('NID'),
                'company' : fields.char('Company'),
                'shortname' : fields.char('Short Name'),
                'busregn' : fields.char('Bus Regn'),
                'type2' : fields.char('Type'),
                'location' : fields.char('Location'),
                'designation' : fields.char('Designation'),
                'mobile' : fields.char('Mobile'),
                'spousename' : fields.char('Spouse Name'),
                'spouce_mobile' : fields.char('Mobile'),
                'addr1' : fields.char('Addr1'),
                'addr1ext' : fields.char(''),
                'addr2' : fields.char('Addr 2'),
                'addr2ext' : fields.char(''),
                'ward' : fields.char('Ward'),
                'district' : fields.char('District'),
                'wardext' : fields.char('Ward'),
                'districtext' : fields.char('District'),
                'city' : fields.char('City'),
                'addr_phone' : fields.char('Phone'),
                'extn' : fields.char('Extn'),
                'cityext' : fields.char('City'),
                'addr_phoneext' : fields.char('Phone'),
                'email' : fields.char('Email'),
                'emailext' : fields.char('Email'),
                'grossincomepa' : fields.float("Gross Income p.a.",digits=(12,2)),
                'variableincome' : fields.float('Variable Income',digits=(12,2)),
                'otherincome' : fields.float('Other Income',digits=(12,2)),
                'otherincome_1' : fields.float('',digits=(12,2)),
                'otherincome_2' : fields.float('',digits=(12,2)),
                'otherincome_3' : fields.float('',digits=(12,2)),
                'monthlyexpense' : fields.float('Monthly Expense',digits=(12,2)),
                'houseasset' : fields.float('House'),
                'scooterasset' : fields.float('Two Wheeler'),
                'carasset' : fields.float('Car'),
                'investedasset' : fields.float('Investment'),
                'equityasset' : fields.float('Equity'),
                'inslife' : fields.float('Life Insurance'),
                'inscar' : fields.float('Car Insurance'),
                'instw' : fields.float('TW'),
                'inshealth' : fields.float('Health'),
                'insproperty' : fields.float('Property'),
                'relations2cpd' : fields.one2many('customer.profiling.dependents', 'dep_ref2cst_prof_form', 'Dependents'),
                'relations2ref' : fields.one2many('customer.profiling.reference', 'ref_ref2cst_prof_form', 'Reference'),
                'othr_bank' : fields.char('Bank'),
                'othr_cr_card' : fields.char('Creditcard Details'),
                'othr_home' : fields.char('Home Loan'),
                'othr_loan' : fields.char('Other Loan'),
                'othr_auto' : fields.char('Auto'),
                'othr_personal' : fields.char('Personal'),
                'othr_shopping' : fields.char('Shopping'),
                'othr_local' : fields.char('Local'),
                'othr_fav_rest' : fields.char('Favorite Restaurant'),
                'othr_travel1' : fields.char('Domestic'),
                'othr_travel2' : fields.char('Overseas'),
                'rela_to_crm_lead' : fields.many2one('rb.crm.lead','Reference'),
                'data':fields.binary('File',filters='*.csv')
                }
customer_profiling_form()
###################################################################################################################

class customer_profiling_dependents(osv.osv):

        _name = "customer.profiling.dependents"

        _columns = {
                'name' : fields.char('Name'),
                'relation' : fields.char('Relation'),
                'gender' : fields.selection([('Male','Male'),('Female','Female')],'Gender'),
                'age' : fields.float('Age'),
                'dep_ref2cst_prof_form' : fields.many2one('customer.profiling.form','Reference',invisible=True)

                }
customer_profiling_dependents()

###################################################################################################################

class customer_profiling_reference(osv.osv):

        _name = "customer.profiling.reference"

        _columns = {
                'name' : fields.char('Name'),
                'type' : fields.char('Relation'),
                'mobile' : fields.integer('mobile'),
                'ref_ref2cst_prof_form' : fields.many2one('customer.profiling.form','Reference',invisible=True)

                }
customer_profiling_reference()
###################################################################################################################

class user_issue_post(osv.osv):

        _name = "user.issue.post"

        _columns = {
                'name' : fields.char('Subject'),
                'user_name' : fields.char('Relation'),
                'user_id' : fields.many2one('res.users','User'),
                'ref2issu' : fields.one2many('user.issue.post.list', 'rel_issue', 'Dependents'),
                'state' : fields.char('Status'),
                'description' : fields.text('Description'),
                'type':fields.char('Type')
                }
user_issue_post()
###################################################################################################################
class user_issue_post_list(osv.osv):

        _name = "user.issue.post.list"

        _columns = {
                'issue' : fields.text('Issue'),
                'user_name' : fields.char('Relation'),
                'user_id' : fields.many2one('res.users','User'),
                'rel_issue' : fields.many2one('user.issue.post','Issue'),

                }
user_issue_post_list()
###################################################################################################################
class rb_crm_sa_approve(osv.osv):


        def application_upload(self, cr, uid, ids, context=None):
                #raise osv.except_osv(('warning'),( context['id']))
                submition_date = date.today().strftime('%Y-%m-%d')
                rb_application = self.pool.get('rb.lead.application')
                rb_lead = self.pool.get('rb.crm.lead')
                record = self.pool.get('rb.crm.sa.approve').browse(cr, uid, context['id'], context)
                if (platform.system()=='Windows'):
                            file_path = 'E:/application_lead.csv'
                else:
                            file_path = '/opt/openerp/application_lead.csv'

                bdata = record.data
                f = open(file_path,'wb')
                f.write(bdata.decode('base64'))
                f.flush()
                f.close
                t_Rows = (len(list(csv.reader(open(file_path)))))-1
                with open(file_path, 'rb') as fd:
                        row_pointer = 0
                        reader = csv.reader(fd)
                        for row in csv.reader(fd):
                            if (row_pointer>0):
                                    
                                    product_code = 0
                                    insurance = 0
                                    personal_income = 0.0
                                    loan_term_request = 0
                                    loan_term_approve = 0
                                    loan_not_insurance = 0.0
                                    approve_amount = 0.0
                                    monthly_payment = 0.0
                                    age = 0
                                    len_of = len(row[5]) - row[5].index(' ')
                                    last_date_csv = row[5]          
                                    last_date_r = last_date_csv[:-len_of]

                                    date_of_app_creation_r = row[8]
                                    date_of_disbursal_r =  row[18]

                                    len_of = len(row[19]) - row[19].index(' ')
                                    last_date_csv = row[19] 
                                    lsm_stating_date_r = last_date_csv[:-len_of] 

                                    len_of = len(row[35]) - row[35].index(' ')
                                    last_date_csv = row[35]
                                    time_finish_r = last_date_csv[:-len_of]

                                    _logger.error(last_date_r+'_______'+row[8]+'_______'+row[18]+'___'+lsm_stating_date_r+'__'+time_finish_r)
                                    
                                    chars = '/'
                                    positions_last_date = [m.start() for m in re.finditer("|".join(map(re.escape, chars)), last_date_r)]
                                    _logger.error(positions_last_date)
                                    positions_date_of_app_creation = [m.start() for m in re.finditer("|".join(map(re.escape, chars)), date_of_app_creation_r)]
                                    _logger.error(positions_date_of_app_creation)
                                    positions_date_of_disbursal = [m.start() for m in re.finditer("|".join(map(re.escape, chars)), date_of_disbursal_r)]
                                    _logger.error(positions_date_of_disbursal)
                                    positions_lsm_stating_date = [m.start() for m in re.finditer("|".join(map(re.escape, chars)), lsm_stating_date_r)]
                                    _logger.error(positions_lsm_stating_date)
                                    positions_time_finish = [m.start() for m in re.finditer("|".join(map(re.escape, chars)), time_finish_r)]
                                    _logger.error(positions_time_finish)
                                    _logger.error(time_finish_r[6:-6]+'_______'+time_finish_r[:-14]+'_______'+time_finish_r[3:-11])


				    time_finish = time_finish_r[positions_time_finish[1]+1:] + '-' + time_finish_r[0:positions_time_finish[0]] + '-' + time_finish_r[positions_time_finish[0]+1:-(positions_time_finish[1]+1)] 
                                    last_date = last_date_r[positions_last_date[1]+1:] + '-' + last_date_r[0:positions_last_date[0]] + '-' + last_date_r[positions_last_date[0]+1:-(positions_last_date[1]+1)] 
                                    date_of_app_creation =  date_of_app_creation_r[positions_date_of_app_creation[1]+1:] + '-' + date_of_app_creation_r[0:positions_date_of_app_creation[0]] + '-' + date_of_app_creation_r[positions_date_of_app_creation[0]+1:-(positions_date_of_app_creation[1]+1)] 
                                    date_of_disbursal = date_of_disbursal_r[positions_date_of_disbursal[1]+1:] + '-' + date_of_disbursal_r[0:positions_date_of_disbursal[0]] + '-' + date_of_disbursal_r[positions_date_of_disbursal[0]+1:-(positions_date_of_disbursal[1]+1)] 
                                    lsm_stating_date = lsm_stating_date_r[positions_lsm_stating_date[1]+1:] + '-' + lsm_stating_date_r[0:positions_lsm_stating_date[0]] + '-' + lsm_stating_date_r[positions_lsm_stating_date[0]+1:-(positions_lsm_stating_date[1]+1)] 


                                    _logger.error(str(time_finish)+'_______'+str(last_date)+'_______'+str(date_of_app_creation)+'_______'+str(date_of_disbursal)+'_______'+str(lsm_stating_date))
                                                                
                                    #raise osv.except_osv(('warning'),(datetime.strptime(last_date,'%Y-%m-%d'),datetime.strptime(time_finish,'%Y-%m-%d'),datetime.strptime(date_of_app_creation,'%Y-%m-%d'),datetime.strptime(date_of_disbursal,'%Y-%m-%d'),datetime.strptime(lsm_stating_date,'%Y-%m-%d')))
                                    if not row[2]:
                                            product_code = 0
                                    else:
                                            product_code = int(row[2])
                                    if not row[4]:
                                            insurance = 0
                                    else:
                                            insurance = int(row[4])
                                    if not row[12]:
                                            personal_income = 0.0
                                    else:
                                            personal_income = float(row[12])
                                    if not row[13]:
                                            loan_term_request = 0
                                    else:
                                            loan_term_request = int(row[13])    
                                    if not row[14]:
                                            loan_term_approve = 0
                                    else:
                                            loan_term_approve = int(row[14])
                                    if not row[15]:
                                            loan_not_insurance = 0
                                    else:
                                            loan_rb_lead_applicationnot_insurance = float(row[15])
                                    if not row[16]:
                                            approve_amount = 0.0
                                    else:
                                            approve_amount = float(row[16])
                                    if not row[17]:
                                            monthly_payment = 0
                                    else:
                                            monthly_payment = float(row[17])
                                    if not row[23]:
                                            age = 0
                                    else:
                                            age = int(row[23])         
                                    application_search = rb_lead.search(cr, uid, [('id_card_no','=',row[24])])
                                    #raise osv.except_osv(('warning'),( application_search))
                                    if len(application_search) > 0:
                                            
                                            rb_application.create(cr, uid,{'application_id':row[0],'contact_number':row[1],'product_code':product_code,'request_amount':row[3],'insurance':insurance,'last_date':last_date,'last_status':row[6],'chanel':row[7],'date_of_app_creation':date_of_app_creation,'product_name':row[9],'cc_code':row[10],'cc_name':row[11],'personal_income':personal_income,'loan_term_request':loan_term_request,'loan_term_approve':loan_term_approve,'loan_not_insurance':loan_not_insurance,'approve_amount':approve_amount,'monthly_payment':monthly_payment,'date_of_disbursal':date_of_disbursal,'lsm_start_date':lsm_stating_date,'ft_account':row[20],'client_name':row[21],'gender':row[22],'age':age,'id_no':row[24],'mobile_phone':row[25],'home_phone':row[26],'official_phone':row[27],'actual_dist':row[28],'actual_city':row[29],'reg_dist':row[30],'reg_city':row[31],'reason_needaddinfo_qde':row[32],'code_cancle':row[33],'comment_cancle':row[34],'time_finish':time_finish,'tsa_code':row[36],'tsa_name':row[37],'dsa_code':row[38],'dsa_name':row[39],'related_lead':application_search[0]}, context = context)
                                    #raise osv.except_osv(('warning'),( disposition_search[0],sub_disposition_search[0]))
                            row_pointer = row_pointer + 1
                self.write(cr, uid,context['id'], {'modify_date':submition_date}, context = context)

        def sa_bulk_dispo_update(self, cr, uid, ids, context=None):
                #raise osv.except_osv(('warning'),( context['id']))
                submition_date = date.today().strftime('%Y-%m-%d')
                obj_disposition = self.pool.get('rb.crm.disposition')
                obj_sub_disposition = self.pool.get('rb.crm.sub.disposition')
                obj_dispo_history = self.pool.get('rb.crm.disposition.history')
                crm_lead = self.pool.get('rb.crm.lead')
                disposition_name = 'null'
                sub_disposition_name = 'null'
                record = self.pool.get('rb.crm.sa.approve').browse(cr, uid, context['id'], context)
                if (platform.system()=='Windows'):
                            file_path = 'E:/sa_update.csv'
                else:
                            file_path = '/opt/openerp/tmp_lead.csv'

                bdata = record.data
                f = open(file_path,'wb')
                f.write(bdata.decode('base64'))
                f.flush()
                f.close
                t_Rows = (len(list(csv.reader(open(file_path)))))-1
                with open(file_path, 'rb') as fd:
                        row_pointer = 0
                        reader = csv.reader(fd)
                        for row in csv.reader(fd):
                            if (row_pointer>0):
                                           
                                    #raise osv.except_osv(('warning'),( row[0],row[1],row[2],row[3]))
                                    disposition_search = obj_disposition.search(cr, uid, [('name','=',row[1])])
                                    sub_disposition_search = obj_sub_disposition.search(cr, uid, [('name','=',row[2]),('disposition_status','=',int(disposition_search[0]))])
                                    crm_lead.write(cr, uid, int(row[0]), {'disposition_status':disposition_search[0],'subdisposition_status':sub_disposition_search[0],'app_id':row[3],'submition_date':submition_date}, context = context)
                                    obj_dispo_history.create(cr, uid,{'name':row[0],'user_name':uid,'disposition_code':disposition_search[0],'subdisposition_code':sub_disposition_search[0],'related_lead':int(row[0]),'submition_date':submition_date}, context = context)
                                    #raise osv.except_osv(('warning'),( disposition_search[0],sub_disposition_search[0]))
                            row_pointer = row_pointer + 1
                self.write(cr, uid,context['id'], {'modify_date':submition_date}, context = context)           

        _name = "rb.crm.sa.approve"

        _columns = {
                'description' : fields.text('Description'),
                'no_of_lead_modify' : fields.char('No Of Lead'),
                'modify_date' : fields.date('Modify Date'),
                'upload_date' : fields.date('Upload Date'),
                'data':fields.binary('File',filters='*.csv'),

                }
        _defaults = {'upload_date': fields.date.context_today}
rb_crm_sa_approve()
###################################################################################################################
class rb_lead_application(osv.osv):

        _name = "rb.lead.application"

        _columns = {
                'application_id' : fields.integer('Application Id'),
                'contact_number' : fields.char('Contact Number'),
                'product_code' : fields.integer('Product Code'),
                'request_amount' : fields.char('REQUEST AMOUNT'),
                'insurance' : fields.integer('INSURANCE'),
                'last_date' : fields.date('LAST DATE'),
                'chanel' : fields.char('CHANEL'),
                'last_status' : fields.char('LAST STATUS'),
                'date_of_app_creation' : fields.date('DATE OF APP CREATION'),
                'product_name' : fields.char('PRODUCT NAME'),
                'cc_name' : fields.char('CC NAME'),
                'cc_code' : fields.char('CC CODE'),
                'personal_income' : fields.float('PERSONAL INCOME'),
                'loan_term_approve' : fields.integer('LOAN TERM APPROVE'),
                'loan_term_request' : fields.integer('LOAN TERM REQUEST'),
                'loan_not_insurance' : fields.float('LOANAMOUNT NOT INSURANCE'),
                'approve_amount' : fields.float('APPROVEAMOUNT'),
                'monthly_payment' : fields.float('MONTHLY PAYMENT'),
                'date_of_disbursal' : fields.date('DATE OF DISBURSAL'),
                'lsm_stating_date' : fields.date('LSM STARTING DATE'),
                'ft_account' : fields.char('FT ACCOUNT'),
                'client_name' : fields.char('CLIENT NAME'),
                'gender' : fields.char('GENDER'),
                'age' : fields.integer('AGE'),
                'id_no' : fields.char('ID NO'),
                'mobile_phone' : fields.char('MOBILE PHONE'),
                'home_phone' : fields.char('Home Phone'),
                'official_phone' : fields.char('OFFICE PHONE'),
                'actual_dist' : fields.char('ACTUAL DIST'),
                'actual_city' : fields.char('ACTUAL CITY'),
                'reg_dist' : fields.char('REG DIST'),
                'reg_city' : fields.char('REG CITY'),
                'reason_needaddinfo_qde' : fields.char('REASON NEEDADDINFO QDE'),
                'code_cancle' : fields.char('CODE CANCEL'),
                'comment_cancle' : fields.text('COMMENT_CANCEL'),
                'time_finish' : fields.date('TIME FINISH'),
                'tsa_code' : fields.char('TSA CODE'),
                'tsa_name' : fields.char('TSA NAME'),
                'dsa_code' : fields.char('DSA CODE'),
                'dsa_name' : fields.char('DSA NAME'),
                'related_lead':fields.many2one('rb.crm.lead', 'Blank reference',select=False), ## Data <================================
                }
rb_lead_application()
###################################################################################################################
class rb_fpc_visit(osv.osv):


        def create(self, cr, uid, values, context=None):
                    #raise osv.except_osv(('warning'),(values))
                    #values.update({'disposition_status':values['disposition_status']})
                    #values.update({'subdisposition_status':values['subdisposition_status']})
                    #raise osv.except_osv(('warning'),('Create'))
                    #val = {'disposition_status':values['disposition_status'],'subdisposition_status':values['subdisposition_status']}
                    obj_rb_crm_lead = self.pool.get('rb.crm.lead')
                    #obj_rb_crm_lead.write(cr, uid, int(values['related_lead']), {'disposition_status':int(values['disposition_status']),'subdisposition_status':int(values['subdisposition_status'])})
                    new_id = super(rb_fpc_visit, self).create(cr, uid, values, context)
                    
                    return new_id

        _name = "rb.fpc.visit"

        _columns = {
                'name' : fields.char('Contact Number'),
                'visit_date' : fields.datetime('Visit Date'),
                'visit_location':fields.char('Visit Location'),
                'description':fields.text('Description'),
                'disposition_status':fields.many2one('rb.crm.disposition','Disposition',change_default=True),
                'subdisposition_status':fields.many2one('rb.crm.sub.disposition','Sub Dosposition Status',domain="[('disposition_status','=',disposition_status)]"),
                'next_date':fields.datetime('Next action Date'),
                'next_action':fields.char('Next Action'),
                'related_lead':fields.many2one('rb.crm.lead', 'Blank reference',select=False), ## Data <================================
                }
rb_lead_application()



class lead_referral_log(osv.osv):
	_name = "lead.referral.log"
	_columns = {
							'ref_lead_id':fields.many2one('rb.crm.lead','Lead relation'),
							'ref_sales_team': fields.many2one('rb.sales.team','Sales team'),
							'ref_tl_group':fields.many2one('rb.tl.team','Tl Group'),
							'ref_by' : fields.many2one('res.users','Referred by'),


					}
lead_referral_log()

class lead_referral_tsr_log(osv.osv):
	_name = "lead.referral.tsr.log"
	_columns = {
							'ref_lead_id':fields.many2one('rb.crm.lead','Lead relation'),
							'ref_campaign':fields.many2one('rb.campaign.crm','Campaign'),
							'ref_tsr':fields.many2one('res.users','Tsr'),
							'ref_by': fields.many2one('res.users','Referred by'),

					}
lead_referral_tsr_log()




#================================================  Delinquency ================================================ Delinquency ================================================


class rb_crm_delinquency_disposition(osv.osv):
        _name = 'rb.crm.delinquency.disposition'
        _description = 'Disposition'
        _columns = {
				'name': fields.char('Disposition Name', size=64,help='Name of Disposition', required=True, translate=True),
				'short_code':fields.char('Short Code', size=64, required=True),
				'dis_type':fields.selection([('tsr','TSR'),('qa','QA'),('tl','TL'),('sa','SA'),('fpc','FPC'),('qa doc','QA Doc'),('all','All')],string='Type')
               }
	_sql_constraints = [('name_uniq', 'unique (name)','must be unique !'),('code_uniq', 'unique (short_code)','must be unique !')]
	_order='name'
rb_crm_delinquency_disposition()


class rb_crm_delinquency_sub_disposition(osv.osv):
        #_description="Sub Disposition"
        _name = 'rb.crm.delinquency.sub.disposition'
        _columns = {
				'disposition_status': fields.many2one('rb.crm.delinquency.disposition', 'Disposition',required=True),
				'name': fields.char('Sub Disposition Name', size=64, required=True),
				'short_code':fields.char('Short Code', size=64, required=True),
				'rank':fields.integer("Rank",size=64,required=True),
				'description':fields.char("Description"),
				'forwardable':fields.boolean("Forward able")
			}		
rb_crm_delinquency_sub_disposition()

class rb_crm_delinquency_disposition_history(osv.osv):

	_name = "rb.crm.delinquency.disposition.history"
	_columns = {
			'name':fields.char("Subject",required=True),
			'user_name':fields.many2one('res.users',"Edited By"),
                        'disposition_code': fields.many2one('rb.crm.delinquency.disposition',"Disposition Code"),
                        'subdisposition_code': fields.many2one('rb.crm.delinquency.sub.disposition',"Sub Disposition Code"),
                        'remarks':fields.char("Remarks"),
                        'state_change':fields.char("State"),
                        'submition_date': fields.date('Submission Date'),
			'related_lead':fields.many2one('rb.crm.delinquency.lead', 'Blank reference',select=False), ## Data <================================
			}


rb_crm_delinquency_disposition_history()

class rb_crm_delinquency_stage_history(osv.osv):

        def _get_concat_val(self, cr, uid, ids, name, arg, context = None):
                res = { }
                for lead in self.browse(cr, uid, ids, context = context):
                        res[lead.id] = str(date(lead.create_date)) + lead.current_stage
                        #raise osv.except_osv(('warning'),( str(date(lead.create_date)) + lead.current_stage))
                return res
                
        

	_name = "rb.crm.delinquency.stage.history"
	_columns = {
			'previous_stage':fields.char("Previous Stage"),
			'current_stage':fields.char('Current Stage'),
                        'create_date':fields.datetime('Convert Date',readonly=True),
                        'concatination_field':fields.char("Concat"),
			'related_lead':fields.many2one('rb.crm.delinquency.lead', 'Blank reference',select=False), ## Data <================================
			}


rb_crm_delinquency_stage_history()

class crm_delinquency_save_calldetails(osv.osv):
        
    

	_name = "crm.delinquency.save.calldetails"
	_columns = {
			'name':fields.char("Subject",required=True),
			's_ip_address':fields.char("Server Ip Address",size=64, required=True),
			's_agent_id':fields.integer("Agent ID", required=True),
			's_user_name':fields.integer("Agent Login ID", required=True),
			's_lead_id':fields.integer('Lead ID'),
			's_call_time': fields.datetime('Calling Time'),
			's_endcall_time': fields.datetime('Ending Time'),
                        's_disposition_id': fields.many2one('rb.crm.delinquency.disposition',"Disposition ID"),
                        's_subdisposition_id': fields.many2one('rb.crm.delinquency.sub.disposition',"Sub Disposition ID"),
						'rela_lead':fields.many2one('rb.crm.delinquency.lead', 'Blank reference',select=False), ## Data <================================
						'differ_time':fields.char('Duration'),
						'mobile':fields.char('Mobile'),
                        'record_url':fields.char("Recording View"),
			}


crm_delinquency_save_calldetails()

class rb_crm_delinquency_callback_stage(osv.osv):



        def relatedId(self,cr,uid,context=None):
                lead_id = context.get('id')
                
                return lead_id


        
        def submit_to(self, cr, uid, ids, context=None):
               
                
                obj_crm = self.pool.get('rb.crm.delinquency.lead')
                obj_crm.write(cr, uid, context.get('id'), {'callback_state':'followup'})
                return {'type': 'ir.actions.act_window_close'}

        

        
        def _getUsersId(self,cr,uid,context=None):
                user_id =  uid
        
                return user_id

	_name = "rb.crm.delinquency.callback.stage"
	_columns = {
			'callback_reason':fields.text("Call back Query:"),
			'feedback':fields.text('Feedback:'),
                        'callback_send_date':fields.date('Call Back date',readonly=True),
                        'send_user_name':fields.many2one('res.users',"Send By"),
                        'feedback_send_date':fields.date('Feedback Date',readonly=True),
                        'stage_id':fields.integer("Last Count"),
			'related_lead':fields.many2one('rb.crm.delinquency.lead', 'Blank reference',select=False), ## Data <================================
			}
        _defaults = {'callback_send_date': fields.date.context_today,'send_user_name':_getUsersId,'related_lead':relatedId} 

rb_crm_delinquency_callback_stage()





class rb_crm_delinquency_lead(osv.osv):


        check_group = 0

        ###################################################################################################################

        def get_subdisposition(self,cr,uid,dispo_id,context=None):
                lst_of_subdispo_pair = []
                obj_subdisposition = self.pool.get('rb.crm.delinquency.sub.disposition')
                ids_sub_disposition = obj_subdisposition.search(cr, uid, [])
                rs_sub_disposition = obj_subdisposition.read(cr, uid, ids_sub_disposition, ['name','id','disposition_status'], context)
                for each in rs_sub_disposition:
                        if(dispo_id == each['disposition_status'][0]):
                                sdname = each['name']
                                sdid = each['id']
                                pair_sub_dispo = "("+str(sdname)+","+str(sdid)+")"
                                lst_of_subdispo_pair.append(pair_sub_dispo)
                _logger.error(str(dispo_id)+'List Of Disposition'+str(lst_of_subdispo_pair))
                return lst_of_subdispo_pair

        #####################################################################################################################
        
        def convert_to_qa(self, cr, uid, ctxval, context=None):
                obj_dispo_history = self.pool.get('rb.crm.delinquency.disposition.history')
                state_change_date = datetime.now().strftime('%Y-%m-%d 00:00:00')
                disposition = ctxval['disposition_status']
                subdisposition = ctxval['subdisposition_status']
                lead_id = ctxval['id']
                state = ctxval['state_change']
                obj_dispo = self.pool.get('rb.crm.delinquency.disposition')
                obj_state_change_history = self.pool.get('rb.crm.delinquency.stage.history')
		ids_dispo = obj_dispo.search(cr, uid, [('id','=',disposition)])
                obj_dispo_read = obj_dispo.read(cr, uid, ids_dispo, ['dis_type','id'], context)
                for dispo_stat in obj_dispo_read:
                        #raise osv.except_osv(('warning'),(dispo_stat['dis_type'])) 
                        if dispo_stat['dis_type'] not in state:
                                #self.write(cr, uid, ids, {'disposition_status':False,'subdisposition_status':False})
                                return 'Please Select Correct Disposition'              
                obj_subdisposition = self.pool.get('rb.crm.delinquency.sub.disposition')
                
                subDisposition_search = obj_subdisposition.search(cr, uid, [('id','=',subdisposition)])
                obj_subdisposition_read = obj_subdisposition.read(cr, uid, subDisposition_search, ['forwardable','name'], context)
                #raise osv.except_osv(('warning'),(submition_date))
                for subdispo_stat in obj_subdisposition_read:
                        if subdispo_stat['forwardable'] is False:
                                return "Please Choose Correct Disposition For Forwarding"
                _logger.error('Total convert_to_qa--->>>'+str(ctxval))
                ctxval['state_change'] = 'qa'
                self.write(cr, uid, ctxval['id'],ctxval)
                obj_dispo_history.create(cr, uid,{'name':str(lead_id),'user_name':uid,'disposition_code':disposition,'subdisposition_code':subdisposition,'related_lead':lead_id,'submition_date':state_change_date}, context = context)
		obj_state_change_history.create(cr, uid,{'related_lead':lead_id,'previous_stage':state,'current_stage':'qa','concatination_field':str(state_change_date)+'qa'}, context = context)
		return 'ok'

        
        ###################################################################################################################
                                                                                                                                                                                
        ###################################################################################################################
        def  get_disposition(self,cr,uid,context=None):                             
                ids_disposition = []
                lst_of_dispo_pair = [] ##consist dictionary of disposition based on state change
                obj_disposition =  self.pool.get('rb.crm.delinquency.disposition')
                ids_disposition = obj_disposition.search(cr, uid, ['|',('dis_type','=','tsr'),('dis_type','=','all')]) ##Dynamic key here
                rs_disposition = obj_disposition.read(cr, uid, ids_disposition, ['name','id'], context)
                for drs in rs_disposition:
                        dsname = drs['name']
                        dsid = drs['id']
                        pair_dispo = "("+str(dsname)+","+str(dsid)+")"
                        lst_of_dispo_pair.append(pair_dispo)
                return lst_of_dispo_pair
                         
        #####################################################################################################################

        
        #######################################################################################




	
		

        #######################################################################################

	#######################################################################################
        def get_last_lead(self, cr, uid, ids, context=None):
                obj = self.pool.get('res.users')
                ids = obj.search(cr, uid, [('id','=',uid)])
                res = obj.read(cr, uid, ids, ['last_lead_id','dial_state'], context)
                #return res['last_lead_id']
                
	##########################################################################################

        def search(self, cr, user, args, offset=0, limit=None, order=None, context=None, count=False, xtra=None):
                #raise osv.except_osv(('warning'),(args))
                if (args and len(args)>0 and str(args[0]) == "['state', '=', 'today']"):
                        args=[]
                        newStartPeriod=datetime.today()
                        newStartPeriod = newStartPeriod.replace(hour=0) #i wanted everything today, not just from this minute
                        newStartPeriod = newStartPeriod.replace(minute=0) #if you want you can remove these and you
                        newStartPeriod = newStartPeriod.replace(second=0) #will just get stuff after this second
                        _logger.error('Todays Date-------'+str(newStartPeriod))
                        args = [('date_convert_opp', '>=', newStartPeriod.strftime('%Y-%m-%d %H:%M:%S'))] 
                        ret = super(rb_crm_delinquency_lead,self).search(cr, user, args, offset, limit, order, context, count)
                        
                elif (args and len(args)>0 and str(args[0]) == "['state', '=', 'notcontact']"):
                        args=[]
                        ret=[]
                        ret2=[]
                        connectList=[]
                        obj_sub_dispo_history = self.pool.get('rb.crm.delinquency.disposition.history')
                        newStartPeriod=datetime.today()
                        newStartPeriod = newStartPeriod.replace(hour=0) #i wanted everything today, not just from this minute
                        newStartPeriod = newStartPeriod.replace(minute=0) #if you want you can remove these and you
                        newStartPeriod = newStartPeriod.replace(second=0) #will just get stuff after this second
                        _logger.error('Todays Date-------'+str(newStartPeriod))
                        ids = obj_sub_dispo_history.search(cr, user,[('create_date', '>=', newStartPeriod.strftime('%Y-%m-%d %H:%M:%S'))])
                        _logger.error('Todays Date-------'+str(ids))
                        disposition_read = obj_sub_dispo_history.read(cr, user, ids, ['disposition_code','related_lead'], context)
                        _logger.error('Tupale-------'+str(disposition_read))
                                
                        for dispo in disposition_read:
                                get_dispo_code = dispo.get('disposition_code')
                                _logger.error('Disposition ********'+str(get_dispo_code[0]))
                                if(get_dispo_code[0]==2):
                                        get_lead_id = dispo.get('related_lead')
                                        _logger.error('Lead Id'+str(get_lead_id[0]))
                                        args = [('id', '=', get_lead_id[0])]
                                else:
                                        get_lead_id = dispo.get('related_lead')
                                        connectList = [get_lead_id[0]] + connectList
                                        args = [('id', '=', 0)]
                                
                                ret1 = super(rb_crm_delinquency_lead,self).search(cr, user, args, offset, limit, order, context, count)
                                ret = ret + ret1
                        ret = list(set(ret))
                        connectList = list(set(connectList))
                        
                        _logger.error('After Sorting-------'+str(connectList))
                        _logger.error('After Sorting-------'+str(ret))
                        
                elif (args and len(args)>0 and str(args[0]) == "['state', '=', 'contact']"):
                       
                        args=[]
                        ret=[]
                        obj_sub_dispo_history = self.pool.get('rb.crm.delinquency.disposition.history')
                        newStartPeriod=datetime.today()
                        newStartPeriod = newStartPeriod.replace(hour=0) #i wanted everything today, not just from this minute
                        newStartPeriod = newStartPeriod.replace(minute=0) #if you want you can remove these and you
                        newStartPeriod = newStartPeriod.replace(second=0) #will just get stuff after this second
                        _logger.error('Todays Date-------'+str(newStartPeriod))
                        ids = obj_sub_dispo_history.search(cr, user,[('create_date', '>=', newStartPeriod.strftime('%Y-%m-%d %H:%M:%S'))])
                        _logger.error('Todays Date-------'+str(ids))
                        disposition_read = obj_sub_dispo_history.read(cr, user, ids, ['disposition_code','related_lead'], context)
                        _logger.error('Disposition-------'+str(disposition_read))
                        for dispo in disposition_read:
                                get_dispo_code = dispo.get('disposition_code')
                                _logger.error('Disposition ********'+str(get_dispo_code[0]))
                                if(get_dispo_code[0]!=2):
                                        get_lead_id = dispo.get('related_lead')
                                        _logger.error('Lead Id'+str(get_lead_id[0]))
                                        args = [('id', '=', get_lead_id[0])]
                                else:
                                        args = [('id', '=', 0)]
                                ret1 = super(rb_crm_delinquency_lead,self).search(cr, user, args, offset, limit, order, context, count)
                                ret = ret + ret1
                        ret = list(set(ret))
                        _logger.error('After Sorting-------'+str(ret))

                elif (args and len(args)>0 and str(args[0]) == "['state', '=', 'yesterday']"):
                        args=[]
                        newStartPeriod=datetime.today() - timedelta(hours=24)
                        #raise osv.except_osv(('warning'),(newStartPeriod))
                        newStartPeriod = newStartPeriod.replace(hour=0) #i wanted everything today, not just from this minute
                        newStartPeriod = newStartPeriod.replace(minute=0) #if you want you can remove these and you
                        newStartPeriod = newStartPeriod.replace(second=0) #will just get stuff after this second
                        _logger.error('Todays Date-------'+str(newStartPeriod))
                        todaysDate=datetime.today()
                        #raise osv.except_osv(('warning'),(newStartPeriod))
                        todaysDate = todaysDate.replace(hour=0) #i wanted everything today, not just from this minute
                        todaysDate = todaysDate.replace(minute=0) #if you want you can remove these and you
                        todaysDate = todaysDate.replace(second=0) #will just get stuff after this second
                        args = [('relation2statechange.concatination_field', '=', newStartPeriod.strftime('%Y-%m-%d %H:%M:%S')+'fpc')]  
                        ret = super(rb_crm_delinquency_lead,self).search(cr, user, args, offset, limit, order, context, count)
                        
                elif (args and len(args)>0 and str(args[0]) == "['state', '=', 'mtd']"):
                        obj_stage_history = self.pool.get('rb.crm.delinquency.stage.history')
                        args=[]
                        ret=[]
                        today = date.today()
                        currentYear = today.year + 1
                        currentMonth = today.month
                        currentDay = 1
                        currentPeriod = date(today.year, today.month,currentDay)
                        #raise osv.except_osv(('warning'),(currentPeriod))
                        newStartPeriod=datetime.today()
                        newStartPeriod = newStartPeriod.replace(hour=0) #i wanted everything today, not just from this minute
                        newStartPeriod = newStartPeriod.replace(minute=0) #if you want you can remove these and you
                        newStartPeriod = newStartPeriod.replace(second=0) #will just get stuff after this second
                        day_diffrence = (today-currentPeriod).days
                        args = ['&',('date_convert_opp', '>=', currentPeriod.strftime('%Y-%m-%d %H:%M:%S')),('state_change','!=','Reject')] 
                        ret = super(rb_crm_delinquency_lead,self).search(cr, user, args, offset, limit, order, context, count)







                elif (args and len(args)>0 and str(args[0]) == "['state', '=', 'notcontactyesterday']"):
                       
                        args=[]
                        ret=[]
                        obj_sub_dispo_history = self.pool.get('rb.crm.delinquency.disposition.history')
                        newStartPeriod=datetime.today() -  timedelta(hours=24)
                        newStartPeriod = newStartPeriod.replace(hour=0) #i wanted everything today, not just from this minute
                        newStartPeriod = newStartPeriod.replace(minute=0) #if you want you can remove these and you
                        newStartPeriod = newStartPeriod.replace(second=0) #will just get stuff after this second
                        today=datetime.today()
                        today = today.replace(hour=0) #i wanted everything today, not just from this minute
                        today = today.replace(minute=0) #if you want you can remove these and you
                        today = today.replace(second=0) #will just get stuff after this second
                        _logger.error('Todays Date-------'+str(newStartPeriod))
                        ids = obj_sub_dispo_history.search(cr, user,['&',('create_date', '>=', newStartPeriod.strftime('%Y-%m-%d %H:%M:%S')),('create_date', '<', today.strftime('%Y-%m-%d %H:%M:%S'))])
                        _logger.error('Todays Date-------'+str(ids))
                        disposition_read = obj_sub_dispo_history.read(cr, user, ids, ['disposition_code','related_lead'], context)
                        _logger.error('Disposition-------'+str(disposition_read))
                        for dispo in disposition_read:
                                get_dispo_code = dispo.get('disposition_code')
                                _logger.error('Disposition ********'+str(get_dispo_code[0]))
                                if(get_dispo_code[0]==2):
                                        get_lead_id = dispo.get('related_lead')
                                        _logger.error('Lead Id'+str(get_lead_id[0]))
                                        args = [('id', '=', get_lead_id[0])]
                                else:
                                        args = [('id', '=', 0)]
                                ret1 = super(rb_crm_delinquency_lead,self).search(cr, user, args, offset, limit, order, context, count)
                                ret = ret + ret1
                        ret = list(set(ret))
                        _logger.error('After Sorting-------'+str(ret))

                elif (args and len(args)>0 and str(args[0]) == "['state', '=', 'contactyesterday']"):
                       
                        args=[]
                        ret=[]
                        obj_sub_dispo_history = self.pool.get('rb.crm.delinquency.disposition.history')
                        newStartPeriod=datetime.today() -  timedelta(hours=24)
                        newStartPeriod = newStartPeriod.replace(hour=0) #i wanted everything today, not just from this minute
                        newStartPeriod = newStartPeriod.replace(minute=0) #if you want you can remove these and you
                        newStartPeriod = newStartPeriod.replace(second=0) #will just get stuff after this second
                        today=datetime.today()
                        today = today.replace(hour=0) #i wanted everything today, not just from this minute
                        today = today.replace(minute=0) #if you want you can remove these and you
                        today = today.replace(second=0) #will just get stuff after this second
                        _logger.error('Todays Date-------'+str(newStartPeriod))
                        ids = obj_sub_dispo_history.search(cr, user,['&',('create_date', '>=', newStartPeriod.strftime('%Y-%m-%d %H:%M:%S')),('create_date', '<', today.strftime('%Y-%m-%d %H:%M:%S'))])
                        _logger.error('Todays Date-------'+str(ids))
                        disposition_read = obj_sub_dispo_history.read(cr, user, ids, ['disposition_code','related_lead'], context)
                        _logger.error('Disposition-------'+str(disposition_read))
                        for dispo in disposition_read:
                                get_dispo_code = dispo.get('disposition_code')
                                _logger.error('Disposition ********'+str(get_dispo_code[0]))
                                if(get_dispo_code[0]!=2):
                                        get_lead_id = dispo.get('related_lead')
                                        _logger.error('Lead Id'+str(get_lead_id[0]))
                                        args = [('id', '=', get_lead_id[0])]
                                else:
                                        args = [('id', '=', 0)]
                                ret1 = super(rb_crm_delinquency_lead,self).search(cr, user, args, offset, limit, order, context, count)
                                ret = ret + ret1
                        ret = list(set(ret))
                        _logger.error('After Sorting-------'+str(ret))

                else:
                        ret = super(rb_crm_delinquency_lead,self).search(cr, user, args, offset, limit, order, context, count)
                return ret
                

        def write(self, cr, uid, ids, values, context = None):
                #raise osv.except_osv(('warning'),(ids))
                var_for_wiz_1 = self.browse(cr, uid, ids, context=context) #@%@%@%
		#raise osv.except_osv(('warning'),(var_for_wiz_1['tsr_change_flag']))
                get_group_name = 'null'
                get_all_grp = []
                current_grp = 0
                prev_grp = 0
                var_status = 'null'
                res = False
                lead_id = 0
                dispo_id = 0
                remarks = ' '
                get_disposition_status = ''
                submition_date = date.today().strftime('%Y-%m-%d')
                obj_dispo_history = self.pool.get('rb.crm.delinquency.disposition.history')
                obj_disposition = self.pool.get('rb.crm.delinquency.disposition')
                if 'sales_team_r' in values:
                        if var_for_wiz_1['tsr_change_flag'] !=True: #********** Tweak Here ***** 7
                                raise osv.except_osv(('warning'),('You have no permission to change TSR'))
                if 'state_change' in values:
                        res = super(rb_crm_delinquency_lead,self).write(cr, uid, ids, values, context = context)
                        return res
                elif ('rela2fpcvisit' in values):
                        size = len(values['rela2fpcvisit']) - 1
                        get_disposition = values['rela2fpcvisit'][size][2]
                        res = super(rb_crm_delinquency_lead,self).write(cr, uid, ids, {'submition_date':submition_date,'disposition_status':get_disposition['disposition_status'],'subdisposition_status':get_disposition['subdisposition_status']}, context = context)
                        #res = super(rb_crm_delinquency_lead,self).write(cr, uid, ids,{'submition_date':submition_date}, context = context)
                        if 'remarks' in values:
                                remarks = values['remarks']
                        #_logger.error('State Stae-------'+var_status)
                        #raise osv.except_osv(('warning'),(ids))        
                        obj_dispo_history.create(cr, uid,{'name':str(lead_id),'user_name':uid,'disposition_code':get_disposition['disposition_status'],'subdisposition_code':get_disposition['subdisposition_status'],'related_lead':ids[0],'submition_date':submition_date,'remarks':remarks}, context = context)
                        #raise osv.except_osv(('warning'),(get_disposition['disposition_status']))
                        
                elif ('state' not in values) and ('callback_state' not in values):
                        
                        #raise osv.except_osv(('warning'),(values))
                        cr.execute('select gid from res_groups_users_rel where uid=%s',(uid,))
                        group_id = cr.fetchall()
                        for all_grp in group_id:
                                cr.execute('select name from res_groups where id=%s',(all_grp,))
                                group_name = cr.fetchone()[0]
                                if group_name == 'TSR' or group_name == 'QA' or group_name == 'FPC DE' or group_name == 'QA Doc' or group_name == 'SA' or group_name == 'TL' or group_name == 'FPC Users':
                                        rs_approve = self.read(cr, uid,ids, ['state_change','id','disposition_status'], context)
                                        #false_lst = [] #** MOD FOR WIZARD
                                        #false_lst.extend(rs_approve) #** MOD FOR WIZARD
					#raise osv.except_osv(('warning'),(rs_approve))
                                        if ("<type 'dict'>" in str(type(rs_approve))): #************* ADD 1  *************
                                                tmp_rs_approve =  rs_approve #************* ADD 2  *************
                                                rs_approve = [] #************* ADD 3
                                                rs_approve.append(tmp_rs_approve) #************* ADD 4  *************
					#raise osv.except_osv(('warning'),(rs_approve))
                                        for var in rs_approve:
                                                
                                                var_status= var['state_change']
                                                _logger.error('State Stae'+var_status)
						#gate_status =  var['gate']
                                                lead_id = var['id']
                                                if var['disposition_status']:
                                                        dispo_id = var['disposition_status'][0]
                                                if 'disposition_status' in values :        
                                                        dispo_stat_read =  obj_disposition.read(cr, uid,values['disposition_status'], ['dis_type'], context)
                                                        get_disposition_status = dispo_stat_read['dis_type']
                                                        if (values['disposition_status']==35 and var_status=='tsr'):
                                                                raise osv.except_osv(('Warning!'),("Please select Proper Disposition This disposition is only for Follow Up Stage"))
                                                        #for dispo in dispo_stat_read:
                                                        #raise osv.except_osv(('Warning!'),( get_disposition_status)) 
                                                                #get_disposition_status = str(dispo['dis_type'])
                                                         
                                                if (group_name == 'TSR' and var_status=='tsr') or (group_name == 'TSR' and var_status=='customer') or (group_name == 'TSR' and var_status=='qa') or (group_name == 'TSR' and var_status=='fpc') or (group_name == 'TSR' and var_status=='qa doc') or (group_name == 'TSR' and var_status=='sa') or (group_name == 'TSR' and var_status=='Reject'):
                                                        #raise osv.except_osv(('Warning!'),(dispo_id,get_group_name,var_status)) 
                                                        #res = super(rb_crm_delinquency_lead,self).write(cr, uid, ids, values, context = context)
                                                        current_grp = 1
                                                        if 'disposition_status' in values : 
                                                                if (get_disposition_status != 'tsr' and group_name == 'TSR') and (get_disposition_status != 'all' and group_name == 'TSR'):     
                                                                        raise osv.except_osv(('Warning!'),("Please Select Correct Disposition"))
                                                elif group_name == 'QA' and var_status=='qa':
                                                        #res = super(rb_crm_delinquency_lead,self).write(cr, uid, ids, values, context = context)
                                                        current_grp = 1
                                                        
                                                        if 'disposition_status' in values :
                                                                #raise osv.except_osv(('Warning!'),(get_disposition_status))
                                                                if (get_disposition_status != 'qa' and group_name == 'QA'):       
                                                                        raise osv.except_osv(('Warning!'),("Please Select Correct Disposition"))
                                                elif (group_name == 'FPC DE' and (var_status=='fpc' or var_status=='sa' or var_status=='qa doc')) or (group_name == 'FPC Users' and var_status=='fpc')  :
                                                        #res = super(rb_crm_delinquency_lead,self).write(cr, uid, ids, values, context = context)
                                                        current_grp = 1
                                                        if 'disposition_status' in values : 
                                                                if (get_disposition_status != 'fpc' and group_name == 'FPC DE'):
                                                                        raise osv.except_osv(('Warning!'),("Please Select Correct Disposition"))
                                                elif (group_name == 'QA Doc' and var_status=='qa doc'):
                                                        #res = super(rb_crm_delinquency_lead,self).write(cr, uid, ids, values, context = context)
                                                        current_grp = 1
                                                        if 'disposition_status' in values : 
                                                                if (get_disposition_status != 'qa doc' and group_name == 'QA Doc'):
                                                                        raise osv.except_osv(('Warning!'),("Please Select Correct Disposition"))
                                                elif (group_name == 'SA' and var_status=='sa'):
                                                        #res = super(rb_crm_delinquency_lead,self).write(cr, uid, ids, values, context = context)
                                                        current_grp = 1
                                                        if 'disposition_status' in values : 
                                                                if (get_disposition_status != 'sa' and group_name == 'SA'):
                                                                        raise osv.except_osv(('Warning!'),("Please Select Correct Disposition"))
                        if current_grp == 1:
                                if 'disposition_status' in values or 'subdisposition_status' in values:
                                                                res_write = super(rb_crm_delinquency_lead,self).write(cr, uid, ids, values, context = context)
                                                                res = super(rb_crm_delinquency_lead,self).write(cr, uid, ids,{'submition_date':submition_date}, context = context)
                                                                if 'disposition_status' in values:
                                                                        dispo_id = values['disposition_status']
                                                                if 'remarks' in values:
                                                                        remarks = values['remarks']
                                                                _logger.error('State Stae-------'+var_status)
                                                                obj_dispo_history.create(cr, uid,{'name':str(lead_id),'user_name':uid,'disposition_code':dispo_id,'subdisposition_code':values['subdisposition_status'],'related_lead':lead_id,'submition_date':submition_date,'remarks':remarks}, context = context)
                                                                return res
                        else:
                                raise osv.except_osv(('Warning!'),("Yo don't have permission to change or modify"))
                
                #raise osv.except_osv(('Warning!'),(values))
                res = super(rb_crm_delinquency_lead,self).write(cr, uid, ids, values, context = context)
                return res
                        
                                                

        def calculate_age(self,cr,uid,ids,field,context=None):
                #raise osv.except_osv(('warning'),(field)) 2014-03-17
                year, month, day = [int(x) for x in str(field).split("-")]
                born = date(year, month, day)
                
                today = date.today()
                try: 
                        birthday = born.replace(year=today.year)
                except ValueError:
                        birthday = born.replace(year=today.year, day=born.day-1)
                if birthday > today:
                        val = {'age':today.year - born.year - 1}
                else:
                        val = {'age':today.year - born.year}
                return {'value': val}

        def create(self, cr, uid, values, context=None):
                    state_change_date = datetime.now().strftime('%Y-%m-%d 00:00:00')
                    new_id = super(rb_crm_delinquency_lead, self).create(cr, uid, values, context)
                    #self.write(cr, uid, int(new_id), {'date_convert_opp':state_change_date,'remarks':'Direct Lead'})
                    #raise osv.except_osv(('Warning!'),(values))
                    if ('state_change' in values and values['state_change'] == 'fpc'):
                            obj_state_change_history = self.pool.get('rb.crm.delinquency.stage.history')
                            submition_date = date.today().strftime('%Y-%m-%d')
                            obj_dispo_history = self.pool.get('rb.crm.delinquency.disposition.history')
                            obj_dispo_history.create(cr, uid,{'name':str(new_id),'user_name':uid,'disposition_code':3,'subdisposition_code':13,'related_lead':new_id,'submition_date':submition_date,'remarks':'Direct Lead'}, context = context)
                            obj_dispo_history.create(cr, uid,{'name':str(new_id),'user_name':uid,'disposition_code':6,'subdisposition_code':28,'related_lead':new_id,'submition_date':submition_date,'remarks':'Direct Lead'}, context = context)
                            obj_dispo_history.create(cr, uid,{'name':str(new_id),'user_name':uid,'disposition_code':values['disposition_status'],'subdisposition_code':values['subdisposition_status'],'related_lead':new_id,'submition_date':submition_date,'remarks':'Direct Lead'}, context = context)
                            obj_state_change_history.create(cr, uid,{'related_lead':new_id,'previous_stage':'tsr','current_stage':'qa','concatination_field':str(state_change_date)+'qa'}, context = context)
                            obj_state_change_history.create(cr, uid,{'related_lead':new_id,'previous_stage':'qa','current_stage':'fpc','concatination_field':str(state_change_date)+'fpc'}, context = context)
                    return new_id



        def default_get(self, cr, uid, fields, context=None):
                    check_flag = 0
                    obj_grp = self.pool.get('res.groups')
                    data = super(rb_crm_delinquency_lead, self).default_get(cr, uid, fields, context=context)
                    if uid == 1:
                        data['state_change']='tsr'
                        data['state']='draft'
                        data['callback_state']='close'
                        return data
                        
                    grp_search = obj_grp.search(cr, uid, [('users','=',uid)])
                    grp_read = obj_grp.read(cr, uid, grp_search, ['name'], context)
                    for grp in grp_read:
                                grp_name = grp['name']
                                if grp_name == 'FPC DE' or grp_name == 'TL' or grp_name=='FPC Users':
                                        check_flag = 1
                                if grp_name == 'QA Doc':
                                        check_flag = 2
                    
                     
                    if check_flag == 1:
                            data['state_change']='fpc'
                            data['sales_team_r']=False
                            data['date_convert_opp'] = datetime.now().strftime('%Y-%m-%d 00:00:00')
                            #data['remarks'] = 'Direct Lead'
                            obj_sales_team = self.pool.get('rb.sales.team')
                            team_search = obj_sales_team.search(cr, uid, [('financial_conlt_group.fpc_team','=',uid)])
                            team_read = obj_sales_team.read(cr, uid, team_search, ['name','id'], context)
                            #data['sale_team_name']=team_read
                            if grp_name=='FPC Users':
                                    data['fpc_user']=uid
                    elif check_flag == 2:
                            data['state_change']='qa doc'
                            data['sales_team_r']=False
                            data['date_convert_opp'] = datetime.now().strftime('%Y-%m-%d 00:00:00')
                    else:
                            data['state_change']='tsr'
                            data['sales_team_r']=uid
                    data['state']='draft'
                    data['callback_state']='close'
                    
                    return data

        def callback_tsr(self,cr,uid,ids,context=None):
                lead_state = 'null'
                check_flag = 0
                obj_grp = self.pool.get('res.groups')
                grp_search = obj_grp.search(cr, uid, [('users','=',uid)])
                rs_state = self.read(cr, uid,ids, ['state_change'], context)
                for state in rs_state:
                        lead_state = state['state_change']
                grp_read = obj_grp.read(cr, uid, grp_search, ['name'], context)
                for grp in grp_read:
                        grp_name = grp['name']
                        if grp_name == 'QA' and lead_state=='qa':
                                check_flag=1
                        elif (grp_name == 'SA' and lead_state=='sa') or (grp_name == 'SA' and lead_state=='customer'):
                                check_flag=1
                        elif grp_name == 'FPC DE' and lead_state=='fpc':
                                check_flag=1
                        elif grp_name == 'QA Doc' and lead_state=='qa doc':
                                check_flag=1        
                if check_flag == 0:
                        raise osv.except_osv(('warning'),('Please Select Only Your State lead'))
                        
                return {
                        'name':"Call Back Reason",
                        'view_mode': 'form',
                        'view_type': 'tree,form',
                        'res_model': 'rb.crm.callback.stage',
                        'type': 'ir.actions.act_window',
                        'nodestroy': True,
                        'target': 'new',
			'context': context.update({'send_user_id': uid,'id':id})
                        }


        def feedback_send(self,cr,uid,ids,context=None):
                #obj_stages = self.pool.get('rb.crm.callback.stage')
                self.write(cr, uid, ids, {'callback_state':'close'})
                return True



 





        def disposition_onchange(self,cr,uid,ids,context=None):
                var_subdisposition = False
                val = {'subdisposition_status':var_subdisposition,'remarks':False}

                return {'value': val}



        def fun_disposition(self,cr,uid,ids,dispo_stat,state_change,gate,context=None):
                val = {'remarks':False}                                
		return {'value': val}
        


        def returnyear(self, cursor, user_id, context=None):
                lst=[]
                var_rainbow_commission = 0.00
                toup=()
                for k in range(1,50):
                        toup=(str(k),str(k))
                        lst.append(toup)
                return lst

        

                
	def onchange_getage_qa(self,cr,uid,ids,team_id,context=None):
		var_qa = 'null'
		var_tl = 'null'
		var_sa = 'null'
		var_sm = 'null'
		obj = self.pool.get('res.users')
		obj_team = self.pool.get('rb.sales.team')
		ids = obj_team.search(cr, uid, [('id','=',team_id)])
		
		res = obj_team.read(cr, uid, ids, ['quality_asur_group','sales_mgr_group','team_lead_group','sales_admin_group','financial_conlt_group','quality_doc_group','id'], context)
		
		for r in res:

					var_qa = r['quality_asur_group']
					var_tl = r['team_lead_group']
					var_sa = r['sales_admin_group']
					var_fpc = r['financial_conlt_group']
					var_qa_doc = r['quality_doc_group']
					var_sm = r['sales_mgr_group']
					#raise osv.except_osv(('warning'),(r['sales_mgr_group']))
		val = {
            'quality_asur':var_qa,
			'sales_admin':var_sa,
			'team_lead':var_tl,
			'financial_p_conlt':var_fpc,
			'quality_doc_group':var_qa_doc,
                        'sales_mngr':var_sm    
        }
		return {'value': val}
		
		
	def approved_func(self,cr,uid,ids,context=None):
                state_change_date = datetime.now().strftime('%Y-%m-%d 00:00:00')
                disposition = context['disposition_status']
                subdisposition = context['subdisposition_status']
                state = context['state_change']
                obj_dispo = self.pool.get('rb.crm.delinquency.disposition')
                #raise osv.except_osv(('warning'),(dispo_stat)) 
		ids_dispo = obj_dispo.search(cr, uid, [('id','=',disposition)])
                obj_dispo_read = obj_dispo.read(cr, uid, ids_dispo, ['dis_type','id'], context)
                for dispo_stat in obj_dispo_read:
                        #raise osv.except_osv(('warning'),(dispo_stat['dis_type'])) 
                        if dispo_stat['dis_type'] not in state:
                                #self.write(cr, uid, ids, {'disposition_status':False,'subdisposition_status':False})
                                raise osv.except_osv(('warning'),('Please Select Correct Disposition'))
                obj_subdisposition = self.pool.get('rb.crm.delinquency.sub.disposition')
                subDisposition_search = obj_subdisposition.search(cr, uid, [('id','=',subdisposition)])
                obj_subdisposition_read = obj_subdisposition.read(cr, uid, subDisposition_search, ['forwardable','name'], context)
                for subdispo_stat in obj_subdisposition_read:
                        if subdispo_stat['forwardable'] is False:
                                raise osv.except_osv(('warning'),("Please Choose Correct Disposition For Forwarding"))    
		self.write(cr, uid, context['id'], {'state_change': 'fpc','date_convert_opp':state_change_date})
		obj_state_change_history = self.pool.get('rb.crm.delinquency.stage.history')
                obj_state_change_history.create(cr, uid,{'related_lead':context['id'],'previous_stage':state,'current_stage':'fpc','concatination_field':str(state_change_date)+'fpc'}, context = context)
		return True


	def send_back_func(self,cr,uid,ids,context=None):
                state_change_date = datetime.now().strftime('%Y-%m-%d 00:00:00')
                disposition = context['disposition_status']
                subdisposition = context['subdisposition_status']
                state = context['state_change']
                obj_dispo = self.pool.get('rb.crm.delinquency.disposition')
                #raise osv.except_osv(('warning'),(dispo_stat)) 
		ids_dispo = obj_dispo.search(cr, uid, [('id','=',disposition)])
                obj_dispo_read = obj_dispo.read(cr, uid, ids_dispo, ['dis_type','id'], context)
                for dispo_stat in obj_dispo_read:
                        #raise osv.except_osv(('warning'),(dispo_stat['dis_type'])) 
                        if dispo_stat['dis_type'] not in state:
                                #self.write(cr, uid, ids, {'disposition_status':False,'subdisposition_status':False})
                                raise osv.except_osv(('warning'),('Please Select Correct Disposition'))
                obj_subdisposition = self.pool.get('rb.crm.delinquency.sub.disposition')
                subDisposition_search = obj_subdisposition.search(cr, uid, [('id','=',subdisposition)])
                obj_subdisposition_read = obj_subdisposition.read(cr, uid, subDisposition_search, ['forwardable','name'], context)
                for subdispo_stat in obj_subdisposition_read:
                        if subdispo_stat['forwardable'] :
                                raise osv.except_osv(('warning'),("Please Choose Correct Disposition For Forwarding")) 
		self.write(cr, uid, context['id'], {'state_change': 'tsr'})
		obj_state_change_history = self.pool.get('rb.crm.delinquency.stage.history')
                obj_state_change_history.create(cr, uid,{'related_lead':context['id'],'previous_stage':state,'current_stage':'tsr','concatination_field':str(state_change_date)+'tsr'}, context = context)
		return True


        def send_back_QADoc(self,cr,uid,ids,context=None):
                state_change_date = datetime.now().strftime('%Y-%m-%d 00:00:00')
                disposition = context['disposition_status']
                subdisposition = context['subdisposition_status']
                state = context['state_change']
                obj_dispo = self.pool.get('rb.crm.delinquency.disposition')
                #raise osv.except_osv(('warning'),(dispo_stat)) 
		ids_dispo = obj_dispo.search(cr, uid, [('id','=',disposition)])
                obj_dispo_read = obj_dispo.read(cr, uid, ids_dispo, ['dis_type','id'], context)
                for dispo_stat in obj_dispo_read:
                        #raise osv.except_osv(('warning'),(dispo_stat['dis_type'])) 
                        if dispo_stat['dis_type'] not in state:
                                #self.write(cr, uid, ids, {'disposition_status':False,'subdisposition_status':False})
                                raise osv.except_osv(('warning'),('Please Select Correct Disposition'))
                obj_subdisposition = self.pool.get('rb.crm.delinquency.sub.disposition')
                subDisposition_search = obj_subdisposition.search(cr, uid, [('id','=',subdisposition)])
                obj_subdisposition_read = obj_subdisposition.read(cr, uid, subDisposition_search, ['forwardable','name'], context)
                for subdispo_stat in obj_subdisposition_read:
                        if subdispo_stat['forwardable'] :
                                raise osv.except_osv(('warning'),("Please Choose Correct Disposition For Forwarding")) 
		self.write(cr, uid, context['id'], {'state_change': 'fpc'})
		obj_state_change_history = self.pool.get('rb.crm.delinquency.stage.history')
                obj_state_change_history.create(cr, uid,{'related_lead':context['id'],'previous_stage':state,'current_stage':'fpc','concatination_field':str(state_change_date)+'fpc'}, context = context)
		return True

        def reject_func_QADoc(self,cr,uid,ids,context=None):
                state_change_date = datetime.now().strftime('%Y-%m-%d 00:00:00')
                disposition = context['disposition_status']
                subdisposition = context['subdisposition_status']
                state = context['state_change']
                obj_dispo = self.pool.get('rb.crm.delinquency.disposition')
                #raise osv.except_osv(('warning'),(dispo_stat)) 
		ids_dispo = obj_dispo.search(cr, uid, [('id','=',disposition)])
                obj_dispo_read = obj_dispo.read(cr, uid, ids_dispo, ['dis_type','id'], context)
                for dispo_stat in obj_dispo_read:
                        #raise osv.except_osv(('warning'),(dispo_stat['dis_type'])) 
                        if dispo_stat['dis_type'] not in state:
                                #self.write(cr, uid, ids, {'disposition_status':False,'subdisposition_status':False})
                                raise osv.except_osv(('warning'),('Please Select Correct Disposition'))
                obj_subdisposition = self.pool.get('rb.crm.delinquency.sub.disposition')
                subDisposition_search = obj_subdisposition.search(cr, uid, [('id','=',subdisposition)])
                obj_subdisposition_read = obj_subdisposition.read(cr, uid, subDisposition_search, ['forwardable','name'], context)
                for subdispo_stat in obj_subdisposition_read:
                        if subdispo_stat['forwardable'] :
                                raise osv.except_osv(('warning'),("Please Choose Correct Disposition For Forwarding")) 
		self.write(cr, uid, context['id'], {'state_change': 'Reject'})
		obj_state_change_history = self.pool.get('rb.crm.delinquency.stage.history')
                obj_state_change_history.create(cr, uid,{'related_lead':context['id'],'previous_stage':state,'current_stage':'Reject','concatination_field':str(state_change_date)+'Reject'}, context = context)
		return True

        
	def convert_qa(self, cr, uid, ids, context=None):
                state_change_date = datetime.now().strftime('%Y-%m-%d 00:00:00')
                disposition = context['disposition_status']
                subdisposition = context['subdisposition_status']
                lead_id = context['id']
                state = context['state_change']
                obj_dispo = self.pool.get('rb.crm.delinquency.disposition')
                obj_state_change_history = self.pool.get('rb.crm.delinquency.stage.history')
		ids_dispo = obj_dispo.search(cr, uid, [('id','=',disposition)])
                obj_dispo_read = obj_dispo.read(cr, uid, ids_dispo, ['dis_type','id'], context)
                for dispo_stat in obj_dispo_read:
                        #raise osv.except_osv(('warning'),(dispo_stat['dis_type'])) 
                        if dispo_stat['dis_type'] not in state:
                                #self.write(cr, uid, ids, {'disposition_status':False,'subdisposition_status':False})
                                raise osv.except_osv(('warning'),('Please Select Correct Disposition'))               
                obj_subdisposition = self.pool.get('rb.crm.delinquency.sub.disposition')
                #raise osv.except_osv(('warning'),(dispo_stat))
                subDisposition_search = obj_subdisposition.search(cr, uid, [('id','=',subdisposition)])
                obj_subdisposition_read = obj_subdisposition.read(cr, uid, subDisposition_search, ['forwardable','name'], context)
                #raise osv.except_osv(('warning'),(submition_date))
                for subdispo_stat in obj_subdisposition_read:
                        if subdispo_stat['forwardable'] is False:
                                raise osv.except_osv(('warning'),("Please Choose Correct Disposition For Forwarding"))
                self.write(cr, uid, context['id'], {'state_change': 'qa'})
		obj_state_change_history.create(cr, uid,{'related_lead':lead_id,'previous_stage':state,'current_stage':'qa','concatination_field':str(state_change_date)+'qa'}, context = context)
		return True

	def approved_func_fpc(self,cr,uid,ids,context=None):
                state_change_date = datetime.now().strftime('%Y-%m-%d 00:00:00')
                disposition = context['disposition_status']
                subdisposition = context['subdisposition_status']
                state = context['state_change']
                obj_dispo = self.pool.get('rb.crm.delinquency.disposition')
                #raise osv.except_osv(('warning'),(dispo_stat))
                obj_crm_read = self.read(cr, uid,ids,['fpc_user'], context)
                if obj_crm_read is None:
                        raise osv.except_osv(('warning'),('Please Select Your Following FPC'))
		ids_dispo = obj_dispo.search(cr, uid, [('id','=',disposition)])
                obj_dispo_read = obj_dispo.read(cr, uid, ids_dispo, ['dis_type','id'], context)
                for dispo_stat in obj_dispo_read:
                        #raise osv.except_osv(('warning'),(dispo_stat['dis_type'])) 
                        if dispo_stat['dis_type'] not in state:
                                #self.write(cr, uid, ids, {'disposition_status':False,'subdisposition_status':False})
                                raise osv.except_osv(('warning'),('Please Select Correct Disposition'))
                obj_subdisposition = self.pool.get('rb.crm.delinquency.sub.disposition')
                subDisposition_search = obj_subdisposition.search(cr, uid, [('id','=',subdisposition)])
                obj_subdisposition_read = obj_subdisposition.read(cr, uid, subDisposition_search, ['forwardable','name'], context)
                for subdispo_stat in obj_subdisposition_read:
                        if subdispo_stat['forwardable'] is False:
                                raise osv.except_osv(('warning'),("Please Choose Correct Disposition For Forwarding")) 
		self.write(cr, uid, context['id'], {'state_change': 'qa doc'})
		obj_state_change_history = self.pool.get('rb.crm.delinquency.stage.history')
                obj_state_change_history.create(cr, uid,{'related_lead':context['id'],'previous_stage':state,'current_stage':'qa doc','concatination_field':str(state_change_date)+'qa doc'}, context = context)
		return True

        def approved_func_QADoc(self,cr,uid,ids,context=None):
                state_change_date = datetime.now().strftime('%Y-%m-%d 00:00:00')
                disposition = context['disposition_status']
                subdisposition = context['subdisposition_status']
                state = context['state_change']
                obj_dispo = self.pool.get('rb.crm.delinquency.disposition')
                submition_date = date.today().strftime('%Y-%m-%d')
                #raise osv.except_osv(('warning'),(submition_date)) 
		ids_dispo = obj_dispo.search(cr, uid, [('id','=',disposition)])
                obj_dispo_read = obj_dispo.read(cr, uid, ids_dispo, ['dis_type','id'], context)
                for dispo_stat in obj_dispo_read:
                        #raise osv.except_osv(('warning'),(dispo_stat['dis_type'])) 
                        if dispo_stat['dis_type'] not in state:
                                #self.write(cr, uid, ids, {'disposition_status':False,'subdisposition_status':False})
                                raise osv.except_osv(('warning'),('Please Select Correct Disposition'))
                obj_subdisposition = self.pool.get('rb.crm.delinquency.sub.disposition')
                subDisposition_search = obj_subdisposition.search(cr, uid, [('id','=',subdisposition)])
                obj_subdisposition_read = obj_subdisposition.read(cr, uid, subDisposition_search, ['forwardable','name'], context)
                for subdispo_stat in obj_subdisposition_read:
                        if subdispo_stat['forwardable'] is False:
                                raise osv.except_osv(('warning'),("Please Choose Correct Disposition For Forwarding")) 
		self.write(cr, uid, context['id'], {'state_change': 'sa','submition_date':submition_date})
		obj_state_change_history = self.pool.get('rb.crm.delinquency.stage.history')
                obj_state_change_history.create(cr, uid,{'related_lead':context['id'],'previous_stage':state,'current_stage':'sa','concatination_field':str(state_change_date)+'sa'}, context = context)
		return True
		
	def reject_func_tl(self,cr,uid,ids,context=None):
                state_change_date = datetime.now().strftime('%Y-%m-%d 00:00:00')
                disposition = context['disposition_status']
                subdisposition = context['subdisposition_status']
                state = context['state_change']
                obj_dispo = self.pool.get('rb.crm.delinquency.disposition')
                #raise osv.except_osv(('warning'),(dispo_stat)) 
		ids_dispo = obj_dispo.search(cr, uid, [('id','=',disposition)])
                obj_dispo_read = obj_dispo.read(cr, uid, ids_dispo, ['dis_type','id'], context)
                for dispo_stat in obj_dispo_read:
                        #raise osv.except_osv(('warning'),(dispo_stat['dis_type'])) 
                        if dispo_stat['dis_type'] not in state:
                                #self.write(cr, uid, ids, {'disposition_status':False,'subdisposition_status':False})
                                raise osv.except_osv(('warning'),('Please Select Correct Disposition'))
                obj_subdisposition = self.pool.get('rb.crm.delinquency.sub.disposition')
                subDisposition_search = obj_subdisposition.search(cr, uid, [('id','=',subdisposition)])
                obj_subdisposition_read = obj_subdisposition.read(cr, uid, subDisposition_search, ['forwardable','name'], context)
                for subdispo_stat in obj_subdisposition_read:
                        if subdispo_stat['forwardable'] :
                                raise osv.except_osv(('warning'),("Please Choose Correct Disposition For Forwarding"))
		self.write(cr, uid, context['id'], {'state_change': 'Reject'})
		obj_state_change_history = self.pool.get('rb.crm.delinquency.stage.history')
                obj_state_change_history.create(cr, uid,{'related_lead':context['id'],'previous_stage':state,'current_stage':'Reject','concatination_field':str(state_change_date)+'Reject'}, context = context)
		return True
		
	def approved_func_sa(self,cr,uid,ids,context=None):
                state_change_date = datetime.now().strftime('%Y-%m-%d 00:00:00')
		#customer_lst='null'
                in_no = ''
                disposition = context['disposition_status']
                subdisposition = context['subdisposition_status']
                state = context['state_change']
                obj_dispo = self.pool.get('rb.crm.delinquency.disposition')
                #raise osv.except_osv(('warning'),(dispo_stat)) 
		ids_dispo = obj_dispo.search(cr, uid, [('id','=',disposition)])
                obj_dispo_read = obj_dispo.read(cr, uid, ids_dispo, ['dis_type','id'], context)
                #for dispo_stat in obj_dispo_read:
                        #raise osv.except_osv(('warning'),(dispo_stat['dis_type'])) 
                        #if dispo_stat['dis_type'] not in state:
                                #self.write(cr, uid, ids, {'disposition_status':False,'subdisposition_status':False})
                                #raise osv.except_osv(('warning'),('Please Select Correct Disposition'))
                obj_subdisposition = self.pool.get('rb.crm.delinquency.sub.disposition')
                subDisposition_search = obj_subdisposition.search(cr, uid, [('id','=',subdisposition)])
                obj_subdisposition_read = obj_subdisposition.read(cr, uid, subDisposition_search, ['forwardable','name'], context)
                #for subdispo_stat in obj_subdisposition_read:
                        #if subdispo_stat['forwardable'] is False:
                               # raise osv.except_osv(('warning'),("Please Choose Correct Disposition For Forwarding")) 
                obj_customer = self.pool.get('rb.customer.sale')
                obj_lead = self.pool.get('rb.crm.delinquency.lead')
                #ids = obj_lead.search(cr, uid, [('id','=',id)])
                res_customer = obj_lead.read(cr, uid,ids, ['contact_persion','state_change'], context)
                for r in res_customer:
                        #customer_lst = r['contact_persion']
                        #raise osv.except_osv(('warning'),(r['contact_persion']))
                        try:
                               max_id = str(max(self.pool.get("rb.customer.sale").search(cr, uid, [])))
                               max_id=int(max_id)+1
                               max_id=str(max_id)
                               in_no = 'CUST-'+str(datetime.now().month)+'-'+str(datetime.now().day)+'-'+str(datetime.now().year)+'-'+max_id
                        except Exception:
                               in_no = 'CUST-'+str(datetime.now().month)+'-'+str(datetime.now().day)+'-'+str(datetime.now().year)+'-'+'1'
                        obj_customer.create(cr, uid,{'name': r['contact_persion'],'details':context['id'],'customer_id':in_no}, context=None)
			self.write(cr, uid, context['id'], {'state_change': 'customer'})
		obj_state_change_history = self.pool.get('rb.crm.delinquency.stage.history')
                obj_state_change_history.create(cr, uid,{'related_lead':context['id'],'previous_stage':state,'current_stage':'customer','concatination_field':str(state_change_date)+'customer'}, context = context)
		return True	
			




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


                obj_self = self.pool.get('rb.crm.delinquency.lead')
                obj_self_read = obj_self.read(cr, uid, ids, ['last_call_id','id'], context)
                for var_read_obj in obj_self_read:
                    if(var_read_obj['id']==context['id']):
                        global_last_call_id = var_read_obj['last_call_id']
                        #raise osv.except_osv(('warning'),(global_last_call_id))

                

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
		#raise osv.except_osv(('warning'),(xmlvar))
		urllib2.urlopen(xmlvar)
                callend_information = self.pool.get('crm.delinquency.save.calldetails')
                if False in(context['disposition_status'], context['subdisposition_status']):
                    raise osv.except_osv(('warning'),('Select Disposition And SubDisposition'))
                if context['disposition_status'] is 12:
                      raise osv.except_osv(('warning'),('Dialed data cannot have a  "New Lead" status')) 

                vvar=callend_information.browse(cr, uid, global_last_call_id, context)

                call_start =vvar['s_call_time']
                #raise osv.except_osv(('warning'),(datetime.datetime.now()))
                #call_start = call_start.replace(' ','')
                call_start = datetime.strptime(call_start, "%Y-%m-%d %H:%M:%S.%f")

                differ = datetime.now() - call_start

		#SUDIPTA
                #request_url = 'http://'+var_ip+'/dialer/play.php?leadid='+str(context['id'])+'&callid='+str(global_last_call_id)
		#callend_information.write(cr, uid, global_last_call_id, {'differ_time':differ,'s_endcall_time':datetime.now(),'s_disposition_id':context['disposition_status'],'s_subdisposition_id':context['subdisposition_status'],'record_url':request_url}, context=None)

                callend_information.write(cr, uid, global_last_call_id, {'differ_time':differ,'s_endcall_time':datetime.now(),'s_disposition_id':context['disposition_status'],'s_subdisposition_id':context['subdisposition_status']}, context=None)
                
		
		
		#search_dial_ids[] = obj.search(cr, uid, [('last_lead_id','=',last_lead)])   #--------
		#raise osv.except_osv(('warning'),(obj.search(cr, uid, [('last_lead_id','=',last_lead)])))
		obj.write(cr, uid, uid, {'last_lead_id':context['id']}) #----------
		self.write(cr, uid, context['id'], {'state': 'draft','gate':''})
		
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


		res = obj.read(cr, uid, ids, ['server_name','internal_number','id','last_lead_id','dial_state'], context)
		
		for r in res:
			if (r['id']==uid):
                            if r['last_lead_id']:
                                    last_lead_state = self.read(cr, uid, r['last_lead_id'], ['state'], context)
                                    #raise osv.except_osv(('warning'),(r['last_lead_id']))
                                    if (last_lead_state and last_lead_state['state']=='Hangup'):
                                            raise osv.except_osv(('warning'),('Please Hangup Lead No:'+str(r['last_lead_id'])))
                            
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
                        save_information = self.pool.get('crm.delinquency.save.calldetails')
                        last_id = save_information.create(cr, uid,{'name':str(var),'s_ip_address': var_ip,'s_agent_id':int(var),'s_user_name':int(uid),'s_lead_id':int(context['id']),'s_call_time':datetime.now(),'rela_lead':int(context['id']),'mobile':mobile}, context=None)
                        xmlvar = 'http://'+var_ip+'/'+var_callparam+'?xml=<request><security><username>'+var_uname+'</username><password>'+var_pswd+'</password></security><content><agent>'+var+'</agent><phoneNumber>'+mobile+'</phoneNumber><server>'+var_ip+'</server><leadId>'+str(context['id'])+'</leadId><callId>'+str(last_id)+'</callId></content></request>'
                        #raise osv.except_osv(('warning'),(xmlvar))
                        response=urllib2.urlopen(xmlvar)
                        #response.close()
                        #var_info = self.browse(cr, uid, ids, context=context)
                        #raise osv.except_osv(('warning'),(context['id']))
                        #present_lead_id = lead_id_information.browse(cr, uid, ids, context=context)
                        #raise osv.except_osv(('warning'),(present_lead_id.id))
                        #save_information = self.pool.get('crm.delinquency.save.calldetails')
                        #raise osv.except_osv(('warning'),(context['id']))
                        
                        #raise osv.except_osv(('warning'),(global_var))
                        self.global_saveid = last_id
                        #raise osv.except_osv(('warning'),(last_id))
                        self.write(cr, uid, context['id'], {'state': 'Hangup','last_call_id':last_id,'disposition_status':False,'subdisposition_status':False,'gate':'all'})
                        obj.write(cr, uid, ids, {'last_lead_id':context['id']})
		
		return True
						 
						 

        
		
	
	
	
	
	
	
	


	_name = "rb.crm.delinquency.lead"

	_columns = {
				'name':fields.char("Subject", required=True),
                                'state': fields.char("State"),
				'contact_persion':fields.char("Contact Name"),
				'mobile':fields.char("Mobile"),
				'create_date' : fields.datetime('Date Created', readonly=True),
				'phone':fields.char("Phone"),
				#'campaign_team':fields.many2one('rb.campaign.crm','Campaign',change_default=True,required=True),
				#'sale_team_name':fields.many2one('rb.sales.team','Sales Team',change_default=True,domain="[('campaign_name_id','=',campaign_team)]",required=True),
                                'sale_team_name':fields.many2one('rb.sales.team','Sales Team',change_default=True,domain="[('team_member','=',sales_team_r)]",required=True),
				'quality_asur':fields.many2one('rb.qa.team', 'QA Group',domain="[('id','=',sale_team_name)]"),
				'team_lead':fields.many2one('rb.tl.team', 'TL Group',domain="[('id','=',sale_team_name)]"),
                                'sales_mngr':fields.many2one('rb.sm.team', 'PM Group',domain="[('id','=',sale_team_name)]"),
				'sales_admin':fields.many2one('rb.sa.team', 'SA Group',domain="[('id','=',sale_team_name)]"),
                                'quality_doc_group':fields.many2one('rb.doc.qa.team', 'QA Doc Group',domain="[('id','=',sale_team_name)]"),
				'financial_p_conlt':fields.many2one('rb.fpc.team','FPC DE Group',domain="[('id','=',sale_team_name)]"),
				'sales_team_r':fields.many2one('res.users','TSR',domain="[('sales_team','=',sale_team_name)]"),
				'disposition_status':fields.many2one('rb.crm.delinquency.disposition','Delinquency Disposition',change_default=True),
                                'subdisposition_status':fields.many2one('rb.crm.delinquency.sub.disposition',' Delinquency Sub Disposition',domain="[('disposition_status','=',disposition_status)]"),
				#'batch_code':fields.many2one('rb.crm.batch.code','Batch Code',change_default=True),	
				'company_name':fields.char('Company Name'),
				#'callback_date':fields.datetime('Callback Date'),
				#'appo_date':fields.datetime('Appointment Date'),
				'birth_date':fields.date('Date Of Birth'),
				'home_phone':fields.char('Home Phone'),
				'age':fields.integer('Age'),
				'email_id':fields.char('Email'),
                                'gender':fields.selection([('male','Male'),('female','Female')],'Gender'),
				'street': fields.char('Street'),
				'street2': fields.char('Street2'),
				'zip': fields.char('Zip', change_default=True),
				'city': fields.char('City'),
                                'city_id':fields.many2one('rb.city','City'),
				'state_id': fields.many2one("res.country.state", 'State'),
				'country_id': fields.many2one('res.country', 'Country'),
				'title': fields.many2one('res.partner.title', 'Title'),
				'fpc_user': fields.many2one('res.users', 'FPC',domain="[('fpc_group','=',sale_team_name)]"),
				'state_change':fields.char('State'),
				'dis_type':fields.char('State'),
				'description': fields.text('Notes'),
				'gate':fields.char('GATE'),
                                'remarks':fields.char('Remarks'),
                                'relation2disposition':fields.one2many('rb.crm.delinquency.disposition.history', 'related_lead', 'Disposition History'),
                                'relation2statechange':fields.one2many('rb.crm.delinquency.stage.history', 'related_lead', 'Stage History'),
                                'relation2savecall':fields.one2many('crm.delinquency.save.calldetails', 'rela_lead', 'Call History'),
                                'submition_date': fields.date('Modyfied Date'),
                                'callback_state':fields.char('Call Back Status'),
                                'rela2callback_stages':fields.one2many('rb.crm.delinquency.callback.stage', 'related_lead', 'Callback Summary'),
                                'lead_ref_stat' : fields.boolean('Lead reference status'), 
                                'tsr_change_flag' : fields.boolean('TSR Change Flag'),
                                'product_desc': fields.char("Product")
                                
				
	}
	

class ihrit_res_users(osv.osv):

	_inherit = 'res.users'

	_columns = {

				
			'password':fields.char('Password',required=False),
			'teamleader_name':fields.many2one('res.users',"Teamleader Name"),
			'teamleader_code':fields.char('Teamleader Code'),		


	}

ihrit_res_users()
