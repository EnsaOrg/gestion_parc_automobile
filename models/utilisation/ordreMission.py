from odoo import models, fields, api

class ParcAutomobileOrdreMission(models.Model):
     _name = 'parc_automobile.ordre_mission'

     autorisation = fields.Integer()
     permanence = fields.Boolean()
     deplacement = fields.Boolean()
     pointage = fields.Boolean()
     activite = fields.Selection([('administrative', 'Administrative'), ('logistique', 'Logistique'),
                                  ('commerciale', 'Commerciale'), ('autre', 'Autre')])

     trajet_id = fields.Many2one(comodel_name='parc_automobile.trajet', delegate=True)
     affectation_id = fields.Many2one(comodel_name='parc_automobile.affectation', delegate=True)

     @api.multi
     def name_get(self):
          result = []
          for ordre in self:
               name = '[Autorisation: ' + str(ordre.autorisation) + ' - Activité: ' + str(ordre.activite) + ']'
               result.append((ordre.id, name))
          return result