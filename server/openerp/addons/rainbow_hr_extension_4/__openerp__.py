# -*- coding: utf-8 -*-
##############################################################################
#
#    Rose One (Rainbow), Custom Developement Solution
#    Copyright (C) 2013-2015 Rainbow Financial Services.
##############################################################################

{
    'name': 'Extended Employee Recruitment',
    #'version': '3',
    #'author': 'OpenERP SA, Rainbow Customised For Vietnam',
    'category': 'Human Resources Recruitment',
    #'sequence': 193,
    #'website': '',
    #'summary': ' Extended Fields, Additional Applicant Details',
    
    #'author': 'Rainbow Developers,Rainbow Customised',
    #'website': 'www.rainboworldwide.com',
    'depends': ['hr_recruitment'],
    'data': [
        'rb_hr_recruitment_view.xml',
        'security/rb_hr_security.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    #'application': True,
    #'auto_install': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
