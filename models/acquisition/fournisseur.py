from odoo import models, fields, api

class ParcAutomobileFournisseur(models.Model):
     _name = 'parc_automobile.fournisseur'

     registre_commerce = fields.Char('Registre de commerce')
     date_enregistrement = fields.Date('Date enregistrement')
     adresse = fields.Char('Adresse')
     type =  fields.Selection([('concessionnaire','Concessionnaire'),('agence de location','Agence de location')])

     @api.multi
     def name_get(self):
          result = []
          for fournisseur in self:
               name = '[Régistre de commerce: ' + fournisseur.registre_commerce + ' - Type: ' + fournisseur.type + ']'
               result.append((fournisseur.id, name))
          return result

     nbr_vehicule = fields.Integer(string="Nombre de véhicules", compute='comp_vehicule')

     @api.one
     def comp_vehicule(self):
          self.nbr_vehicule = len(self.achat_ids) + len(self.location_ids)