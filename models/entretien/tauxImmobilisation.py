from odoo import models, fields, api

class ParcAutomobileTauxImmobilisation(models.Model):
     _name = 'parc_automobile.taux_immobilisation'
     # _inherit = "parc_automobile.intervention"
     # _description = "Hérite de la classe intervention"

     date = fields.Date('Date d\'acquisition')
     montant_frais = fields.Float()
     prestataire = fields.Char()
     duree = fields.Integer()
     nbr_heure = fields.Integer()

     vehicule_id = fields.Many2one(comodel_name='parc_automobile.vehicule', delegate=True, required=True)