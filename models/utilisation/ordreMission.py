from odoo import models, fields, api, _

class ParcAutomobileOrdreMission(models.Model):
     _name = 'parc_automobile.ordre_mission'
     autorisation = fields.Char(string='Autorisation', required=True, copy=False, readonly=True, index=True, default=lambda self: _('New'))
     permanence = fields.Boolean()
     deplacement = fields.Boolean()
     pointage = fields.Boolean()
     activite = fields.Selection([('administrative', 'Administrative'), ('logistique', 'Logistique'),
                                  ('commerciale', 'Commerciale'), ('autre', 'Autre')])

     trajet_id = fields.Many2one(comodel_name='parc_automobile.trajet', delegate=True)
     affectation_id = fields.Many2one(comodel_name='parc_automobile.affectation', delegate=True)

     _sql_constraints = [
          ('autorisation', 'unique(autorisation)', 'Existe déjà!'),
     ]

     @api.multi
     def name_get(self):
          result = []
          for ordre in self:
               name = '[Autorisation: ' + str(ordre.autorisation) + ' - Activité: ' + str(ordre.activite) + ']'
               result.append((ordre.id, name))
          return result

     @api.model
     def create(self, vals):
          if vals.get('autorisation', _('New')) == _('New'):
               vals['autorisation'] = self.env['ir.sequence'].next_by_code('parc_automobile.ordre_mission.sequence') or _('New')
          result = super(ParcAutomobileOrdreMission, self).create(vals)
          return result
