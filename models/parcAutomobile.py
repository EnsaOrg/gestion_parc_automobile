from odoo import models, fields, api

class ParcAutomobileParcAutomobile(models.Model):
     _name = 'parc_automobile.parc_automobile'

     num_parc = fields.Integer()
     capacite = fields.Integer()
     localisation = fields.Text()

     vehicule_ids = fields.One2many(comodel_name='parc_automobile.vehicule', inverse_name='parc_id')

     _sql_constraints = [
          ('num_parc', 'unique(num_parc)', 'Existe déjà!'),
     ]

     @api.multi
     def name_get(self):
          result = []
          for parc in self:
               name = '[N° Parc: ' + str(parc.num_parc) + ' - Localisation: ' + str(parc.localisation)+']'
               result.append((parc.id, name))

          return result

     nbr_vehicule = fields.Integer(string="Nombre de véhicules", compute='comp_vehicule')

     @api.one
     def comp_vehicule(self):
          self.nbr_vehicule = len(self.vehicule_ids)