from openerp.osv import fields, osv

class default_hr_contract_extend(osv.osv):
    _inherit = 'hr.contract'
    _columns = {
                'wage': fields.float('Basic Salary', digits=(16,2), required=True, help="Proposed Salary of the employee"),
                'minimum_wage' : fields.float('Minimum wage'),
                'telephone_allowance' : fields.float('Telephone Allowance'),
                'fuel_allowance' : fields.float('Fuel Allowance'),
                'air_ticket_allowance' : fields.float('Air Ticket Allowance'),
                'gross_pay_india' : fields.float('Gross Pay'),
                'relocation_allowance' : fields.float('Relocation Allowance'),
                'housing_free_allowance' : fields.float('Housing Free Allowance'),
                'special_allow' : fields.float('Special Allowance'),
                'joining_date': fields.date('Joining Date'),
                'contact_code':fields.char('Contact Code'),
                'on_prob' : fields.boolean('Probation'),
                'probation_salary' : fields.float('Probation salary %'),
                'join_date' : fields.date('Join Date'),
                'wrk_al': fields.float('Work Allowance'),
                'lnch_alw': fields.float('Lunch Allowance'),
                'conv_allw' : fields.float('Conveynce'),
                'city_comp_allow' : fields.float('City Compensatory Allowance'),
                'lta_allow' : fields.float('Leave Traveling Allowance'),
                'meda_allow' : fields.float('Medical Allowance'),
                'wages' : fields.float('Wages'),
                'trial_date_start' : fields.date('Probation From Date'),
                'trial_date_end' : fields.date('Probation End Date'),
                'date_start': fields.date('Contract Time From', required=True),
                'date_end': fields.date('Contract End Date'),
				'active':fields.boolean("Active"),

                
            }
    _defaults = {'active': True}

default_hr_contract_extend()

