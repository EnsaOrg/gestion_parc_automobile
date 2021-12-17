from odoo import models, fields, api

class ParcAutomobileAchat(models.Model):
     _name = 'parc_automobile.achat'
     # _inherit = "parc_automobile.acquisition"
     # _description = "Hérite de la classe acquisition"

     date = fields.Date('Date d\'achat')
     montant = fields.Float()
     motif = fields.Text('Motif')

     fournisseur_id = fields.Many2one(comodel_name='parc_automobile.fournisseur', delegate=True, required=True)

     @api.multi
     def name_get(self):
          result = []
          for achat in self:
               name = '[Date: ' + achat.date + ' - Motif: ' + achat.motif + ']'
               result.append((achat.id, name))
          return result