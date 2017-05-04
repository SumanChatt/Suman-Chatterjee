from openerp.osv import fields, osv
from openerp.tools.translate import _


class contract_policy(osv.osv):

	_name = 'contract.policy'
	_columns = {
			'name' : fields.char('Policy name'),
			'job' : fields.many2one('hr.job','Position'),
			'probation' : fields.boolean('Probation'),
			'term' : fields.float('Term in months'),
			'rate' : fields.float('Rate in %'),
			'pit' : fields.float('Tax in %'),
			'prob_working_days' : fields.char('Probation work days'),
			'contract' : fields.many2one('contract.details','Policy Type'),
			'work_days' : fields.char('General working days'),
			'note' : fields.text('Note')
		}
contract_policy()

class contract_details(osv.osv):

	_name = "contract.details"
	_columns = {
			'name' : fields.char('Abbreviation'),
			'det' : fields.char('Name'),
			'term' : fields.integer('Term in months'),
			'rate' : fields.float('Rate in %'),
			'pit' : fields.float('Tax in %'),
		}
contract_details()

class generic_contract_extend(osv.osv):

        _inherit = 'hr.contract'
        
        _columns = {
                        'policy_relations':fields.many2one('contract.policy','Policy'),
						'contract_history' : fields.one2many('m2o.emp.conttype', 'relation_with_contract', 'Contract History')
                }
generic_contract_extend()



class m2o_emp_conttype(osv.osv):

	_name = "m2o.emp.conttype"
	_columns = {
				'name' : fields.char('Contract Code'),
				'contract_type' : fields.many2one('hr.contract.type','Contract Type'),
				'contract_from': fields.date('Contract Form'),
				'contract_to' : fields.date('Contract To'),
				'remarks':fields.char('Remarks'),
				'relation_with_contract' :fields.many2one('hr.contract'),
			}
m2o_emp_conttype()

