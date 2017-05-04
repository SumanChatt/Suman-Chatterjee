from openerp.osv import fields, osv
from openerp.tools.translate import _

AVAILABLE_PRIORITIES = [
    ('6', 'Rejected'),
    ('5', 'Not Good'),
    ('4', 'On Average'),
    ('3', 'Good'),
    ('2', 'Very Good'),
    ('1', 'Excellent')
]



class default_hr_applicant_extend(osv.osv):
    _inherit = 'hr.applicant'

    def create_employee_from_applicant(self, cr, uid, ids, context=None):
        if context is None:
            context = {}
        hr_employee = self.pool.get('hr.employee')
        model_data = self.pool.get('ir.model.data')
        act_window = self.pool.get('ir.actions.act_window')
        emp_id = False
        for applicant in self.browse(cr, uid, ids, context=context):
            address_id = contact_name = False
            if applicant.partner_id:
                address_id = self.pool.get('res.partner').address_get(cr, uid, [applicant.partner_id.id], ['contact'])['contact']
                contact_name = self.pool.get('res.partner').name_get(cr, uid, [applicant.partner_id.id])[0][1]
            if applicant.job_id and (applicant.partner_name or contact_name) and applicant.emp_id_bck:
                applicant.job_id.write({'no_of_hired_employee': applicant.job_id.no_of_hired_employee + 1})
                create_ctx = dict(context, mail_broadcast=True)
                emp_id = hr_employee.create(cr, uid, {'name': applicant.partner_name or contact_name,
                                                     'job_id': applicant.job_id.id,
                                                     'address_home_id': address_id,
                                                     'department_id': applicant.department_id.id or False,
                                                     'address_id': applicant.company_id and applicant.company_id.partner_id and applicant.company_id.partner_id.id or False,
                                                     'work_email': applicant.department_id and applicant.department_id.company_id and applicant.department_id.company_id.email or False,
                                                     'work_phone': applicant.department_id and applicant.department_id.company_id and applicant.department_id.company_id.phone or False,
                                                     'employee_number': applicant.emp_id_bck
                                                     }, context=create_ctx)
                self.write(cr, uid, [applicant.id], {'emp_id': emp_id}, context=context)
                self.pool['hr.job'].message_post(
                    cr, uid, [applicant.job_id.id],
                    body=_('New Employee %s Hired') % applicant.partner_name if applicant.partner_name else applicant.name,
                    subtype="hr_recruitment.mt_job_applicant_hired", context=context)
            else:
                raise osv.except_osv(_('Warning!'), _('You must define an Applied Job and a Contact Name and Employee id for this applicant.'))
                #raise osv.except_osv(('Warning!'), ('Erreur  name_test  You must define an Applied Job and a Contact Name for this applicant.' ) )
            action_model, action_id = model_data.get_object_reference(cr, uid, 'hr', 'open_view_employee_list')
            dict_act_window = act_window.read(cr, uid, [action_id], [])[0]
            if emp_id:
                dict_act_window['res_id'] = emp_id
            dict_act_window['view_mode'] = 'form,tree'
            return dict_act_window
	


    _columns = {
                'type_id': fields.many2one('hr.recruitment.degree', 'Last Qualification'),
		'cv':fields.binary("Applicant's Document(s) Softcopy"),
		'emp_id_bck':fields.char('Employee ID',help="Assign Employee ID before Creating Employee"),
		'app_stage_sum' : fields.one2many('recruitment.satgewise.summery','relation2application','Application Summary'),
		'skill_quali_summery' : fields.one2many('qualification.details','ref2application','Skill and Qualification'),
		}
    #_defaults = {'active': True}

default_hr_applicant_extend()

class applicant_category(osv.osv):
    """ Category of applicant """
    _name = "hr.applicant_category"
    _description = "Category of applicant"
    _columns = {
        'name': fields.char('Name', size=64, required=True, translate=True),
    }

class recruitment_satgewise_summery(osv.osv):
	"""  Recruitment State Summery """
	_name = "recruitment.satgewise.summery"
	_columns = {
				'name' : fields.many2one('hr.recruitment.stage','Stage'),
				'interviewer' : fields.many2one('hr.employee','Interviewer'),
				'next_action_date' : fields.date('Next Action Date'),
				'action_details' : fields.char('Action Details'),
				'stagewise_appreciation':fields.selection(AVAILABLE_PRIORITIES, 'Appreciation'),
				'note' : fields.char('Details'),
				'relation2application' : fields.many2one('hr.applicant'),
		}
recruitment_satgewise_summery()

class qualification_details(osv.osv):
	""" Interviewee Qualification Details """
	_name = "qualification.details"
	
	_columns = {
					'name' : fields.selection([('Degree','Degree'),('Professional Training','Professional Training')],'Type'),
					'degree_type' : fields.many2one('hr.recruitment.degree','Name of Course'),
					'area' : fields.char('Area of Study'),
					'uvboard' : fields.char('Institute/University/Board'),
					'address' : fields.char('Address'),
					'ref2application' : fields.many2one('hr.applicant'),
				}
qualification_details()

