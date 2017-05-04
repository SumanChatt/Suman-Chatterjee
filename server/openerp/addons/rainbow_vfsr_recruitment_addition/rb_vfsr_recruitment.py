# -*- coding: utf-8 -*-
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
import psycopg2
import xmlrpclib

class vfsr_recruitment_process(osv.osv):
    _name = "vfsr.recruitment.process"




    def create(self, cr, uid, values, context=None):
        #if (uid != 1):
        srt=values['source_type'] 
        sr=values['source'] 
            
        new_id = super(vfsr_recruitment_process, self).create(cr, uid, values, context)
        if (uid != 1):
            cr.execute('update vfsr_recruitment_process set source_type=%s, source=%s where id=%s',(srt,sr,new_id,))
        #try:
        #res = self.pool.get('res.users').read(cr, uid, uid, ['login','password'], context)
        #raise osv.except_osv(('warning'),(res['login']+res['password']))
        #username = res['login']
        #pwd = res['password']
        #dbname = 'hrms'
        #connection 
        #sock_common = xmlrpclib.ServerProxy ('http://192.169.200.168:8070/xmlrpc/common')
        #register and getting uid/token
        #uid = sock_common.login(dbname, username, pwd)
        #creating valid connection object
        #sock = xmlrpclib.ServerProxy('http://192.169.200.168:8070/xmlrpc/object')
        ##Create New Contact
        #data_address = sock.execute(dbname, uid, pwd, 'res.partner', 'create', {'name':values['address']})
        ##Look For new data source if exists otherwise create new
        #source = values['source']
        #ids = sock.execute(dbname, uid, pwd, 'hr.recruitment.source', 'search', [('name', '=ilike', source)])
        #if len(ids)>0:
        #    source = ids[0]
        #else:
        #   source =  sock.execute(dbname, uid, pwd, 'hr.recruitment.source', 'create', {'name':source.upper()})
        return new_id

        #data = {
        #       'name': values['vfsr_name']+"'s Application",
        #       'partner_name': values['vfsr_name'],
        #       'job_id': 97,
        #       'email_from':values['email'] if values['email'] else False,
        #       'partner_mobile':values['mobile'],
        #       'location': values['locaton'] if values['locaton'] else False,
        #       'id_no':values['name'] if values['name'] else False,
        #       'dob':values['dob'] if values['dob'] else False,
        #       'profession': values['profession'] if values['profession'] else False,
        #       'province' : values['province'] if values['province'] else False,
        #       'partner_id' : data_address,
        #       'source_id': source,
        #       'gate' : 'Lock'
        #        }
        #cv_id = sock.execute(dbname, uid, pwd, 'hr.applicant', 'create', data)
        #except:
         #   self.write(cr, uid,new_id, {'status':'Failed to upload CV'})
        
        #return new_id


        
        
        


    def get_team_description(self, csr, uid, context=None): #lst=[]    toup=(str(k),str(k)) lst.append(toup)
        lst = []
        conn = psycopg2.connect(database="openerpcrm", user="openerpcrm", password="openerpcrm", host="127.0.0.1", port="5432")
        db = conn.cursor()
        db.execute("SELECT DISTINCT(description) FROM rb_sales_team")
        rows = db.fetchall()
        for item in rows:
            toup = (str(item[0].encode('utf-8')),str(item[0].encode('utf-8'))) if item[0] else ('None','None')
            lst.append(toup)
        return lst


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

	

		#ids = obj.search(cr, uid, [('id','=',uid)])


		res = obj.read(cr, uid, uid, ['server_name','internal_number','id','last_lead_id','dial_state'], context)
		cnvrt_to_lst = []
                cnvrt_to_lst.append(res)
		
		for r in cnvrt_to_lst:
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
                        obj.write(cr, uid, uid, {'last_lead_id':context['id']})
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


                #obj_self = self.pool.get('vfsr.recruitment.process')
                #obj_self_read = obj_self.read(cr, uid, ids, ['last_call_id','id'], context)
		obj_self_read = self.read(cr, uid, ids, ['last_call_id','id'], context)
                for var_read_obj in obj_self_read:
                    if(var_read_obj['id']==context['id']):
                        global_last_call_id = var_read_obj['last_call_id']
                        

                

		#ids = obj.search(cr, uid, [('id','=',uid)])



		res = obj.read(cr, uid, uid, ['server_name','internal_number','id','last_lead_id'], context) #---
		convert_to_list = []
                convert_to_list.append(res)
		for r in convert_to_list:
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

    def disposition_onchange(self,cr,uid,ids,context=None):
                var_subdisposition = False
                val = {'subdisposition':var_subdisposition}
                return {'value': val}








    

    _columns = {
        'mobile' : fields.char("Contact Number"),
        'vfsr_name': fields.char("VFSR"),
        'locaton': fields.char("Location"),
        'name' : fields.char("National ID"),
        'dob': fields.date("Date Of Birth"),
        'team_leader': fields.many2one('res.users',"Team Leader"),
        'Project': fields.selection(get_team_description,"Project"),
        'profession': fields.char("Profession"),
        'province' : fields.char("Province"),
        'disposition': fields.many2one('vfsr.disposition',"Disposition"),
        'subdisposition':fields.many2one('vfsr.sub.disposition',"Suib Disposition",domain="[('disposition','=',disposition)]"),
        'description' : fields.char('Note'),
        'state': fields.char('State'),
        'last_call_id' : fields.integer("Last Call ID"),
        'gate' : fields.char('Gate'),
        'calling_history':fields.one2many('vfsr.application.call.history', 'rela_lead', 'Calling History', readonly = True),
        ##Questionnaires Section
        'q1' : fields.boolean('Có đăng ký làm nhân viên tư vấn tín dụng bán sản phẩm VPBFC không?'),
        'q2' : fields.boolean('Vui lòng xác nhận lại số CNMD, ngày cấp, nới cấp'),
        'q3' : fields.boolean('Tỉnh thành đăng ký làm việc'),
        'q4' : fields.boolean('Làm việc với TL nào'),
        'q5' : fields.boolean('Đăng kỳ làm việc cho Cty nào?'),
        'q6' : fields.boolean('CV anh chị phải làm là gì?'),
        'q7' : fields.boolean('Đã được đào tạo hay chưa?'),
        'q8' : fields.boolean('Các sản phẩm chính của VPBFC là gì?'),
        'q9' : fields.boolean('Điều kiện vay theo lương (Đặt các câu hỏi nhỏ, như tuổi bao nhiêu? Lương bao nhiêu? Chứng minh lương bằng cách nào?)'),
        'q10' : fields.boolean('Điều kiện vay theo EVN(Đặt các câu hỏi nhỏ, như tuổi bao nhiêu? Lương bao nhiêu? Chứng minh lương bằng cách nào?)'),
        'q11' : fields.boolean('Điều kiện vay theo Bảo Hiểm(Đặt các câu hỏi nhỏ, như tuổi bao nhiêu? Lương bao nhiêu? Chứng minh lương bằng cách nào?)'),
        'q12' : fields.boolean('Các câu hỏi liên quan đến sản phẩm: Lãi suất, khoản vay, quy trình…'),
        'q13' : fields.boolean('Anh chị đã được đào tạo về Code of Conduct/Nguyên tắc ứng xử chưa?'),
        'q14' : fields.boolean('Các hành động nào là nghiêm cấm?'),
        'q15' : fields.boolean('Nếu KH đưa tiền, tối đa số tiền anh chị được nhận là bao nhiêu?'),
        'q16' : fields.boolean('Các câu hỏi tình huống: VD Trường hợp KH bận, gửi hồ sơ cho người thân,bạn phải làm gì để nhận được hồ sơ này?'),
        'q17' : fields.boolean('VDAnh A đã chuẩn bị hồ sơ cho vợ của anh A. Anh A nhờ bạn đến nhận hồ sơ để làm cho vợ anh. Bạn phải làm gì để giúp KH vay?'),
        'q18' : fields.boolean('Khi có hồ sơ, anh chị nộp ở đâu?'),
        'q19' : fields.boolean('Sau khi hồ sơ lên hệ thống, sẽ có những bước thẩm định nào?'),
        'q20' : fields.boolean('Khi thẩm định đến nhà, có nhất thiết có KH ở nhà không?'),
        'q21' : fields.boolean('Những câu hỏi khác'),
        'q22' : fields.boolean('KH phải chuẩn bị gì khi có thẩm định đến'),
        #Fe Coding
        'coded_by_fe' : fields.boolean('Coded by FE Credit'),
        'fe_code' : fields.char('FE code'),
        'rejected_by_fe' :fields.boolean('Rejected by FE Credit'),

        'source':fields.char('Data Source',write=['base.group_erp_manager']),
        'recruiter': fields.char("Qa"), ## Receieve QA emailif the cvs came from CV Otherwise Left Blank

        'email': fields.char("Emil"),
        'address' :fields.char('Address'),

        'status' : fields.char('CV Upload Status'),
        'create_uid' : fields.many2one('res.users','Owner'),
        'create_date' : fields.datetime('Create Date'),
        'write_date': fields.datetime('Write Date'),
	'fte_coding_rejection_date': fields.date('FE Coding/Rejection Date'),
	'source_type':fields.selection([('Project','Project'),('Database','Database'),('Personal','Personal'),('Deactivated','Deactivated'),('Others','Others')],string='Source Type',write=['base.group_erp_manager']),
        'income':fields.float("Income of vfsr(in VND)"),
        
        }
    _defaults = {'state': 'draft','disposition':6,'source_type':'Personal'} #Need to Change
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

