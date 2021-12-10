from odoo import models, fields, api

class ParcAutomobileFournisseur(models.Model):
     _name = 'parc_automobile.fournisseur'
     _inherit = "parc_automobile.acquisition"
     _description = "Hérite de la casse acquisition"

     registre_commerce = fields.Char('Registre de commerce')
     date_enregistrement = fields.Date('Date enregistrement')
     adresse = fields.Char('Adresse')
     type =  fields.Selection([('concessionnaire','Concessionnaire'),('agence de location','Agence de location')])