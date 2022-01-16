from odoo import models, fields, api

class ParcAutomobileAcquisition(models.Model):
     _name = 'parc_automobile.acquisition'

     date = fields.Date('Date d\'acquisition')
     montant = fields.Float('Montant (en DH)')
     motif = fields.Text('Address')