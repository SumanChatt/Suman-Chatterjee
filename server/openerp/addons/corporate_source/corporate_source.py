from osv import fields, osv
import time
import urllib


AVAILABLE_STATES = [
	('new', 'Draft'),
	('inprogress','In Progress'),
	('reject', 'Reject'),
	('close', 'Close')
]

class corporate_source(osv.osv):
	_name = "corporate.source"
	_description = "COMPANY INFORMATION SHEET"

	def _getYear(self, cr, uid, context=None):
		""" Return Years from 2017 to 2025"""
		lst=[]
		toup=()
		for k in range(1990, 2026):
			toup=(str(k),str(k))
			lst.append(toup)
		return lst


	_columns ={
			'type' : fields.selection([('S','S'),('M','M'),('L','L'),('MEGA','MEGA')],'Type'),
			'sourcing_status' : fields.char('English', size=30, required=True),
			'estd_year' : fields.selection(_getYear, string='Estd Year', store=True),
			'name_of_the_company' : fields.char('Name Of the Company', size=30, required=True),
			'industry_type' : fields.char('Industry Type', size=30, required=True),
			'business_registration_no' : fields.integer('Business Registration No', size=30),
			'date_of_biz_registration' : fields.date('Date of Biz. Registration'),
			'tax_registration_no' : fields.integer('Tax Registration No.', size=30),
			'ho_addr1' : fields.char('Head office address 1', size=30, required=True),
			'ho_addr2' : fields.char('Head office address 2', size=30, required=True),
			'ward' : fields.char('Ward', size=30,),
			'city' : fields.char('City', size=30,),
			'province' : fields.char('Province', size=30,),
			'region' : fields.char('Region', size=30,),
			'telephone_number' : fields.integer('Telephone Number(s)', size=30),
			'fax_number' : fields.integer('Fax Number(s)', size=30),
			'general_email_id' : fields.char('General Email-ID', size=30,),
			'website_address' : fields.char('Website address', size=30, required=True),
			'key_contact_person_info' : fields.one2many('key.contact.person','corporate_id','Key Contact Person'),
			'branch_info' : fields.one2many('branch.details','corporate_id','Branch Details'),
			'facility_info' : fields.one2many('facility.details','corporate_id','Facility Details'),
			'account_info' : fields.one2many('account.details','corporate_id','Account Details'),
			'balance_sheet_info' : fields.one2many('balance.sheet.details','corporate_id','Balance Sheet Details'),
			'emp_profile_details' : fields.one2many('emp.profile.info','corporate_id','Employee Profile Details'),
			'share_holding_info' : fields.one2many('share.holding','corporate_id','Share-holding Information'),
			'state': fields.selection(AVAILABLE_STATES, 'State'),	
			}
	_defaults = {'state': 'new'}


	def set_inprogress(self,cr,uid,ids,context=None):
		self.write(cr, uid, ids, {'state':'inprogress'})
		return True
	def set_reject(self,cr,uid,ids,context=None):
		self.write(cr, uid, ids, {'state':'reject'})
		return True
	def set_close(self,cr,uid,ids,context=None):
		self.write(cr, uid, ids, {'state':'close'})
		return True


corporate_source()


class key_contact_person(osv.osv):
	""" Key Contact Person(s) Details """
	_name = "key.contact.person"
	
	_columns = {
					'name' : fields.char('Name', size=50),
					'designation' : fields.selection([('Chairman','Chairman'),('CEO','CEO'),('CFO','CFO'),('CHRO','CHRO'),('Union Secy','Union Secy'),('HR Mgr','HR Mgr'),('Supervisor','Supervisor')],'Position', size=50),
					'contact_number' : fields.integer('Contact Number',size=30),
					'email_id' : fields.char('Email-ID',size=30),
					'corporate_id' : fields.many2one('corporate.source'),
				}
key_contact_person()

