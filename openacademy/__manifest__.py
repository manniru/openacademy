# -*- coding: utf-8 -*-
{
    'name': "Module 08",

    'summary': """
        Academy module - module 08""",

    'description': """
        
    """,

    'author': "Odoos",
    'website': "http://www.odoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Academy',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        'security/academy_security.xml',
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/courses.xml',
        'views/sessions.xml',
        'views/partners.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}
