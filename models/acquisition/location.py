from odoo import models, fields, api

class ParcAutomobileLocation(models.Model):
     _name = 'parc_automobile.location'
     # _inherit = "parc_automobile.acquisition"
     # _description = "Hérite de la classe acquisition"

     date = fields.Date('Date d\'acquisition')
     montant = fields.Float()
     motif = fields.Text('Motif')
     #durée en heure
     duree = fields.Integer()

     fournisseur_id = fields.Many2one(comodel_name='parc_automobile.fournisseur', delegate=True, required=True)

     @api.multi
     def name_get(self):
          result = []
          for location in self:
               name = '[Date: ' + location.date + ' - Motif: ' + location.motif + ']'
               result.append((location.id, name))
          return result