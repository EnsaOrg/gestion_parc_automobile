from odoo import models, fields, api

class ParcAutomobileAffectation(models.Model):
     _name = 'parc_automobile.affectation'

     date_debut = fields.Date('Date de début')
     date_fin_prevue = fields.Date('Date de fin prévue')
     date_fin_reelle = fields.Date('Date de fin réelle')
     activite = fields.Char('Activite')
     region = fields.Char('Région')
     secteur = fields.Char('Secteur')
     direction = fields.Char('Direction')

     affectation_ids = fields.Many2many(comodel_name='university.affectation',
                                      relation='affectation_conducteur_rel',
                                      column1='date_debut',
                                      column2='matricule')