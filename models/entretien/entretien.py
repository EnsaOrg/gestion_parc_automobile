from odoo import models, fields, api

class ParcAutomobileEntretien(models.Model):
     _name = 'parc_automobile.entretien'
     # _inherit = "parc_automobile.intervention"
     # _description = "Hérite de la classe intervention"

     date = fields.Date('Date d\'acquisition')
     montant_frais = fields.Float()
     prestataire = fields.Char()
     duree = fields.Integer()

     type = fields.Selection([('entretien courant', 'Entretien courant'), ('révision', 'Révision'), ('réparation', 'Réparation'),])

     vehicule_id = fields.Many2one(comodel_name='parc_automobile.vehicule', delegate=True, required=True)