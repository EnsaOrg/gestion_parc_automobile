from odoo import models, fields, api

class ParcAutomobileOrdreMission(models.Model):
     _name = 'parc_automobile.ordreMission'

     autorisation = fields.Integer()
     permanence = fields.Boolean()
     deplacement = fields.Boolean()
     pointage = fields.Boolean()
     activite = fields.Selection([('administrative', 'Administrative'), ('logistique', 'Logistique'),
                                  ('commerciale', 'Commerciale'), ('autre', 'Autre')])