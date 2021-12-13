from odoo import models, fields, api

class ParcAutomobileParcAutomobile(models.Model):
     _name = 'parc_automobile.parc_automobile'

     num_parc = fields.Integer()
     capacite = fields.Integer()
     localisation = fields.Text()

     #vehicule_ids = fields.One2many(comodel_name='parc_automobile.vehicule', inverse_name='parc_id')