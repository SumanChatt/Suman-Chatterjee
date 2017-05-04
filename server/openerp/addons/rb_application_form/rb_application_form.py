from osv import fields, osv
from openerp.osv import fields, osv
import openerp
import psycopg2
from itertools import groupby
from operator import itemgetter
from openerp import addons
from openerp import netsvc
from openerp import tools
from openerp.osv import fields, osv
from openerp.tools.translate import _

class rb_application_form(osv.osv):

	_name = "rb.application.form"

	#Main fields of the application form.
	_columns = {
		 'lead_id':fields.many2one('rb.crm.lead', "Lead",domain="[('disposition_status','in',[17,18])]"),
		 'create_date': fields.datetime("Date Created"),
		 'create_uid' : fields.many2one('res.users',"Created By"),
		 'customer_name':fields.char("Customer Name",required=True),
		 'dob':fields.date("Date Of Birth"),
		 'id_number' :fields.char("ID Number"),
		 'application_serial':fields.integer("Application Serial"),
		 'gender' :fields.selection([('male','Male'),('female','Female')],'Gender'),
		 'email_address' :fields.char("Email address"),
		 'mobile_number' :fields.integer("Mobile Number",required=True),
		 'highest_education' :fields.char("Highest Education"),
		 'location' :fields.many2one('rb.city',"Location",required=True),
		 'district' :fields.char("District"),
		 'living_type' :fields.selection([('Own','Own'),('Rental','Rental'),('Relative House','Relative House'),('Others','Others')],'Type Of Living'),
		 'living_time' :fields.char("Living time at current address"),
		 'occupation' :fields.selection([('Salaried','Salaried'),('Business','Business'),('Retired','Retired'),('Others','Others')],'Occupation'),
		 'company_name' :fields.char("Name of company"),
		 'industry' :fields.char("Industry"),
		 'monthly_income' :fields.float('Monthly Income'),
		 'position' :fields.char("Position"),
		 'working_period' :fields.char("Working Period"),
		 'product': fields.many2one('product.catagories','Product',required=True),
		 'sub_product' :fields.many2one('new.product.registration','Sub Product',domain="[('product_type','=',product)]"),
		 'amount' :fields.char("Amount"),
		 'married_status' :fields.selection([('married','Married'),('single','Single'),('separated','Separated'),('widowd','Widowd')],'Marital Status'),
		 'spouse_name' :fields.char("Spouse Name"),
		 'spouse_email' :fields.char("Spouse Email"),
		 'spouse_mobile' :fields.integer("Spouse Mobile"),
		 'children_information' :fields.char("Children Information"),
		 'name_reference1' :fields.char("Name of 1st Reference"),
		 'email_reference1' :fields.char("Email of 1st Reference"),
		 'mobile_reference1' :fields.integer("Mobile of 1st Reference"),
		 'name_reference2' :fields.char("Name of 2nd Reference"),
		 'email_reference2' :fields.char("Email of 2nd Reference"),
		 'mobile_reference2' :fields.integer("Mobile of 2nd Reference"),
		 'disposition_code': fields.many2one('rb.crm.disposition',"Disposition",required=True),
		 'subdisposition_code': fields.many2one('rb.crm.sub.disposition',"Sub Disposition",domain="[('disposition_status','=',disposition_code)]",required=True),
		 'campaign_team':fields.many2one('rb.campaign.crm',"Campaign Name"),
		 'sales_team' :fields.many2one('rb.sales.team',"Sales Team",domain="[('campaign_name_id','=',campaign_team)]",required=True),
		 'date_of_application' :fields.datetime("Date of application sending to client"),
		 'from_mobile' : fields.integer("Mobile Id"),
		 'tl_name' : fields.many2one('res.users',"TL Name"),
		 'tsr_name' : fields.many2one('res.users',"TSR Name",domain="[('sales_team','=',sales_team)]"),
		 'vfsr_fsr_name' : fields.many2one('res.users',"VFSR/FSR Name",domain="[('sales_team','=',sales_team)]"),
		 'status_history' :fields.one2many('rb.application.form.history', 'related_id', string='Status History', ),
	}


	def get_lead_details(self,cr,uid,ids,field,context=None):
		if (field):
			try:
				result = self.pool.get('rb.crm.lead').read(cr, uid, field, ['contact_persion','mobile','birth_date','id_card_no','gender','email_id','city_id','x_district','monthly_income','company_name','marital_status','campaign_team','sale_team_name','disposition_status','subdisposition_status','sales_team_r'], context)
				val = {'customer_name': result['contact_persion'],'mobile_number': int(result['mobile']),'dob':result['birth_date'],
						'id_number': int(result['id_card_no']),'gender': result['gender'],'email_address': result['email_id'],
						'location': result['city_id'],'district': result['x_district'],'monthly_income': result['monthly_income'],
						'company_name': result['company_name'],'married_status': result['marital_status'],
						'campaign_team': result['campaign_team'],'sales_team': result['sale_team_name'],
						'disposition_code': result['disposition_status'], 'subdisposition_code': result['subdisposition_status'],'tsr_name': result['sales_team_r'],}
			except ValueError:#id_card_no is missing or contain string
				val = {'customer_name': result['contact_persion'],'mobile_number': int(result['mobile']),'dob':result['birth_date'],
						'id_number': int('0'),'gender': result['gender'],'email_address': result['email_id'],
						'location': result['city_id'],'district': result['x_district'],'monthly_income': result['monthly_income'],
						'company_name': result['company_name'],'married_status': result['marital_status'],
						'campaign_team': result['campaign_team'],'sales_team': result['sale_team_name'],
						'disposition_code': result['disposition_status'], 'subdisposition_code': result['subdisposition_status'],'tsr_name': result['sales_team_r'],}
				print('Please input a valid integer')
		return {'value':val}

		#Populate TL name after selecting the sales team.
	def get_tl_name(self, cr, uid,ids, team_id=False, context=None):
		if context is None:
			context = {}
		res={}
		if team_id:			
			cr.execute('select d.id from rb_sales_team a,rb_tl_team b,rb_tl_team_rel c,res_users d \
			 				where a.team_lead_group = b.id and b.id = c.tl_team_id and c.res_users_id = d.id and \
			 				a.active = true and a.id=%s',(team_id,))
			res_id=cr.fetchall()
			
			tl_id=[]
			if res_id:			
				for row in res_id:
					tl_id.append(row[0])
			res['domain'] = {'tl_name': [('id', 'in', tl_id)]}
		else:
			res['domain'] = {'tl_name': []}
		return res

		#Updated valid data
	def write(self, cr, uid, ids, values, context = None):
		obj_application_history = self.pool.get('rb.application.form.history')
		appo_form = self.pool.get('rb.application.form')
		ids = appo_form.search(cr, uid, [('id','=',ids[0])])
		var = appo_form.read(cr, uid, ids, ['lead_id','disposition_code','subdisposition_code','campaign_team','sales_team'], context)
		for r in var:
			if(r['disposition_code']==False or r['subdisposition_code']==False):
				raise osv.except_osv(('warning'),'Please update the valid lead')#Should be filled up
			if(r['lead_id']==False):
				lead='0'
			else:
				lead=r['lead_id']
			dis=r['disposition_code']
			subdis=r['subdisposition_code']
			campaign=r['campaign_team']
			sales=r['sales_team']
			#Insert the history data
			obj_application_history.create(cr, uid,{'user_name': uid,'lead_id': int(lead[0]),'disposition_code': dis[0],'subdisposition_code': subdis[0],'campaign_team': campaign[0],'sales_team': sales[0],'related_id':int(ids[0])}, context = context)
		res = super(rb_application_form,self).write(cr, uid, ids, values, context = context)
		return res


rb_application_form()

#History of application form.
class rb_application_form_history(osv.osv):

	_name = "rb.application.form.history"
	_columns = {
		'user_name':fields.many2one('res.users',"Created By"),
		'lead_id': fields.integer("Lead Id"),
		'disposition_code': fields.many2one('rb.crm.disposition',"Disposition Code"),
		'subdisposition_code': fields.many2one('rb.crm.sub.disposition',"Sub Disposition Code",domain="[('disposition_status','=',disposition_code)]"),
		'campaign_team':fields.many2one('rb.campaign.crm',"Campaign Name"),
		'sales_team' :fields.many2one('rb.sales.team',"Sales Team",domain="[('campaign_name_id','=',campaign_team)]"),
		'related_id':fields.many2one('rb.application.form', 'Blank reference',select=False), #Related Id with application form
	}
rb_application_form_history()
