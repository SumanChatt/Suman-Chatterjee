from openerp.osv import fields, osv

class default_hr_ed_extend(osv.osv):
    _inherit = 'hr.employee'

    def onchange_team_id(self, cr, uid, ids, team_id, context=None):
        value = {'parent_id': False}
        if team_id:
            team = self.pool.get('hr.team').browse(cr, uid, team_id)
            value['parent_id'] = team.manager_id.id
        return {'value': value}

    _columns = {
            'employee_number': fields.char('Code(Employee Code)', size=240,required=True),
            'branch': fields.char('Branch', size=32, readonly=False),
            'project': fields.char('Project', size=100),
            'rb_group': fields.many2one('hr.employee.groups','Group'),
            'team_id': fields.many2one('hr.team', 'Team'),
            'title1':fields.char('Job Title (VN)'),
            'p_payroll' : fields.boolean('Show Employee on Template'), ##Active Filter
            'issue_date':fields.date('Issue Date'),
            'issue_place':fields.char('Issue Place'),
            'bank_acc_id' :fields.many2one('hr.employee.bank.account', 'Bank Account', help="Employee bank salary account"),
            'otherid': fields.char('Bank', size=64),
            'origin' : fields.char('Origin'),
            'no_of_dependent': fields.integer('Number of dependent'),
            'mobile_ct' : fields.char('Cell No.'),
            'mob_oth' : fields.char('Other Ph No.'),
            'identification_sub':fields.char('No.Social Book'),
            'accidental_ins': fields.char('Accidental Insurance'),
            'medical_ins':fields.char('Medical Insurance'),
            'exp_date':fields.date('Expiry Date'),
            'pan_number':fields.char('Pancard Number'),
            'pf_id':fields.char('PIT Code'),
            'resign':fields.boolean('Resign'),
            'cv_cover_letter':fields.boolean('CV/Cover Letter'),
            'id_card_no':fields.boolean('ID CARD'),
            'house_hold':fields.boolean('House Hold Registration Book'),
            'centificate':fields.boolean('Centificate'),
            'health_check':fields.boolean('Health Check'),
            'picture':fields.boolean('Picture'),
            'fraud_prevantion':fields.boolean('Fraud Prevantion'),
            'criminal_background':fields.boolean('Criminal Background'),
            'offer_letter':fields.boolean('Offer Letter'),
            'probation_appraisal':fields.boolean('Probation Appraisal'),
            'labour_contract':fields.boolean('Labour Contract'),
            'services_contract':fields.boolean('Services Contract'),
            'transfer_form':fields.boolean('Transfer Form'),
            'disciplinary_action_form':fields.boolean('Disciplinary Action Form'),
            'registration_form':fields.boolean('Registration Form'),
            'hanover_minute':fields.boolean('Hanover Minute'),
            'clearance_form':fields.boolean('Clearance Form'),
            'terminate_dicision':fields.boolean('Terminate Dicision'),
            'agency_cnt':fields.boolean('Agency Contract'), 
            'free_cnt' :fields.boolean('Freelancer Contract'),
            'seasonal_contract' :fields.boolean('Seasonal Contract'),
            'performance_appraisal' : fields.boolean('Peformance Appraisal'),
            'resign_doc' : fields.binary('Resign documents'),
            'resign_date' : fields.datetime('Resign date'),
            'documents_provided' : fields.many2many('hr.after.regisn.documents','rel_provided_doc_2hr','hr_id','doc_id',string='Documents given to employee'),
            'mob_oth' : fields.char("Father's Name"),
        }
    _defaults = {
            'p_payroll':True,
            'employee_number':'EMP001',
    }
    _sql_constraints = [
            ('emp_id_uniq', 'unique(employee_number)', 'The Employee ID must be unique!'),
         ]
default_hr_ed_extend()
##**********************************************************************************************************************************************************
##**********************************************************************************************************************************************************
##**********************************************************************************************************************************************************
##**********************************************************************************************************************************************************
##**********************************************************************************************************************************************************
##**********************************************************************************************************************************************************
##**********************************************************************************************************************************************************
##**********************************************************************************************************************************************************
##**********************************************************************************************************************************************************
##**********************************************************************************************************************************************************
class hr_team(osv.osv):
    def name_get(self, cr, uid, ids, context=None):
        if context is None:
            context = {}
        if not ids:
            return []
        reads = self.read(cr, uid, ids, ['name','parent_id'], context=context)
        res = []
        for record in reads:
            name = record['name']
            if record['parent_id']:
                name = record['parent_id'][1]+' / '+name
            res.append((record['id'], name))
        return res

    def _team_name_get_fnc(self, cr, uid, ids, prop, unknow_none, context=None):
        res = self.name_get(cr, uid, ids, context=context)
        return dict(res)

    _name = "hr.team"
    _columns = {
        'name': fields.char('Team Name', size=64, required=True),
        'complete_name': fields.function(_team_name_get_fnc, type="char", string='Name'),
        'company_id': fields.many2one('res.company', 'Company', select=True, required=False),
        'parent_id': fields.many2one('hr.team', 'Parent Team', select=True),
        'child_ids': fields.one2many('hr.team', 'parent_id', 'Child Teams'),
        'note': fields.text('Note'),
        'manager_id':fields.many2one('hr.employee','Manager id(Optional)'),
    }

    _defaults = {
        'company_id': lambda self, cr, uid, c: self.pool.get('res.company')._company_default_get(cr, uid, 'hr.team', context=c),
                }

    def _get_members(self, cr, uid, context=None):
        mids = self.search(cr, uid, [('manager_id', '=', uid)], context=context)
        result = {uid: 1}
        for m in self.browse(cr, uid, mids, context=context):
            for user in m.member_ids:
                result[user.id] = 1
        return result.keys()

    def _check_recursion(self, cr, uid, ids, context=None):
        if context is None:
            context = {}
        level = 100
        while len(ids):
            cr.execute('select distinct parent_id from hr_team where id IN %s',(tuple(ids),))
            ids = filter(None, map(lambda x:x[0], cr.fetchall()))
            if not level:
                return False
            level -= 1
        return True

    _constraints = [
        (_check_recursion, 'Error! You cannot create recursive teams.', ['parent_id'])
    ]

