# -*- coding: utf-8 -*-

{
    "name" : "Rainbow Customer relationship management",
    "description" : "Customized Customer relationship management",
    "version" : "1.0",
    "depends" : ['base','web'],
    "category": "Rainbow CRM",
    "author" : "Rainbow IT",
    "url": "",
    "data": [
		'rb_crm_view.xml',
                'rb_crm_vfsr.xml',
                'vfsr_tl_entry_view.xml',
                'wizard/lead_reference_wizard_view.xml',
                'wizard/power_dialer_wizard_view.xml',
                'rb_soft_dialer_view.xml',
		'ir.model.access.csv'
    ],
    "installable" : True,
    'js': ['static/src/js/*.js'],
    'qweb' : ['static/src/xml/*.xml'],
    "active" : False
}

