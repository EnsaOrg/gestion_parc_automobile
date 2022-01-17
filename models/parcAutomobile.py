from odoo import models, fields, api, _

class ParcAutomobileParcAutomobile(models.Model):
     _name = 'parc_automobile.parc_automobile'

     num_parc = fields.Char(string='Order Reference', required=True, copy=False, readonly=True, index=True, default=lambda self: _('New'))
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

     @api.model
     def create(self, vals):
          if vals.get('num_parc', _('New')) == _('New'):
               vals['num_parc'] = self.env['ir.sequence'].next_by_code(
                    'parc_automobile.parc_automobile.sequence') or _('New')
          result = super(ParcAutomobileParcAutomobile, self).create(vals)
          return result

     @api.multi
     @api.onchange('vehicule_ids')
     def check_number_of_vehicules(self):
          if len(self.vehicule_ids) > self.capacite:
               return {'warning': {'title': 'Problème',
                                   'message': 'La capacité du parc a été dépassée'}}