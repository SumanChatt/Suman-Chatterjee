# encoding=utf8
from openerp.osv import fields, osv
from osv import fields, osv


class hr_employee_extension(osv.osv):

    _inherit = 'hr.employee'

    def name_get(self,cr,uid,ids,context=None):
        if context is None:
            context ={}
        res=[]
        record_name=self.browse(cr,uid,ids,context)
        if isinstance(record_name, list):
            for object in record_name:

                    if object.name:
                        res.append((object.id,object.name+" / "+object.employee_number))
                    else:
                        res.append((object.id,str(object.id)+" / "+object.employee_number))
        else:
            if record_name.name:
                res.append((record_name.id,record_name.name+" / "+record_name.employee_number))
            else:
                res.append((record_name.id,str(record_name.id)+" / "+record_name.employee_number))
            
        return res
hr_employee_extension()
class demand_contract_extension(osv.osv):

    _inherit = 'hr.contract'

    _columns = {
                'emp_x_code' :fields.related('employee_id', 'employee_number', type='char',  readonly=True, store=True, string='Employee ID'),
                
            }
demand_contract_extension()

