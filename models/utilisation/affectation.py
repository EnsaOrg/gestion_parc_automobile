from odoo import models, fields, api

class ParcAutomobileAffectation(models.Model):
     _name = 'parc_automobile.affectation'

     date_debut = fields.Date('Date de début')
     date_fin_prevue = fields.Date('Date de fin prévue')
     date_fin_reelle = fields.Date('Date de fin réelle')
     region = fields.Char('Région')
     secteur = fields.Char('Secteur')
     direction = fields.Char('Direction')

     vehicule_id = fields.Many2one(comodel_name='parc_automobile.vehicule', delegate=True, required=True)

     conducteur_ids = fields.Many2many(comodel_name='parc_automobile.conducteur',
                                       relation='conducteur_affectation_rel',
                                       column1='matricule',
                                       column2='date_debut',required=True)

     @api.multi
     def name_get(self):
         result = []
         for affectation in self:
             name = '[Date: ' + str(affectation.date_debut) + ' - Activité: ' + str(affectation.vehicule_id.matricule) + ']'
             result.append((affectation.id, name))
         return result

     nbr_conducteur = fields.Integer(string="Nombre de véhicules", compute='comp_conducteur')

     @api.one
     def comp_conducteur(self):
         self.nbr_conducteur = len(self.conducteur_ids)