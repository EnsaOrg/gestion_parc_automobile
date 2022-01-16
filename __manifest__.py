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
        'views/vehicule_views.xml',
        'views/modele_views.xml',
        'views/marque_views.xml',
        'views/assurance_views.xml',
        'views/parc_automobile_views.xml',
        'views/achat_views.xml',
        'views/assurance_views.xml',
        'views/conducteur_views.xml',
        'views/entretien_views.xml',
        'views/fournisseur_views.xml',
        'views/location_views.xml',
        'views/ordre_mission_views.xml',
        'views/parc_automobile_views.xml',
        'views/taux_immobilisation_views.xml',
        'views/trajet_views.xml',
        'views/visite_technique_views.xml',
        'views/affectation_views.xml',
        'models/utilisation/data/sequence.xml',
        'models/data/parc_sequence.xml'
        # 'views/intervention_views.xml',
        # 'views/acquisition_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': 'true',
}