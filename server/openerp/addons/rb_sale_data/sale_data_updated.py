from osv import fields, osv
import time

class rb_sale_data(osv.osv):
    _name = "rb_sale_data"
    _description = "Updated Sale Data"
    _columns = {
            'project': fields.char('Project', size=256),
            'location' : fields.char('Location', size=256),
            'unit_head_pm' : fields.char('Unit Head PM', size=256),
            'team_name' : fields.char('Team Name', size=256),
            'team_leader_code' : fields.char('Team Leader Code', size=256),
            'team_leader' : fields.char('Team Leader', size=256),
            'application_serial' : fields.char('Application Serial', size=256),
            'status' : fields.char('Status', size=256),
            'status_date' : fields.date('Status Date'),
            'customer_name' : fields.char('Customer Name', size=256),
            'gender' : fields.char('Gender', size=256),
            'age' : fields.char('Age', size=256),
            'id_no' : fields.char('ID No', size=256),
            'company_name' : fields.char('Company Name', size=256),
            'contact_no' : fields.char('Contact No', size=256),
            'email_id' : fields.char('Email ID', size=256),
            'monthly_income' : fields.char('Monthly Income', size=256),
            'sale_code_bank_side' : fields.char('Sale Code Bank Side', size=256),
            'rainbow_code' : fields.char('Rainbow Code', size=256),
            'tsr_vfsr_name' : fields.char('TSR VFSR Name', size=256),
            'fpc_code' : fields.char('FPC Code', size=256),
            'fpc_name' : fields.char('FPC Name', size=256),
            'product' : fields.char('Product', size=256),
            'with_without_insurance' : fields.char('With Without Insurance', size=256),
            'credit_card_type' : fields.char('Credit Card Type', size=256),
            'loan_amount_fyp' : fields.char('Loan Amount FYP', size=256),
            'mis_date' : fields.date('Mis Date'),

                }

rb_sale_data()
