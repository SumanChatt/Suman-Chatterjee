from openerp.osv import fields, osv
from openerp.tools.translate import _


class employee_profile_sheet_main(osv.osv):
	
	_name = "employee.profile.sheet.main"


        def create(self, cr, uid, values, context=None):
                #raise osv.except_osv(('warning'),(values['name']))
                #print 'Here Pointer'
                emp_id = int(values['name'])
                #print emp_id
                emp_grp = int(self.pool.get('hr.employee').browse(cr, uid, emp_id, context = context).rb_group)
                #print emp_id
                #print emp_grp
                #print "-x-x-x-x-x-x-x-x-x-x-x"
                #raise osv.except_osv(('warning'),(emp_grp))
                values['employee_group'] = emp_grp
                #print values
                return super(employee_profile_sheet_main, self).create(cr, uid, values, context)




                
	
	_columns = {

			'name' : fields.many2one('hr.employee','Employee Name'),
			'epsno2' : fields.char('EPS No'),
			'dateapplied3' : fields.date('Date Applied '),
			'datereceived4' : fields.date('Date Received'),
			'dateupdated5' : fields.date('Date Updated '),
			'firstname6' : fields.char('First Name'),
			'middlename17' : fields.char('Full name (VNM)'),
			'middlename28' : fields.char('Full name(ENG)'),
			'surname9' : fields.char('Surname'),
			'gender10' : fields.selection([(1,'Male'),(0,'Female')],'Gender'),
			'salutation11' : fields.char('Salutation'),
			'location12' : fields.char('Location'),
			'branch13' : fields.char('Branch'),
			'source14' : fields.char('Source'),
			'position15' : fields.char('Position'),
			'project16' : fields.char('Project'),
			'team17' : fields.char('Team'),
			'reference2address': fields.one2many('employee.profile.address','rela2emp_prof_main','Address'),
			'mobile136' : fields.char('Mobile 1'),
			'mobile237' : fields.char('Mobile 2'),
			'email138' : fields.char('Email 1'),
			'email239' : fields.char('Email 2'),
			'dob40' : fields.date('DOB'),
			'maritalstatus41' : fields.char('Marital Status'),
			'father42' : fields.char('Father '),
			'mother43' : fields.char('Mother'),
			'familybooknumber44' : fields.char('Family Book Number'),
			'siblings45' : fields.char('Siblings'),
			'sibling146' : fields.char('Sibling1'),
			'sibling247' : fields.char('Sibling2'),
			'children48' : fields.char('Children '),
			'child149' : fields.char('Child 1'),
			'gender50' : fields.selection([(1,'Male'),(0,'Female')],'Gender'),
			'child251' : fields.char('Child 2'),
			'gender52' : fields.selection([(1,'Male'),(0,'Female')],'Gender'),
			## Certificate and Work Experience
			'reference2education': fields.one2many('employee.profile.education','relation2emp_profile','Education'),
			'reference2job_profile' : fields.one2many('employee.profile.work.experience','rela2emp_prof','Work Experience'),
			'reference68' : fields.char('Reference Name'),
			'mobile70' : fields.char('Mobile'),
			'name71' : fields.char('Name'),
			'mobile72' : fields.char('Mobile'),
			'hobby173' : fields.char('Hobby1'),
			'hobby274' : fields.char('Hobby2'),
			'signature75' : fields.char('Signature'),
			'date76' : fields.date('Date '),
			# reference check
			'ref_chk_date' : fields.date('Reference Check Date'),
			'decesion': fields.selection([(1,'Pass'),(0,'Fail')],'Decesion'),
			'done_by': fields.many2one('hr.employee','Done By'),
			'type': fields.selection([(1,'Company'),(0,'Reference'),(2,'Family'),(3,'CIC')],'Type'),
			'person_contacted' : fields.text('Person Contacted'),
			'mobile_tel' : fields.char('Mobile/Tel'),
			'reference2questionans': fields.one2many('interview.question.answer','rel2e_prof','Question And Answer'),
			'conclusion' : fields.selection([(1,'Positive'),(0,'Negative')],'Conclusion'),
			'remarks': fields.text('Remarks'),
                        'employee_group': fields.many2one('hr.employee.groups','Groups',readonly=True),



		}
employee_profile_sheet_main()

## Education Profile

class employee_profile_education(osv.osv):

	_name = "employee.profile.education"
	_columns = {
			'name' : fields.char('Course Name'),
			'board' : fields.char('Board'),
			'institute' : fields.char('Institute Name'),
			'ins_location' : fields.char('Institute Location'),
			'year_from': fields.integer('From'),
			'year_to': fields.integer('To'),
			'reference2subjects' : fields.one2many('employee.profile.education.subject','relation2education','Subjects'),
			'relation2emp_profile' : fields.many2one('employee.profile.sheet.main','Employee reference Details',invisible="True")
			

		}
employee_profile_education()


## Class Subjects

class employee_profile_education_subject(osv.osv):

	_name = "employee.profile.education.subject"
	_columns = {
			'name': fields.char('Subject Name'),
			'total' : fields.float('Total Marks'),
			'obtain' : fields.float('Marks Obtain'),
			'relation2education' : fields.many2one('employee.profile.education','Employee Education',invisible="True")
		}
	_defaults = {'total': 100.0,'obtain':0.0}

employee_profile_education_subject()


##Job History

class employee_profile_work_experience(osv.osv):
	
	_name = "employee.profile.work.experience"
	_columns = {
			'name': fields.char('Job Role'),
			'company_name' : fields.char('Company Name'),
			'company_address' : fields.char('Company Address'),
			'company_phone' : fields.char('Company Phone Number'),
			'year_from': fields.integer('Working From'),
			'year_to': fields.integer('Working To'),
			'reference_2_ref' : fields.one2many('employee.profile.work.reference','relation2exp','Company Reference'),
			'rela2emp_prof' : fields.many2one('employee.profile.sheet.main','Employee reference Details',invisible="True")
			
		}
employee_profile_work_experience()


##Reference of previous company

class employee_profile_work_reference(osv.osv):

	_name = "employee.profile.work.reference"
	_columns = {
			'name' : fields.char('Reference Name'),
			'ref_address' : fields.char('Address'),
			'ref_cont' : fields.char('Cont. Number'),
			'ref_work' : fields.char('Company'),
			'ref_position' : fields.char('Position'),
			'relation2exp' : fields.many2one('employee.profile.work.experience','Work Experience',invisible="True")

		}
employee_profile_work_reference()


## Address

class employee_profile_address(osv.osv):
	
	_name = "employee.profile.address"
	_columns = {
			'name' : fields.selection([(1,'Permanent'),(0,'Temporary')],'Address Type'),
			'address1' : fields.char('Address1'),
			'address2' : fields.char('Address2'),
			'address3' : fields.char('Address3'),
			'ward' : fields.char('Ward'),
			'district' : fields.char('District'),
			'city' : fields.char('City'),
			'mobile' : fields.char('Mobile'),
			'rela2emp_prof_main' : fields.many2one('employee.profile.sheet.main','Employee reference Details',invisible="True")
		}

employee_profile_address()


##interview questions and answer

class interview_question_answer(osv.osv):

	_name = "interview.question.answer"
	_columns = {
			'name': fields.char('Question'),
			'answer': fields.char('Answer'),
			'rel2e_prof' : fields.many2one('employee.profile.sheet.main','Employee reference Details',invisible="True")
		}
interview_question_answer()
