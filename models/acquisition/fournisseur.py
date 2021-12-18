from odoo import models, fields, api

class ParcAutomobileFournisseur(models.Model):
     _name = 'parc_automobile.fournisseur'

     registre_commerce = fields.Char('Registre de commerce')
     date_enregistrement = fields.Date('Date enregistrement')
     adresse = fields.Char('Adresse')
     type =  fields.Selection([('concessionnaire','Concessionnaire'),('agence de location','Agence de location')])

     #acquisition_ids = fields.One2many(comodel_name='parc_automobile.acquisition', inverse_name='rel_id')
     achat_ids = fields.One2many(comodel_name='parc_automobile.achat', inverse_name='fournisseur_id')
     location_ids = fields.One2many(comodel_name='parc_automobile.location', inverse_name='fournisseur_id')

     @api.multi
     def name_get(self):
          result = []
          for fournisseur in self:
               name = '[Régistre de commerce: ' + fournisseur.registre_commerce + ' - Type: ' + fournisseur.type + ']'
               result.append((fournisseur.id, name))
          return result

     nbr_vehicule = fields.Integer(String="Nombre de véhicules", compute='comp_vehicule')

     @api.one
     def comp_vehicule(self):
          self.nbr_vehicule = len(self.achat_ids) + len(self.location_ids)