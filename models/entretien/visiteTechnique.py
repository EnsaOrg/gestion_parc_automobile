from odoo import models, fields, api

class ParcAutomobileVisiteTechnique(models.Model):
     _name = 'parc_automobile.visite_technique'
     # _inherit = "parc_automobile.intervention"
     # _description = "Hérite de la classe intervention"

     date = fields.Date('Date d\'acquisition')
     montant_frais = fields.Float()
     prestataire = fields.Char()
     duree = fields.Integer()

     certificat = fields.Selection([('a', 'A'), ('s', 'S')])

     vehicule_id = fields.Many2one(comodel_name='parc_automobile.vehicule', delegate=True, required=True)