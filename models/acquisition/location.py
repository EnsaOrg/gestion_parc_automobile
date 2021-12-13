from odoo import models, fields, api

class ParcAutomobileLocation(models.Model):
     _name = 'parc_automobile.location'

     #durée en heure
     duree = fields.Integer()