from odoo import models, fields, api

class ParcAutomobileVehicule(models.Model):
     _name = 'parc_automobile.vehicule'

     matricule = fields.Char('Matricule')
     carte_grise = fields.Char('N° carte grise')
     chassis = fields.Char('Numéro de chassis')
     date_circulation = fields.Date('Date de circulation')
     date_reforme = fields.Date('Date enregistrement')
     kilometrage = fields.Integer()
     couleur = fields.Char('Couleur')