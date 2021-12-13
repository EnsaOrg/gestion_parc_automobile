from odoo import models, fields, api

class ParcAutomobileEntretien(models.Model):
     _name = 'parc_automobile.entretien'

     type = fields.Selection([('entretien courant', 'Entretien courant'), ('révision', 'Révision'), ('réparation', 'Réparation'),])