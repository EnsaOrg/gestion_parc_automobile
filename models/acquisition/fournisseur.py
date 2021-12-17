from odoo import models, fields, api

class ParcAutomobileFournisseur(models.Model):
     _name = 'parc_automobile.fournisseur'

     registre_commerce = fields.Char('Registre de commerce')
     date_enregistrement = fields.Date('Date enregistrement')
     adresse = fields.Char('Adresse')
     type =  fields.Selection([('concessionnaire','Concessionnaire'),('agence de location','Agence de location')])

     #acquisition_ids = fields.One2many(comodel_name='parc_automobile.acquisition', inverse_name='rel_id')
     acquisition_ids = fields.One2many(comodel_name='parc_automobile.achat', inverse_name='fournisseur_id')
     acquisition_ids = fields.One2many(comodel_name='parc_automobile.location', inverse_name='fournisseur_id')