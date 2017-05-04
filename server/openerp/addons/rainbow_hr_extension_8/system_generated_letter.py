from osv import fields, osv
from openerp.osv import fields, osv


class LaborContract(osv.osv):
    _name = 'rb.hr.labour.contract'
    
    _description = 'RoseOne Labour Contract'





    _columns = {

                    'name' : fields.char('OfferLetter Number',required=True),
                    'employer'  : fields.many2one("hr.employee", "Employer", required=True, ), #
                    'employer_designation': fields.related('employer', 'job_id', type='many2one', string='Employer Designation', readonly=True, relation="hr.job",store=True,),
                    'employer_nationality' : fields.related('employer', 'country_id', type='many2one', string='Employer Nationality', readonly=True, relation="res.country",store=True,),
                    'employee' : fields.many2one("hr.employee", "Employee Name", required=True, ),#
                    'employee_nationality': fields.related('employee', 'country_id', type='many2one', string='Employee Nationality', readonly=True, relation="res.country",store=True,),
                    'employee_designation' : fields.related('employee', 'job_id', type='many2one', string='Employee Designation', readonly=True, relation="hr.job",store=True,),
                    'employee_dob' : fields.related('employee', 'birthday', type='date', string='Employee Date Of Birth',store=True, readonly=True,),
                    'employee_place_of_birth' : fields.related('employee', 'place_of_birth', type='char', string='Place Of Birth',store=True, readonly=True,),
                    'employee_address' : fields.related('employee', 'address_home_id', type='many2one', string='Employee Address', readonly=True, relation="res.partner",store=True,),
                    'employee_idc_no'  : fields.related('employee', 'identification_id', type='char', string='ID Card Number',store=True, readonly=True,),
                    'employee_idc_issue' : fields.related('employee', 'issue_date', type='date', string='Issue Date',store=True, readonly=True,),
                    'employee_idc_issue_plc' : fields.related('employee', 'issue_place', type='char', string='Issue Place',store=True, readonly=True,),
                    'contract_period' :  fields.selection([('1', '1'), ('2', '2'),('3', '3'),('4', '4'),('5', '5'),('6', '6'), ],"Contract Period", required=True, ),
                    'contract_from_date' : fields.date("From", required=True, ),
                    'contract_to_date' :fields.date("To", required=True, ),
                    'employee_wage' : fields.float("Basic Wage",  required=True,),
                    'payment_type' : fields.selection([('banktransfer', 'Bank Transfer'), ('cashinhand', 'Cash In hand'), ], "Payment Type",required=True, ),
                    'sign_in_day' :  fields.date("Sign date", required=True, ),
                    'sign_employer' : fields.many2one("hr.employee", "Signature", required=True, ),
                    'change_state' :  fields.integer("Change State", required=False,),
        }
    _defaults = {'change_state': 1} 
LaborContract()
#######################################################################################################################

class LabourContractTerminationAgreement(osv.osv):
    _name = 'rb.hr.labor.termination'
    
    _description = 'Labour Termination From'


    _columns = {
                'name' : fields.char('Letter No.',required=True),
                'dated' :  fields.date("Dated", required=True, ),
                'terminate_employee_name' :  fields.many2one("hr.employee", "Employee", required=True, ),
                'terminate_employee_des' : fields.related('terminate_employee_name', 'job_id', type='many2one', string='Employee Designation', readonly=True, relation="hr.job",store=True,),
                'contract_terminate_day' :  fields.date("Contract Termination", required=True, ),
                'payments_till' :  fields.date("Receive Salary Until ", required=True, ),
                'handing_over' : fields.char("Company SI, HI, UI Pay", required=True, ),
                'employer' : fields.many2one("hr.employee", "Employer", required=True, ),
                'employee' : fields.many2one("hr.employee", "Employee", required=True, ),
                'signed_on' : fields.date("Signed on", required=True, ),
                'alternate_payments_till' : fields.date("Being Paid to", required=False, ),
                'change_state' :  fields.integer(string="Change State", required=False, ),
                
        }
    _defaults = {'change_state': 1}
LabourContractTerminationAgreement()
#######################################################################################################################

