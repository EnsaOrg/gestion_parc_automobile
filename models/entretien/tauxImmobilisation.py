from odoo import models, fields, api

class ParcAutomobileTauxImmobilisation(models.Model):
     _name = 'parc_automobile.tauxImmobilisation'
     _inherit = "parc_automobile.intervention"
     _description = "Hérite de la classe intervention"

     nbr_heure = fields.Integer()