from odoo import models, fields, api

class ParcAutomobileAchat(models.Model):
     _name = 'parc_automobile.achat'
     _inherit = "parc_automobile.acquisition"
     _description = "Hérite de la casse acquisition"

     matricule = fields.Char('Matricule')