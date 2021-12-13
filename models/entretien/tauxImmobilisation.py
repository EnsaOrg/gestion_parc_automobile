from odoo import models, fields, api

class ParcAutomobileTauxImmobilisation(models.Model):
     _name = 'parc_automobile.taux_immobilisation'
     _inherit = "parc_automobile.intervention"
     _description = "Hérite de la classe intervention"

     nbr_heure = fields.Integer()