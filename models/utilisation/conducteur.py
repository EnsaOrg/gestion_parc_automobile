from odoo import models, fields, api

class ParcAutomobileConducteur(models.Model):
     _name = 'parc_automobile.conducteur'

     num_permis = fields.Integer()
     nom = fields.Char('Nom')
     prenom = fields.Char('Prénom')
     service = fields.Char('Service')
     departement = fields.Char('Département')
     type_permis = fields.Selection([('A','A'),('A1','A1'),('A2','A2'),
                                     ('B','B'),('B1','B1'),('BE','BE'),('C1E','C1E'),
                                     ('C','C'),('C1','C1'),('C1E','C1E'),
                                     ('D','D'),('D1','D1'),('D1E','D1E'),('DE','DE')])
     ordre = fields.Selection([('principal','Principal'),('secondaire','Secondaire')])
     validite_permis = fields.Date('Date d\'expiration')

     affectation_ids = fields.Many2many(comodel_name='parc_automobile.affectation',
                                        relation='affectation_conducteur_rel',
                                        column1='date_debut',
                                        column2='matricule')

     _sql_constraints = [
         ('num_permis', 'unique(num_permis)', 'Le matricule existe déjà!'),
     ]

     @api.multi
     def name_get(self):
         result = []
         for conducteur in self:
             name = '[Prénom: ' + conducteur.prenom + ' - Nom: ' + conducteur.nom + ']'
             result.append((conducteur.id, name))
         return result

     nbr_affectation = fields.Integer(string="Nombre de véhicules", compute='comp_affectation')

     @api.one
     def comp_affectation(self):
         self.nbr_affectation = len(self.affectation_ids)