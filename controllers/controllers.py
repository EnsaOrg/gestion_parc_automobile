# -*- coding: utf-8 -*-
from odoo import http

# class ParcAutomobile(http.Controller):
#     @http.route('/parc_automobile/parc_automobile/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/parc_automobile/parc_automobile/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('parc_automobile.listing', {
#             'root': '/parc_automobile/parc_automobile',
#             'objects': http.request.env['parc_automobile.parc_automobile'].search([]),
#         })

#     @http.route('/parc_automobile/parc_automobile/objects/<model("parc_automobile.parc_automobile"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('parc_automobile.object', {
#             'object': obj
#         })