class OfferLetter(osv.osv):
    _name = 'rb.hr.offer.letter'
    
    _description = 'Offer Letter Generation'


    _columns = {
            'name' : fields.char('Offer-Letter Reference Number',required=True, ),
            'date' : fields.date("Date", required=True, ),
            'employee_name' : fields.many2one("hr.employee", "Employee Name", required=True, ),
            'position' : fields.related('employee_name', 'job_id', type='many2one', string='Employee Designation', readonly=True, relation="hr.job",store=True,),
            'start_date' : fields.date("Joining Date", required=True, ),
            'compensation'  :fields.char("Compensation", required=True, ),
            'employer_sign' :fields.many2one("hr.employee", "Sincerely", required=True, ),
            'change_state' :  fields.integer("Change State", required=False,),
    }
    _defaults = {'change_state': 1,'name':'RB-OL-RF-'}
OfferLetter()
#######################################################################################################################

class AgencyContractCb(osv.osv):
    _name = 'rb.hr.agency.contract.cb'
    
    _description = 'Agency Contract Citi-Bank Format'




    _columns = {

            'name' : fields.char("Contract reference Number",required=True,),
            'contract_est_date'  : fields.date("Contract Established Date", required=True, ),
            'employee_name'  : fields.many2one("hr.employee", "Employee/Candidate", required=True, ),
            'employee_dob'  : fields.related('employee_name', 'birthday', type='date', string='Date Of Birth',store=True, readonly=True,),
            'id_card'  : fields.related('employee_name', 'identification_id', type='char', string='ID Card Number',store=True, readonly=True,),
            'issued_on' : fields.related('employee_name', 'issue_date', type='date', string='Issue Date',store=True, readonly=True,),
            'employee_address' : fields.related('employee_name', 'address_home_id', type='many2one', string='Employee Address', readonly=True, relation="res.partner",store=True,),
            'agreement_vnd' : fields.char("Support Fixed VND", required=True, ),
            'issue_place' :  fields.related('employee_name', 'issue_place', type='char', string='Issue Place',store=True, readonly=True,),
            'change_state' :  fields.integer("Change State", required=False,)
        }
    _defaults = {'change_state': 1,'name':'RB-AGC-RF-'}
AgencyContractCb()
#######################################################################################################################

class PromotionalLetter(osv.osv):
    _name = 'rb.hr.promotion.letter'

    _description = 'Promotion Letter Format'




    _columns = {

            'name' : fields.char("Promotion Reference Number",),
            'dated'  : fields.date(string="Dated", required=True, ),
            'employee' : fields.many2one("hr.employee", "Employee", required=True, ),
            'position'  : fields.related('employee', 'job_id', type='many2one', string='Past position', readonly=True, relation="hr.job",store=True,),
            'position_now' : fields.many2one("hr.job", "Position To", required=True, ),
            'effective_date'  : fields.date("Effective from", required=True, ),
            'change_state' :  fields.integer("Change State", required=False, ),
}
    _defaults = {'change_state': 1,'name':'RB-PL-RF-'}
PromotionalLetter()
#################################################################################################################################################################
class OfferLetterSales(osv.osv):
    _name = 'rb.offer.sales.letter'

    _description = 'Offer Letter Sales'


    _columns = {
        'name' : fields.char("Reference Serial",store=True),
        'employee' : fields.many2one("hr.employee", "Employee", required=True,),
        'cmnd' : fields.related('employee', 'identification_id', type='char', string='CMND',store=True, readonly=True,required=True,),
        'location' : fields.related('employee', 'address_home_id', type='many2one', string='Location', readonly=True, relation="res.partner",store=True,),
        'project' : fields.related('employee', 'project', type='char', string='Project',store=True, readonly=True,),
        'contract' : fields.many2one("hr.contract", "Select Contract", required=True, domain="[('employee_id','=',employee)]"),
        'dmgmt' : fields.related('employee', 'parent_id', type='many2one', string='Direct Management', readonly=True, relation="hr.employee",store=True,),
        'start_day' : fields.date("Print Date", required=False, ),
        'trial_work_from' : fields.related('contract', 'trial_date_start', type='date', string='From',store=True, readonly=True,),
        'trial_work_to' : fields.related('contract', 'trial_date_end', type='date', string='To',store=True, readonly=True,),
        'amount_vnd' : fields.related('contract', 'wage', type='date', string='Support Fixed',store=True, readonly=True,),
        }
    

    _defaults = {'name':'RB-OL-SLS-'}

OfferLetterSales()




