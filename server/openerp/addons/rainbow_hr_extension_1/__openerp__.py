# -*- coding: utf-8 -*-
##############################################################################
#
#    Rose One (Rainbow), Custom Developement Solution
#    Copyright (C) 2013-2015 Rainbow Financial Services.
#
##############################################################################

{
    'name': 'Extended Employee Directory',
    'category': 'Human Resources',
    'website': '',
    'depends': ['hr'],
    'data': [
        'rb_hr_view.xml',
        'security/rb_hr_security.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'active' : False
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
