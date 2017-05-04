# -*- coding: utf-8 -*-

{
    'name': 'Rainbow contract policy',
    #'version': '3',
    #'author': 'Rainbow IT',
    'category': 'Human Resources',
    #'sequence': 198,
    #'website': '',
    #'summary': ' Extended contract, Additional contract policy',
   
    #'author': 'Rainbow Developers,Rainbow Customised',
    #'website': 'www.rainboworldwide.com',
    "depends" : ['base','web','hr'],
    "data": [
		'rainbow_contract_policy_view.xml',
		'security/ir.model.access.csv',
		
		
    ],
    'installable': True,
    #'application': True,
    #'auto_install': False,
}