hr_team()
##**********************************************************************************************************************************************************
##**********************************************************************************************************************************************************
##**********************************************************************************************************************************************************
##**********************************************************************************************************************************************************
##**********************************************************************************************************************************************************
##**********************************************************************************************************************************************************
##**********************************************************************************************************************************************************
##**********************************************************************************************************************************************************
##**********************************************************************************************************************************************************
##**********************************************************************************************************************************************************
class hr_employee_groups(osv.osv):

	_name = 'hr.employee.groups'

	_columns = {
			'name' : fields.char('Group name'),
			'description' : fields.text('About group'),
		}
hr_employee_groups()
##**********************************************************************************************************************************************************
##**********************************************************************************************************************************************************
##**********************************************************************************************************************************************************
##**********************************************************************************************************************************************************
##**********************************************************************************************************************************************************
##**********************************************************************************************************************************************************
##**********************************************************************************************************************************************************
##**********************************************************************************************************************************************************
##**********************************************************************************************************************************************************
##**********************************************************************************************************************************************************
class hr_employee_bank_account(osv.osv):

    _name = "hr.employee.bank.account"

    _columns = {
                    'name' : fields.char('Account Number'),
                    'account_type' : fields.selection([('Salary Account','Salary Account'),('Personal Account','Personal Account')],string='Account Type'),
                    'owner' : fields.many2one('hr.employee','Account Owner'),
                    'street' : fields.char('Address'),
                    'pin': fields.char('Zip'),
                    'city' : fields.char('City'),
                    'bank_name' : fields.char('Bank Name'),
                    'bic' : fields.char('Bank Identifier Code'),
                    'brnnm' : fields.char('Branch Name'),
           }
hr_employee_bank_account()
##**********************************************************************************************************************************************************
##**********************************************************************************************************************************************************
##**********************************************************************************************************************************************************
##**********************************************************************************************************************************************************
##**********************************************************************************************************************************************************
##**********************************************************************************************************************************************************
##**********************************************************************************************************************************************************
##**********************************************************************************************************************************************************
##**********************************************************************************************************************************************************
##**********************************************************************************************************************************************************
class hr_after_regisn_documents(osv.osv):
    _name = "hr.after.regisn.documents"
    _columns = {

                    'name' : fields.char('Documents provided'),
            }
hr_after_regisn_documents()

##class hr_job_extend(osv.osv):
##    _inherit = 'hr.job'
##    _columns = {
##
##                  'name': fields.char('Job Name', required=True, select=True,write=['base.group_hr_manager']),
##                  'no_of_recruitment': fields.integer('Expected New Employees', copy=False,help='Number of new employees you expect to recruit.',write=['base.group_hr_manager']),
##                  #'no_of_hired_employee': fields.integer('Hired Employees', copy=False, help='Number of hired employees for this job position during recruitment phase.'),
##                  'department_id': fields.many2one('hr.department', 'Department',write=['base.group_hr_manager']),
##                  'company_id': fields.many2one('res.company', 'Company',write=['base.group_hr_manager']),
##                  'user_id': fields.many2one('res.users', 'Recruitment Responsible', track_visibility='onchange',write=['base.group_hr_manager']),
##                  'color': fields.integer('Color Index',write=['base.group_hr_manager']),
##                  'address_id': fields.many2one('res.partner', 'Job Location', help="Address where employees are working",write=['base.group_hr_manager']),
##                  'survey_id': fields.many2one('survey.survey', 'Interview Form', help="Choose an interview form for this job position and you will be able to print/answer this interview from all applicants who apply for this job",write=['base.group_hr_manager']),
##                  'state': fields.selection([('open', 'Recruitment Closed'), ('recruit', 'Recruitment in Progress')],
##                                  string='Status', readonly=True, required=True,
##                                  track_visibility='always', copy=False,
##                                  help="By default 'Closed', set it to 'In Recruitment' if recruitment process is going on for this job position.",write=['base.group_hr_manager']),
##        
##        }
##hr_job_extend()
