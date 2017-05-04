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

class rb_tl_vfsr_meeting(osv.osv):
    _name = 'rb.tl.vfsr.meeting'

    def default_get(self, cr, uid, fields, context=None):
        data = super(rb_tl_vfsr_meeting, self).default_get(cr, uid, fields, context=context)
        data['supervisor']=uid
        return data

        

    

    _columns = {

                'supervisor':fields.many2one('res.users','Team Supervisor'),
                #'vfsr_team_id':fields.many2one('rb.vfsr.team','VFSR Team',change_default=True),
                #'vfsr': fields.many2one('res.users','VFSR'),
                'vfsr_line':fields.one2many('vfsr.apps.promised', 'rel2vfsr_meeting', 'VFSR Entries', ),
                'meeting_date': fields.date("Date"),
		'duration': fields.float("Duration (In Hours)"),
		'meeting_place':fields.char("Meeting Place"),

                #'aaps_promices':fields.integer("Apps Promised"),
                'remarks':fields.text('Remarks'),
}



class vfsr_apps_promised(osv.osv):
    _name = 'vfsr.apps.promised'
    def default_get(self, cr, uid, fields, context=None):
        data = super(vfsr_apps_promised, self).default_get(cr, uid, fields, context=context)
        data['supervisor']=uid
        return data


    _columns = {
                'supervisor':fields.many2one('res.users','Team Supervisor'),
                'vfsr_team_id':fields.many2one('rb.vfsr.team','VFSR Team',change_default=True),
                'vfsr_name': fields.many2one('res.users','VFSR',),
                'rel2vfsr_meeting': fields.many2one('rb.tl.vfsr.meeting','Relational Field'),
                'aap_promices':fields.integer("Apps Promised"),
                'remarks':fields.text('Remarks'),
            }