class emp_profile_info(osv.osv):
	""" emp_profile_info Details """
	_name = "emp.profile.info"
	
	_columns = {
					'emp_profile' : fields.selection([('Senior Management (HNI)','Senior Management (HNI)'),('Management (AFF)','Management (AFF)'),('Middle Management (MA)','Middle Management (MA)'),('Supervisors','Supervisors'),('T. Leaders (UM)','T. Leaders (UM)'),('Officers (M)','Officers (M)')],'Emp. Profile'),
					'no_of_emp' : fields.integer('No. of Employees',size=30),
					'avg_salary' : fields.float('Average salary',size=30),
					'corporate_id' : fields.many2one('corporate.source'),
				}
emp_profile_info()

class share_holding(osv.osv):
	""" Share-holding Information """
	_name = "share.holding"
	
	_columns = {
					'type_key_mngt_personnel' : fields.selection([('Shareholder','Shareholder'),('Chief Executive Officer','Chief Executive Officer'),('HR Manager','HR Manager'),('Finance Manager','Finance Manager'),('Employee','Employee')],'Type Key Management Personnel', size=50),
					'name_of_the_share_holding' : fields.char('Name of the Share-holder', size=50),
					'no_of_share_holding' : fields.char('No. of Shares / % holding', size=50),
					'corporate_id' : fields.many2one('corporate.source'),
				}
share_holding()

class branch_details(osv.osv):
	""" Branch Details Information """
	_name = "branch.details"
	
	_columns = {
					'branch_province' : fields.char('Province', size=30, required=True),
					'branch_address' : fields.char('Address', size=30, required=True),
					'branch_employees' : fields.integer('No. of Employees', size=30, required=True),
					'corporate_id' : fields.many2one('corporate.source'),
				}
branch_details()

class facility_details(osv.osv):
	""" Facility Details Information """
	_name = "facility.details"

	def _getYear(self, cr, uid, context=None):
		""" Return Years from 1990 to 2026"""
		lst=[]
		toup=()
		for k in range(2010, 2026):
			toup=(str(k),str(k))
			lst.append(toup)
		return lst
	_columns = {
					'cic_max_group' : fields.char('CIC Max Grp', size=30, required=True),
					'facility' : fields.char('Facility', size=30, required=True),
					'year' : fields.selection(_getYear,'Year', size=30, required=True),
					'bank' : fields.char('Bank', size=30, required=True),
					'amount' : fields.integer('Amount', size=30, required=True),
					'type' : fields.char('Type', size=30, required=True),
					'status' : fields.char('Status', size=30, required=True),
					'corporate_id' : fields.many2one('corporate.source'),
				}
facility_details()

class account_details(osv.osv):
	""" Account Details Information """
	_name = "account.details"

	def _getYear(self, cr, uid, context=None):
		""" Return Years from 1990 to 2026"""
		lst=[]
		toup=()
		for k in range(1990, 2026):
			toup=(str(k),str(k))
			lst.append(toup)
		return lst
	_columns = {
					'financial' : fields.selection([('P&L','P&L'),('Revenues','Revenues'),('Expenses','Expenses'),('Profit','Profit'),('Tax','Tax'),('PAT','PAT')],'Financial', size=50),
					'amount' : fields.integer('Amount', size=30, required=True),
					'year' : fields.selection(_getYear,'Year', size=30, required=True),
					'corporate_id' : fields.many2one('corporate.source'),
				}
account_details()


class balance_sheet_details(osv.osv):
	"""Balance sheet Details Information """
	_name = "balance.sheet.details"

	def _getYear(self, cr, uid, context=None):
		""" Return Years from 1990 to 2026"""
		lst=[]
		toup=()
		for k in range(1990, 2026):
			toup=(str(k),str(k))
			lst.append(toup)
		return lst
	_columns = {
					'balance_sheet' : fields.selection([('Cash','Cash'),('Fixed','Fixed'),('Other','Other'),('Assets','Assets'),('Capital','Capital'),('Loans','Loans'),('Liabilities','Liabilities')],'Balance Sheet', size=50),
					'amount' : fields.integer('Amount', size=30, required=True),
					'year' : fields.selection(_getYear,'Year', size=30, required=True),
					'corporate_id' : fields.many2one('corporate.source'),
				}
balance_sheet_details()
