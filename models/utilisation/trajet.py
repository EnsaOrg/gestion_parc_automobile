from odoo import models, fields, api

class ParcAutomobileTrajet(models.Model):
     _name = 'parc_automobile.trajet'

     isRecurrent = fields.Boolean()
     distance = fields.Integer()