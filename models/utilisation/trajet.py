from odoo import models, fields, api

class ParcAutomobileTrajet(models.Model):
     _name = 'parc_automobile.trajet'

     isRecurrent = fields.Boolean()
     distance = fields.Integer()

     ordreMission_ids = fields.One2many(comodel_name='parc_automobile.ordreMission', inverse_name='trajet_id')