from odoo import models, fields, api

class ParcAutomobileLocation(models.Model):
     _name = 'parc_automobile.location'
     # _inherit = "parc_automobile.acquisition"
     # _description = "Hérite de la classe acquisition"

     date = fields.Date('Date d\'acquisition')
     montant = fields.Float('Montant (en DH)')
     motif = fields.Text('Motif')
     #durée en heure
     duree = fields.Integer('Durée (en jours)')

     vehicule_id = fields.Many2one(comodel_name='parc_automobile.vehicule', delegate=True, required=True)

     @api.multi
     def name_get(self):
          result = []
          for location in self:
               name = '[Date: ' + location.date + ' - Motif: ' + location.motif + ']'
               result.append((location.id, name))
          return result