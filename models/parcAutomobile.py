from odoo import models, fields, api

class ParcAutomobileParcAutomobile(models.Model):
     _name = 'parc_automobile.parc_automobile'

     num_parc = fields.Integer()
     capacite = fields.Integer()
     localisation = fields.Text()

