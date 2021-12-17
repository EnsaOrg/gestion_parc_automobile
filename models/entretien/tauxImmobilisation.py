from odoo import models, fields, api

class ParcAutomobileTauxImmobilisation(models.Model):
     _name = 'parc_automobile.taux_immobilisation'
     # _inherit = "parc_automobile.intervention"
     # _description = "Hérite de la classe intervention"

     date = fields.Date('Date')
     montant_frais = fields.Float()
     prestataire = fields.Char()
     duree = fields.Integer()
     nbr_heure = fields.Integer()

     vehicule_id = fields.Many2one(comodel_name='parc_automobile.vehicule', delegate=True, required=True)

     @api.multi
     def name_get(self):
          result = []
          for taux in self:
               name = '[Prestataire: ' + str(taux.prestataire) + ' - Véhicule: ' + str(taux.vehicule_id.matricule) + ']'
               result.append((taux.id, name))
          return result