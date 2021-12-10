# -*- coding: utf-8 -*-
{
    'name': "parc_automobile",

    'summary': """
        Gestion de parc automobile
    """,

    'description': """
        Ce module permet de gérer le parc automobile communal à travers une base de données patrimoine et des modules des procédures qui l'alimentent et la mettent à jour.
    """,

    'author': "Ambroise Ngagne TINE & Festus Philippe Sendze Ndjounouga",
    'website': "www.myTown.ma",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Town management',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': 'true',
}