from openerp.osv import fields, osv
from openerp.tools.translate import _
import logging
import time
import os


_logger = logging.getLogger(__name__)

class power_dialer_wizard(osv.TransientModel):
	_name = "power.dialer.wizard"
	_columns = {
			'lead_ids': fields.one2many('power.dialer.wizard.reference', 'wizard_id', string='Leads'),
		}


	def default_get(self, cr, uid, fields, context=None):
		if context == None:
			context = {}
		lead_ids = context.get('active_ids', [])
		wiz_id = context.get('active_id', None)
		res = []
		lead_id=()
		lead_count=0
		leads = self.pool.get('rb.crm.lead').search(cr, uid, [('id', '=', lead_ids), 
																		('subdisposition_status', '=', 53)])
		# raise osv.except_osv(_('Warning!'),_(hr_holidays_ids))
		if not leads:
			raise osv.except_osv(_('Warning!'),_('Please select the New Leads!'))
		else:
			for lead in self.pool.get('rb.crm.lead').browse(cr, uid, leads, context=context):
				res.append((0, 0, {
				'wizard_id': wiz_id,
				'lead_id': lead.id,
				'name': lead.contact_persion,
				'mobile':int(lead.mobile),
				'disposition_status':int(lead.disposition_status),
				'subdisposition_status':int(lead.subdisposition_status),
				'state':lead.state,
				}))
		#raise osv.except_osv(('warning'),(res))
		return {'lead_ids': res}


	def start_power_dialer(self, cr, uid, id, context=None):
		wizard = self.browse(cr, uid, id, context=context)[0]
		line_ids = [lead.id for lead in wizard.lead_ids]
		self.pool.get('power.dialer.wizard.reference').start_power_dialer(cr, uid, line_ids, context=context)
		return True


class power_dialer_wizard_reference(osv.TransientModel):
	_name = "power.dialer.wizard.reference"
	_columns = {
		'wizard_id': fields.many2one('power.dialer.wizard', string='Wizard', required=True),
		'lead_id': fields.integer(string='Lead', required=True),
		'name': fields.char('Name', readonly=True),
		'mobile': fields.integer('Mobile',required=True),
		'disposition_status':fields.many2one('rb.crm.disposition','Disposition',change_default=True,required=True),
		'subdisposition_status':fields.many2one('rb.crm.sub.disposition','Sub Disposition',domain="[('disposition_status','=',disposition_status)]",required=True),
		'state': fields.char("State"),
	}

	def start_power_dialer(self, cr, uid, ids, context=None):
		#print('/007')
		#while True:
		for lead in self.browse(cr, uid, ids, context=context):
			self.pool.get('power.dialer.wizard.reference').start_call(cr, uid, lead, context=context)
			end_call()
			#self.write(cr, uid, ids, {'state': 'Hangup','disposition_status':False,'subdisposition_status':False})
			#os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % ( 300, 2000))
			#print('/007')
			#self.pool.get('rb.crm.lead').write(cr, uid, lead.lead_id.id, {'sale_team_name': int(lead.new_sales_team),'team_lead':lead.team_lead_id.id,'lead_ref_stat':True,'tsr_change_flag':True,'state_change': 'TL'})
			self.pool.get('power.dialer.log').create(cr, 1,{'ref_by':uid,'ref_tsr':uid,'ref_lead_id':lead.lead_id,'mobile':lead.mobile},context = context)
		return True

	def start_call(self, cr, uid, ids, context=None):
		mobile = context['mobilex']
		raise osv.except_osv(('Message'),(mobile))
		#raise osv.except_osv(('warning'),(res))


class power_dialer_log(osv.osv):
	_name = "power.dialer.log"
	_columns = {
		'ref_lead_id':fields.many2one('rb.crm.lead','Lead relation'),
		'mobile':fields.integer('Mobile'),
		'ref_tsr':fields.many2one('res.users','Tsr'),
		'ref_by': fields.many2one('res.users','Referred by'),
	}
power_dialer_log()




			






	
