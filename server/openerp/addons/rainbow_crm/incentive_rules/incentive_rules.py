from osv import fields, osv
import time

class incentive_rules(osv.osv):
    _name = "incentive_rules"
    _description = "Monthly Sale Data"
    _columns = {
            'slab_no' : fields.integer('SLAB NO'),
            'slab_name' : fields.char('SLAB NAME', size=256),
            'level_no' : fields.integer('Level NO'),
            'Month' : fields.char('MONTH', size=30),
            'Year' : fields.char('YEAR', size=30),
            'location' : fields.char('LOCATION', size=256),
            'project' : fields.char('PROJECT', size=256),
            'role' : fields.char('ROLE', size=256),
            'team' : fields.char('Team', size=256),
            'contest' : fields.char('Contest', size=256),
            'product' : fields.char('PRODUCT', size=256),
            'product_rule' : fields.char('PRODUCT RULE', size=256),
            'mob_rule' : fields.char('MOB RULE', size=256),
            'scale_start' : fields.char('Scale Start', size=256),
            'scale_end' : fields.char('Scale End', size=256),
            'slab_type' : fields.char('SLAB TYPE', size=256),
            'inctv_with_ins' : fields.char('INCENTIVE WITH INS', size=256),
            'inctv_wo_ins' : fields.char('INCENTIVE WO INS', size=256),


                }

incentive_rules()
