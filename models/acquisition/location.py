from odoo import models, fields, api

class ParcAutomobileLocation(models.Model):
     _name = 'parc_automobile.location'
     _inherit = "parc_automobile.location"
     _description = "Hérite de la classe acquisition"

     #durée en heure
     duree = fields.Integer()