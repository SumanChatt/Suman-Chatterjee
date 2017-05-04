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




########### Tsr Lead Form #############

class get_tsr_list(osv.osv):

    _name = 'get.tsr.list'
    
    def create(self, cr, uid, val, context = None):
        x_var_set = []
	field_value = val['select_sales_team']
        xab =  super(get_tsr_list,self).create(cr,uid,val,context)
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
        cr.execute('select str.res_users_id from rb_sales_team_rel str,res_users usr where str.sales_team_id = %s and str.res_users_id = usr.id and usr.active is TRUE',(field_value,))
        tsr_id = cr.fetchall()
        for row in tsr_id:
            var = row [0]
            x_var_set.append(row [0])
            tsr_usr_name = obj_var.browse(cr, uid, row [0], context)
            self.pool.get('res.users')
            m2o_tup = (str(var),tsr_usr_name['name'],0)
            var_lst.append(m2o_tup)
        self.write(cr, uid, xab, {'select_tsr': var_lst})

            
        for set_id in x_var_set:
            self.pool.get('user.lead.mapping').create(cr, uid,{'name':datetime.datetime.now().strftime("%Y%m%d%H%M%S"),'tsr_name':set_id,'reference_with_ldist':int(xab),'batch_code':int(self.browse(cr, uid, xab, context).s_batch_code)}, context=None)
        return xab
    def func_get_sales_team(self,cr,uid,ids,field_value,context=None):
        ##return {'value':{'select_sales_team':''}}
        return True
    def func_get_tsr(self,cr,uid,ids,field_value,context=None):
        print "Blank Function"
