# -*- coding: utf-8 -*-
##############################################################################
#
#    Rose One (Rainbow), Custom Developement Solution
#    Copyright (C) 2013-2015 Rainbow Financial Services.
##############################################################################

{
    "name" : "Rainbow Employee Profile Sheet",
    "description" : "Employee Profile Details",
    #'version': '3',
    #'author': 'Rainbow IT team',
    'category': 'Human Resources',
    #'sequence': 194,
    #'website': '',
    #'summary': ' Employee Profile sheet for individual employees',
    
    #'author': 'Rainbow Developers,Rainbow Customised',
    #'website': 'www.rainboworldwide.com',
    "depends" : ['base','web','hr'],
    "data": [
		'custom_employee_profile_view.xml',
		'security/ir.model.access.csv'
		
    ],
    'installable': True,
    #'application': True,
    #'auto_install': False,
}

