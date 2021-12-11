from odoo import models, fields, api

class ParcAutomobileEntretien(models.Model):
     _name = 'parc_automobile.entretien'
     _inherit = "parc_automobile.intervention"
     _description = "Hérite de la classe intervention"

     type = fields.Selection([('entretien courant', 'Entretien courant'), ('révision', 'Révision'), ('réparation', 'Réparation'),])