##        var_lst = []
##        m2o_tup = ()
##        obj_var = self.pool.get('res.users')
##        cr.execute('select str.res_users_id from rb_sales_team_rel str,res_users usr where str.sales_team_id = %s and str.res_users_id = usr.id and usr.active is TRUE',(field_value,))
##        tsr_id = cr.fetchall()
##        self._var_set = []
##        for row in tsr_id:
##            var = row [0]
##            self._var_set.append(row [0])
##            tsr_usr_name = obj_var.browse(cr, uid, row [0], context)
##            self.pool.get('res.users')
##            m2o_tup = (str(var),tsr_usr_name['name'],0)
##            var_lst.append(m2o_tup)
##        return {'value': {'select_tsr':var_lst}}


    def func_get_batch_details(self,cr,uid,ids,field_value,context=None):
        obj = self.pool.get('rb.crm.batch.code').browse(cr, uid, int(field_value), context)
        #raise osv.except_osv(('warning'),(obj.database_name))
        return {'value': {'database_name':obj.database_name,'batch_id':obj.id}}


    
    def import_file(self,cr,uid,ids,context=None):
        dstv_lead = 0
        lead_reminder = 0
        assigned = 0
        lst_tsr_id = []
        
        nol = []
        bol = context['auto_distribute']
        row_left = 0
        to = 0
        gate_stat = False
        boundary = 0
        peak = False
        obj = self.pool.get('rb.sales.team')
        obj_rs = obj.browse(cr, uid, context['select_sales_team'], context)
        onj_lst = self.pool.get('user.lead.mapping').search(cr, uid, [('reference_with_ldist', '=', context['id'])])
        for tsr_isd in self.pool.get('user.lead.mapping').read(cr, uid, onj_lst, [], context):
            lst_tsr_id.append(tsr_isd['tsr_name'][0])
            nol.append(tsr_isd['no_of_lead'])
        var_qa_group = int(obj_rs.quality_asur_group)
        var_tl_group = int(obj_rs.team_lead_group)
        var_sa_group = int(obj_rs.sales_admin_group)
        var_qa_doc_group = int(obj_rs.quality_doc_group)
        var_fpc_de_group = int(obj_rs.financial_conlt_group)
        pm_group = int(obj_rs.sales_mgr_group)
        _logger.error(var_qa_group,var_tl_group,var_sa_group,var_qa_doc_group,var_fpc_de_group)
        lstp=''
        toup=()
        record = self.pool.get('get.tsr.list').browse(cr, uid, context['id'], context)
        if (platform.system()=='Windows'):
            file_path = 'E:/x.csv'
        else:
            file_path = '/opt/openerpcrm/tmp_lead.csv'

        bdata = record.data
        blist = record.select_tsr
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
        for tsr_var in range(0,team_size):
            _logger.error('Record To'+chrms[tsr_var][2])
            assigned_tsr = lst_tsr_id[tsr_var]
            _logger.error(assigned_tsr)
            with open(file_path, 'rb') as fd:
                row_pointer = 0
                reader = csv.reader(fd)
                for row in csv.reader(fd):
                    if (row_pointer>0):
                        dob=False
                        if row[8]:
                                dob = row[8]
                        if(bol is False):
                            if(peak is False):
                                peak = True
                            if (row_pointer > cur_pos_pointer   and  row_pointer <=(int(nol[tsr_var])+cur_pos_pointer)  ):
                                _logger.error(str(row)+'______________________________________________________________'+str(assigned_tsr))
                                _logger.error(row[0])
                                _logger.error(row[1])
                                
                                self.pool.get('rb.crm.lead').create(cr, uid,{'state_change':'tsr','callback_state':'close','batch_code':int(self.browse(cr, uid, context['id'], context).s_batch_code),'contact_persion': row[0],'phone':row[1],'street':row[2],'street2':row[3],'monthly_income':float(row[5]) if row[5] else 0.0,'name':row[4],'disposition_status':12,'subdisposition_status':53,'mobile':row[6],'email_id':row[7],'birth_date':dob,'id_card_no':row[9],'company_name':row[10],'designation':row[11],'city':row[12],'gender':row[13],'exprience':row[14],'education_institution':row[15],'degree':row[16],'x_district':row[17],'x_industry':row[18],'company_street':row[19],'sales_team_r':assigned_tsr,'campaign_team':int(context['select_campaign']),'quality_asur':var_qa_group,'team_lead':var_tl_group,'quality_doc_group':var_qa_doc_group,'sales_admin':var_sa_group,'financial_p_conlt':var_fpc_de_group,'sale_team_name':int(context['select_sales_team']),'sales_mngr':pm_group}, context=None)
                                if(row_pointer == (int(nol[tsr_var])+cur_pos_pointer)):
                                    cur_pos_pointer = (row_pointer)
                                    _logger.error(":::::::::::::%s",cur_pos_pointer)
                                    break
                        elif(bol):
                            if(gate_stat is False):
                                dstv_lead = t_Rows/len(nol)
                                lead_reminder = dstv_lead%len(nol)
                                boundary = (dstv_lead*len(nol))
                                row_left = t_Rows - boundary
                                to = boundary+row_left
                                gate_stat = True
                            if (row_pointer > cur_pos_pointer   and  row_pointer <=(dstv_lead+cur_pos_pointer)  ):
                                _logger.error(str(row)+'______________________________________________________________'+str(assigned_tsr))
                                _logger.error(row[0])
                                _logger.error(row[1])
                                self.pool.get('rb.crm.lead').create(cr, uid,{'state_change':'tsr','callback_state':'close','batch_code':int(self.browse(cr, uid, context['id'], context).s_batch_code),'contact_persion': row[0],'phone':row[1],'street':row[2],'street2':row[3],'monthly_income':float(row[5]) if row[5] else 0.0,'name':row[4],'disposition_status':12,'subdisposition_status':53,'mobile':row[6],'email_id':row[7],'birth_date':dob,'id_card_no':row[9],'company_name':row[10],'designation':row[11],'city':row[12],'gender':row[13],'exprience':row[14],'education_institution':row[15],'degree':row[16],'x_district':row[17],'x_industry':row[18],'company_street':row[19],'sales_team_r':assigned_tsr,'campaign_team':int(context['select_campaign']),'quality_asur':var_qa_group,'team_lead':var_tl_group,'quality_doc_group':var_qa_doc_group,'sales_admin':var_sa_group,'financial_p_conlt':var_fpc_de_group,'sale_team_name':int(context['select_sales_team']),'sales_mngr':pm_group}, context=None)
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
                    self.pool.get('rb.crm.lead').create(cr, uid,{'state_change':'tsr','callback_state':'close','batch_code':int(self.browse(cr, uid, context['id'], context).s_batch_code),'contact_persion': row[0],'phone':row[1],'street':row[2],'street2':row[3],'monthly_income':float(row[5]) if row[5] else 0.0,'name':row[4],'disposition_status':12,'subdisposition_status':53,'mobile':row[6],'email_id':row[7],'birth_date':dob,'id_card_no':row[9],'company_name':row[10],'designation':row[11],'city':row[12],'gender':row[13],'exprience':row[14],'education_institution':row[15],'degree':row[16],'x_district':row[17],'x_industry':row[18],'company_street':row[19],'sales_team_r':random.choice(lst_tsr_id),'campaign_team':int(context['select_campaign']),'quality_asur':var_qa_group,'team_lead':var_tl_group,'quality_doc_group':var_qa_doc_group,'sales_admin':var_sa_group,'financial_p_conlt':var_fpc_de_group,'sale_team_name':int(context['select_sales_team']),'sales_mngr':pm_group}, context=None)
            if(peak):
                row = kalibabu[-1]
                self.pool.get('rb.crm.lead').create(cr, uid,{'state_change':'tsr','callback_state':'close','batch_code':int(self.browse(cr, uid, context['id'], context).s_batch_code),'contact_persion': row[0],'phone':row[1],'street':row[2],'street2':row[3],'monthly_income':float(row[5]) if row[5] else 0.0,'name':row[4],'disposition_status':12,'subdisposition_status':53,'mobile':row[6],'email_id':row[7],'birth_date':dob,'id_card_no':row[9],'company_name':row[10],'designation':row[11],'city':row[12],'gender':row[13],'exprience':row[14],'education_institution':row[15],'degree':row[16],'x_district':row[17],'x_industry':row[18],'company_street':row[19],'sales_team_r':lst_tsr_id[0],'campaign_team':int(context['select_campaign']),'quality_asur':var_qa_group,'team_lead':var_tl_group,'quality_doc_group':var_qa_doc_group,'sales_admin':var_sa_group,'financial_p_conlt':var_fpc_de_group,'sale_team_name':int(context['select_sales_team']),'sales_mngr':pm_group}, context=None)


            rd.close()
        
        return True
                     
                
    _columns = {
                'select_campaign': fields.many2one('rb.campaign.crm', 'Select Campaign',required=True),
                'select_sales_team' : fields.many2one('rb.sales.team', 'Select Sales Team',domain="[('campaign_name_id','=',select_campaign)]",required=True),
                'select_tsr':fields.text('Sales Team'),
                'data':fields.binary('File',filters='*.csv'),
                'auto_distribute':fields.boolean('Auto assign'),
                'relation_with_leadmap' : fields.one2many('user.lead.mapping', 'reference_with_ldist', 'Dependents'),
                's_batch_code' : fields.many2one('rb.crm.batch.code','Batch',required=True),
		'state' : fields.char('State'),
                'upload_date' : fields.datetime('Uplaod Date'),
                'quantity' : fields.integer('Quantity'),
                'database_name':fields.char('Database Name'),
                'batch_id':fields.char('Batch ID')
            }
    _defaults = {'upload_date': date.today().strftime('%Y-%m-%d')}
    
get_tsr_list()



class user_lead_mapping(osv.osv):
    _name='user.lead.mapping'
    def unlink(self, cr, uid, ids, context=None):
        raise osv.except_osv(('warning'),('You cannot delete assigned record'))
        
    _columns = {
                'name' : fields.char('Title'),
                'tsr_name' : fields.many2one('res.users','TSR'),
                'no_of_lead' : fields.integer('No Of leads'),
                'batch_code' : fields.many2one('rb.crm.batch.code','Select Batch'),
                'reference_with_ldist' : fields.many2one('get.tsr.list','Reference To Lead Distribution'),

                }
    #_defaults = {'tsr_name': ''}
user_lead_mapping()
