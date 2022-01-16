from odoo import models, fields, api

class ParcAutomobileVisiteTechnique(models.Model):
     _name = 'parc_automobile.visite_technique'
     # _inherit = "parc_automobile.intervention"
     # _description = "Hérite de la classe intervention"

     date = fields.Date('Date d\'acquisition')
     montant_frais = fields.Float('Frais (en DH)')
     prestataire = fields.Char()
     duree = fields.Integer('Durée (en jours)')

     certificat = fields.Selection([('a', 'A'), ('s', 'S')])

     vehicule_id = fields.Many2one(comodel_name='parc_automobile.vehicule', delegate=True, required=True)

     @api.multi
     def name_get(self):
          result = []
          for visite in self:
               name = '[Prestataire: ' + str(visite.prestataire) + ' - Véhicule: ' + str(visite.vehicule_id.matricule) + ']'
               result.append((visite.id, name))
          return result