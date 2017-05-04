#__author__ = 'Rainbow'
# -*- coding: utf-8 -*-
{
    'name': "Rainbow System Generated Letter Print",

    #'summary': """Official Letter Digitization Module""",

   

    #'author': "Rainbow Developers",
    #'website': "http://www.rainboworldwide.com",

    'category': 'Human Resource',
    #'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base','web','hr'],

    # always loaded
    'data': [
        #
        'security/security_access.xml',
        'security/ir.model.access.csv',
        'view/system_generated_letter_view.xml'
        
        #'report/hr_report_register.xml',
        #'report/labor_contract_layout.xml',
        #'report/labor_contract_termination_layout.xml',
        #'report/offer_letter_layout.xml',
        #'report/cb_agency_contract_layout.xml',
        #'report/promotion_letter_layout.xml',
        #'report/offer_letter_layout_sales.xml',

    ],
   
    'installable' : True,
    #'js': ['static/src/js/*.js'],
    #'application': True,
}

