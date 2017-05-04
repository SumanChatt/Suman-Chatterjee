# -*- coding: utf-8 -*-

{
    'name': 'Holiday management',
    #'version': '3',
    #'author': 'Rainbow IT',
    'category': 'Human Resources',
    #'sequence': 199,
    #'website': '',
    #'summary': ' manage holiday lists',
    
    #'author': 'Rainbow Developers,Rainbow Customised',
    #'website': 'www.rainboworldwide.com',
    "depends" : ['base','web','hr'],
    "data": [
		'holiday_list_view.xml',
		#'security/ir.model.access.csv',
		
    ],
    'installable': True,
    #'application': True,
    #'auto_install': False,
}

