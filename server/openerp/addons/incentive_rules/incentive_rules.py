from osv import fields, osv
import time

class incentive_rules(osv.osv):
    _name = "incentive_rules"
    _description = "Monthly Sale Data"
    _columns = {
            'slab_no' : fields.integer('SLAB NO'),
            'slab_name' : fields.char('SLAB NAME', size=256),
            'level_no' : fields.integer('Level NO'),
            'Month' : fields.selection([('01','01'),('02','02'),('03','03'),('04','04'),('05','05'),('06','06'),('07','07'),('08','08'),('09','09'),('10','10'),('11','11'),('12','12')],'Month'),
            'Year' : fields.selection([('2013','2013'),('2014','2014'),('2015','2015'),('2016','2016'),('2017','2017'),('2018','2018'),('2019','2019'),('2020','2020'),('2021','2021'),('2022','2022'),('2023','2023'),('2024','2024'),('2025','2025')],'Year'),
            'location' : fields.many2one('rb.city','Location'),
            'project' : fields.many2one('hr.project', 'Project'),
            'role' : fields.many2one('hr.position', 'Role'),
            'team' :  fields.many2one('hr.team','Team Name'),
            'type_of_rule' : fields.char('Type of rules', size=256),
            'product' : fields.char('PRODUCT', size=256),
            'product_rule' : fields.char('PRODUCT RULE', size=256),
            'mob_rule' : fields.char('MOB RULE', size=256),
            'scale_start' : fields.integer('Scale Start', size=256),
            'scale_end' : fields.integer('Scale End', size=256),
            'slab_type' : fields.char('SLAB TYPE', size=256),
            'inctv_with_ins' : fields.integer('INCENTIVE WITH INS', size=256),
            'inctv_wo_ins' : fields.integer('INCENTIVE WO INS', size=256),
        }
incentive_rules()
