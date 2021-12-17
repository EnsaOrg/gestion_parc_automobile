from odoo import models, fields, api

class ParcAutomobileTrajet(models.Model):
     _name = 'parc_automobile.trajet'

     isRecurrent = fields.Selection([('oui', 'OUI'), ('non', 'NON')])
     distance = fields.Integer()

     ordreMission_ids = fields.One2many(comodel_name='parc_automobile.ordre_mission', inverse_name='trajet_id')

     @api.multi
     def name_get(self):
          result = []
          for trajet in self:
               name = '[Distance: ' + str(trajet.distance) + ' Km]'
               result.append((trajet.id, name))
          return result