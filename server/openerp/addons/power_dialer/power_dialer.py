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
class power_dialer(osv.osv):
    _name = 'power.dialer'

    def create(self, cr, uid, val, context = None):
        xab =  super(power_dialer,self).create(cr,uid,val,context)
        self.write(cr, uid, xab, {'state': 1})
        return xab

    def func_get_sales_team(self,cr,uid,ids,field_value,context=None):
        raise osv.except_osv(('warning'),(field_value))
        return True

    def func_get_tsr(self,cr,uid,ids,team_id=False,context=None):
       
        res = {'value': {'tsr_list': False}}
        if context is None:
            context = {}
        #raise osv.except_osv(('warning'),(campaign_id,team_id))
        var_lst = []
        res_user_obj = self.pool.get('res.users')
        if team_id:            
            cr.execute('select str.res_users_id from rb_sales_team_rel str,res_users usr where str.sales_team_id = %s and str.res_users_id = usr.id and usr.active is TRUE',(team_id,))
            tsr_id = cr.fetchall()
            for row in tsr_id:
                var_lst.append(int(row[0]))
            # raise osv.except_osv(('warning'),(var_lst))
            res['domain'] = {'tsr_list':  [('id', 'in', var_lst)]}
        return res

    def func_get_lead(self,cr,uid,campaign_id=False,team_id=False,tsr_id=False,context=None):
        raise osv.except_osv(('warning'),(campaign_id,team_id,tsr_id))
        res = {'value': {'tsr_list': False}}
        if campaign_id and team_id and tsr_id:         
            cr.execute('select count(*) from rb_crm_lead where campaign_team=%s and sale_team_name=%s and sales_team_r=%s',(campaign_id,team_id,tsr_id,))
            res_id=cr.fetchone()[0]            
            if res_id:          
                res['value'] = {'department_id': res_id}
        raise osv.except_osv(('warning'),(res))
        return res

    def disposition_onchange(self,cr,uid,ids,context=None):
        var_subdisposition = False
        val = {'subdisposition_status':var_subdisposition,'remarks':False}
        return {'value': val}

    _columns = {
                'campaign'  : fields.many2one('rb.campaign.crm', 'Select Campaign',required=True),
                'sale_team' : fields.many2one('rb.sales.team', 'Select Sales Team',domain="[('campaign_name_id','=',campaign)]",required=True),
                'tsr_list'  : fields.many2one('res.users','TSR List'),
                'disposition_status':fields.many2one('rb.crm.disposition','Disposition',change_default=True),
                'subdisposition_status':fields.many2one('rb.crm.sub.disposition','Sub Disposition',domain="[('disposition_status','=',disposition_status)]"),
                'state' : fields.boolean('State'),
                'quantity' : fields.integer('Quantity'),
            }
    
power_dialer()