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

     vehicule_id = fields.Many2one(comodel_name='parc_automobile.vehicule', delegate=True)



     conducteur_ids = fields.Many2many(comodel_name='parc_automobile.conducteur',
                                       relation='conducteur_affectation_rel',
                                       column1='matricule',
                                       column2='date_debut')