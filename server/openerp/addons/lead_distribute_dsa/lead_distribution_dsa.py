from osv import fields, osv
from openerp.osv import fields, osv
import csv
import base64
import tempfile
import cgi, os
import random
import struct
import platform
import logging
import datetime
from datetime import date
import tempfile

_logger = logging.getLogger(__name__)




########### dsa Lead Form #############

class get_dsa_list(osv.osv):
    _name = 'get.dsa.list'

    
    def create(self, cr, uid, val, context = None):
        x_var_set = []
        field_value = val['select_sales_team']
        xab =  super(get_dsa_list,self).create(cr,uid,val,context)
        self.write(cr, uid, xab, {'state': 1})
        fl_dt = self.browse(cr, uid, xab, context).data
        try:
            fl_dt = fl_dt.decode('base64')
        except Exception:
            raise osv.except_osv(('warning'),('Please Uplaod Lead First'))
        t_counter = (fl_dt.count('\n'))-1
        #raise osv.except_osv(('warning'),(t_counter))
        if self.browse(cr, uid, xab, context).quantity<1:
            self.write(cr, uid, xab, {'quantity': t_counter})

        var_lst = []
        m2o_tup = ()
        obj_var = self.pool.get('res.users')
        cr.execute('select str.res_users_id from rb_fpc_rel str,res_users usr where str.sales_team_id = %s and str.res_users_id = usr.id and usr.active is TRUE',(field_value,))
        dsa_id = cr.fetchall()
        for row in dsa_id:
            var = row [0]
            x_var_set.append(row [0])
            dsa_usr_name = obj_var.browse(cr, uid, row [0], context)
            self.pool.get('res.users')
            m2o_tup = (str(var),dsa_usr_name['name'],0)
            var_lst.append(m2o_tup)
        self.write(cr, uid, xab, {'select_dsa': var_lst})

            
        for set_id in x_var_set:
            self.pool.get('user.lead.mapping.dsa').create(cr, uid,{'name':datetime.datetime.now().strftime("%Y%m%d%H%M%S"),'dsa_name':set_id,'reference_with_ldist':int(xab),'batch_code':int(self.browse(cr, uid, xab, context).s_batch_code)}, context=None)
        return xab
    def func_get_sales_team(self,cr,uid,ids,field_value,context=None):
        return True
    def func_get_dsa(self,cr,uid,ids,field_value,context=None):
        return True


    def func_get_batch_details(self,cr,uid,ids,field_value,context=None):
        obj = self.pool.get('rb.crm.batch.code').browse(cr, uid, int(field_value), context)
        #raise osv.except_osv(('warning'),(obj.database_name))
        return {'value': {'database_name':obj.database_name,'batch_id':obj.id}}


    
    def import_file(self,cr,uid,ids,context=None):
        dstv_lead = 0
        lead_reminder = 0
        assigned = 0
        lst_dsa_id = []
        dsa_count = 0
        nol = []
        bol = context['auto_distribute']
        quantity=context.get('quantity')
        row_left = 0
        to = 0
        gate_stat = False
        boundary = 0
        peak = False
        obj = self.pool.get('rb.sales.team')
        obj_rs = obj.browse(cr, uid, context['select_sales_team'], context)
        onj_lst = self.pool.get('user.lead.mapping.dsa').search(cr, uid, [('reference_with_ldist', '=', context['id'])])
        for dsa_isd in self.pool.get('user.lead.mapping.dsa').read(cr, uid, onj_lst, [], context):
            lst_dsa_id.append(dsa_isd['dsa_name'][0])
            nol.append(dsa_isd['no_of_lead'])
            dsa_count = dsa_count+1
        var_qa_group = int(obj_rs.quality_asur_group)
        var_tl_group = int(obj_rs.team_lead_group)
        var_sa_group = int(obj_rs.sales_admin_group)
        var_qa_doc_group = int(obj_rs.quality_doc_group)
        var_fpc_de_group = int(obj_rs.financial_conlt_group)
        pm_group = int(obj_rs.sales_mgr_group)
        _logger.error(var_qa_group,var_tl_group,var_sa_group,var_qa_doc_group,var_fpc_de_group)
        lstp=''
        toup=()
        record = self.pool.get('get.dsa.list').browse(cr, uid, context['id'], context)
        if (platform.system()=='Windows'):
            file_path = 'E:/x.csv'
        else:
            file_path = '/opt/openerpcrm/tmp_lead.csv'

        bdata = record.data
        blist = record.select_dsa
        f = open(file_path,'wb')
        f.write(bdata.decode('base64'))
        f.flush()
        f.close
        no_row = 0
        lstp = blist
        mylist = lstp.split(',')
        _logger.error(len(mylist))
        size = len(mylist)
        chrms = [mylist[x:x+3] for x in xrange(0, size, 3)]
        _logger.error(chrms)
        _logger.error(chrms[0][1])
        _logger.error(len(chrms))
        team_size = len(chrms)
        _logger.error(chrms[0])
        cur_pos_pointer = -1
        t_Rows = (len(list(csv.reader(open(file_path)))))-1
        #raise osv.except_osv(('warning'),(bol))
        for dsa_var in range(0,team_size):
            _logger.error('Record To'+chrms[dsa_var][2])
            assigned_dsa = lst_dsa_id[dsa_var]
            _logger.error(assigned_dsa)
            with open(file_path, 'rb') as fd:
                row_pointer = 0
                reader = csv.reader(fd)
                for row in csv.reader(fd):
                    if (row_pointer>0):
                        dob=False
                        city_id=0
                        if row[8]:
                                dob = row[8]
                        if row[12]:
                            city_id = self.pool.get('rb.city').search(cr, uid, [('name', '=', row[12])])
                        else:
                            raise osv.except_osv(('warning'),('Missing city name at line  %s') %(row_pointer))
                        if not city_id:
                            raise osv.except_osv(('warning'),('Please enter currect city name at line  %s') %(row_pointer))  
                        if not row[17]:
                            raise osv.except_osv(('warning'),('Missing district name at line %s') %(row_pointer))

                        if(bol is False):
                            if(peak is False):
                                peak = True
                            if (row_pointer > cur_pos_pointer   and  row_pointer <=(int(nol[dsa_var])+cur_pos_pointer)  ):
                                _logger.error(str(row)+'______________________________________________________________'+str(assigned_dsa))
                                _logger.error(row[0])
                                _logger.error(row[1])
                                
                                self.pool.get('rb.crm.lead').create(cr, uid,{'state_change':'fpc','callback_state':'close','batch_code':int(self.browse(cr, uid, context['id'], context).s_batch_code),'contact_persion': row[0],'phone':row[1],'street':row[2],'street2':row[3],'monthly_income':float(row[5]) if row[5] else 0.0,'name':row[4],'disposition_status':6,'subdisposition_status':28,'mobile':row[6],'email_id':row[7],'birth_date':dob,'id_card_no':row[9],'company_name':row[10],'designation':row[11],'city_id':city_id[0] or None,'gender':row[13],'exprience':row[14],'education_institution':row[15],'degree':row[16],'x_district':row[17],'x_industry':row[18],'company_street':row[19],'fpc_user':assigned_dsa,'campaign_team':int(context['select_campaign']),'quality_asur':var_qa_group,'team_lead':var_tl_group,'quality_doc_group':var_qa_doc_group,'sales_admin':var_sa_group,'financial_p_conlt':var_fpc_de_group,'sale_team_name':int(context['select_sales_team']),'sales_mngr':pm_group,'appo_date':datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}, context=None)
                                if(row_pointer == (int(nol[dsa_var])+cur_pos_pointer)):
                                    cur_pos_pointer = (row_pointer)
                                    _logger.error(":::::::::::::%s",cur_pos_pointer)
                                    break
                        elif(bol):
                            if (quantity < dsa_count):
                                raise osv.except_osv(('warning'),('The no of lead should be greater than DSA list'))
                            if(gate_stat is False):
                                dstv_lead = t_Rows/len(nol)
                                lead_reminder = dstv_lead%len(nol)
                                boundary = (dstv_lead*len(nol))
                                row_left = t_Rows - boundary
                                to = boundary+row_left
                                gate_stat = True
                            if (row_pointer > cur_pos_pointer   and  row_pointer <=(dstv_lead+cur_pos_pointer)  ):
                                _logger.error(str(row)+'______________________________________________________________'+str(assigned_dsa))
                                _logger.error(row[0])
                                _logger.error(row[1])
                                self.pool.get('rb.crm.lead').create(cr, uid,{'state_change':'fpc','callback_state':'close','batch_code':int(self.browse(cr, uid, context['id'], context).s_batch_code),'contact_persion': row[0],'phone':row[1],'street':row[2],'street2':row[3],'monthly_income':float(row[5]) if row[5] else 0.0,'name':row[4],'disposition_status':6,'subdisposition_status':28,'mobile':row[6],'email_id':row[7],'birth_date':dob,'id_card_no':row[9],'company_name':row[10],'designation':row[11],'city_id':city_id[0],'gender':row[13],'exprience':row[14],'education_institution':row[15],'degree':row[16],'x_district':row[17],'x_industry':row[18],'company_street':row[19],'fpc_user':assigned_dsa,'campaign_team':int(context['select_campaign']),'quality_asur':var_qa_group,'team_lead':var_tl_group,'quality_doc_group':var_qa_doc_group,'sales_admin':var_sa_group,'financial_p_conlt':var_fpc_de_group,'sale_team_name':int(context['select_sales_team']),'sales_mngr':pm_group,'appo_date':datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}, context=None)
                                if(row_pointer == (dstv_lead+cur_pos_pointer)):
                                    cur_pos_pointer = (row_pointer)
                                    _logger.error(":::::::::::::%s",cur_pos_pointer)
                                    break

                        row_pointer = row_pointer+1
                    else:
                        row_pointer = row_pointer+1
                fd.close()
	with open(file_path, 'rb') as rd:
            kalibabu = list(csv.reader(rd))
           
            if(gate_stat):
                from_ = boundary
                for lefts in range(from_,(to+1)):
                    _logger.error(str(kalibabu[lefts])+'#######################################==============================>')
                    row = kalibabu[lefts]
                    self.pool.get('rb.crm.lead').create(cr, uid,{'state_change':'fpc','callback_state':'close','batch_code':int(self.browse(cr, uid, context['id'], context).s_batch_code),'contact_persion': row[0],'phone':row[1],'street':row[2],'street2':row[3],'monthly_income':float(row[5]) if row[5] else 0.0,'name':row[4],'disposition_status':6,'subdisposition_status':28,'mobile':row[6],'email_id':row[7],'birth_date':dob,'id_card_no':row[9],'company_name':row[10],'designation':row[11],'city_id':city_id[0],'gender':row[13],'exprience':row[14],'education_institution':row[15],'degree':row[16],'x_district':row[17],'x_industry':row[18],'company_street':row[19],'fpc_user':random.choice(lst_dsa_id),'campaign_team':int(context['select_campaign']),'quality_asur':var_qa_group,'team_lead':var_tl_group,'quality_doc_group':var_qa_doc_group,'sales_admin':var_sa_group,'financial_p_conlt':var_fpc_de_group,'sale_team_name':int(context['select_sales_team']),'sales_mngr':pm_group,'appo_date':datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}, context=None)
            if(peak):
                row = kalibabu[-1]
                self.pool.get('rb.crm.lead').create(cr, uid,{'state_change':'fpc','callback_state':'close','batch_code':int(self.browse(cr, uid, context['id'], context).s_batch_code),'contact_persion': row[0],'phone':row[1],'street':row[2],'street2':row[3],'monthly_income':float(row[5]) if row[5] else 0.0,'name':row[4],'disposition_status':6,'subdisposition_status':28,'mobile':row[6],'email_id':row[7],'birth_date':dob,'id_card_no':row[9],'company_name':row[10],'designation':row[11],'city_id':city_id[0],'gender':row[13],'exprience':row[14],'education_institution':row[15],'degree':row[16],'x_district':row[17],'x_industry':row[18],'company_street':row[19],'fpc_user':lst_dsa_id[0],'campaign_team':int(context['select_campaign']),'quality_asur':var_qa_group,'team_lead':var_tl_group,'quality_doc_group':var_qa_doc_group,'sales_admin':var_sa_group,'financial_p_conlt':var_fpc_de_group,'sale_team_name':int(context['select_sales_team']),'sales_mngr':pm_group,'appo_date':datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}, context=None)


            rd.close()
        
        return True
                     
                
    _columns = {
                'select_campaign': fields.many2one('rb.campaign.crm', 'Select Campaign',required=True),
                'select_sales_team' : fields.many2one('rb.sales.team', 'Select Sales Team',domain="[('campaign_name_id','=',select_campaign)]",required=True),
                'select_dsa':fields.text('Sales Team'),
                'data':fields.binary('File',filters='*.csv'),
                'auto_distribute':fields.boolean('Auto assign'),
                'relation_with_leadmap' : fields.one2many('user.lead.mapping.dsa', 'reference_with_ldist', 'Dependents'),
                's_batch_code' : fields.many2one('rb.crm.batch.code','Batch',required=True),
                'state' : fields.char('State'),
                'upload_date' : fields.datetime('Uplaod Date'),
                'quantity' : fields.integer('Quantity'),
                'database_name':fields.char('Database Name'),
                'batch_id':fields.char('Batch ID'),
            }
    _defaults = {'upload_date': date.today().strftime('%Y-%m-%d')}
    
get_dsa_list()



class user_lead_mapping(osv.osv):
    _name='user.lead.mapping.dsa'
    def unlink(self, cr, uid, ids, context=None):
        raise osv.except_osv(('warning'),('You cannot delete assigned record'))
        
    _columns = {
                'name' : fields.char('Title'),
                'dsa_name' : fields.many2one('res.users','DSA'),
                'no_of_lead' : fields.integer('No Of leads'),
                'batch_code' : fields.many2one('rb.crm.batch.code','Select Batch'),
                'reference_with_ldist' : fields.many2one('get.dsa.list','Reference To Lead Distribution'),

                }
    #_defaults = {'dsa_name': ''}
user_lead_mapping()
