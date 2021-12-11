from odoo import models, fields, api

class ParcAutomobileMarque(models.Model):
     _name = 'parc_automobile.marque'

     nom = fields.Char('Marque')
     type = fields.Selection([('coupé','Coupé'),('berline','Berline'),('hayon','Hayon'),('break','Break'),
                              ('limousine','Limousine'),('pick-up','Pick-up'),('crossovers','Crossovers'),
                              ('suv','SUV'),('fourgonnette','Fourgonnette'),('mini-ourgonnette','Mini-fourgonnette'),
                              ('carrosserie liftback','Carrosserie Liftback'),('cabriolet','Cabriolet'),('minibus','Minibus'),
                              ('autobus', 'Autobus'),('roadsters','Roadsters'),('targa','Targa'),])

     vehicule_ids = fields.One2many(comodel_name='parc_automobile.vehicule', inverse_name='marque_id')
     modele_ids = fields.One2many(comodel_name='parc_automobile.modele', inverse_name='marque_id')