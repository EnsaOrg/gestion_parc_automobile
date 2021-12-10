from odoo import models, fields, api

class ParcAutomobileAcquisition(models.Model):
     _name = 'parc_automobile.acquisition'

     date = fields.Date('Date d\'acquisition')
     montant = fields.Float()
     motif = fields.Text('Address')