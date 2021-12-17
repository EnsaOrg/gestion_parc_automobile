from odoo import models, fields, api

class ParcAutomobileLocation(models.Model):
     _name = 'parc_automobile.location'
     # _inherit = "parc_automobile.acquisition"
     # _description = "Hérite de la classe acquisition"

     date = fields.Date('Date d\'acquisition')
     montant = fields.Float()
     motif = fields.Text('Address')
     #durée en heure
     duree = fields.Integer()

     fournisseur_id = fields.Many2one(comodel_name='parc_automobile.fournisseur', delegate=True, required=True)