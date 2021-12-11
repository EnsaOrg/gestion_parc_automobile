from odoo import models, fields, api

class ParcAutomobileAffectation(models.Model):
     _name = 'parc_automobile.affectation'

     num_agence = fields.Integer()
     date_debut = fields.Date('Date de début')
     date_fin_prevue = fields.Date('Date de fin prévue')
     date_fin_reelle = fields.Date('Date de fin réelle')
     prime_totale = fields.Float()
     activite = fields.Char('Activite')
     region = fields.Char('Région')
     secteur = fields.Char('Secteur')
     direction = fields.Char('Direction')