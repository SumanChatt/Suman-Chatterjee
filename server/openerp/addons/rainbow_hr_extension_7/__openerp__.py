# -*- coding: utf-8 -*-
{
    'name': "Rainbow HR Leave Extension",

    #'summary': """ HR Leave Extension For Rainbow Vietnam """,

    

    'category': 'Human Resources',
    #'version': '3.0',

    # any module necessary for this one to work correctly
    'depends': ['base','web','hr','hr_holidays','hr_contract'],

    # always loaded
    'data': [
        #'security/security.xml',
        #'security/ir.model.access.csv',
        #'templates.xml',
        'view/hrms_leave_extension.xml',
        
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo.xml',
    ],
    'installable' : True,
    #'js': ['static/src/js/*.js'],
    #'application': True,
}

