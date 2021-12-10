from odoo import models, fields, api

class ParcAutomobileModele(models.Model):
     _name = 'parc_automobile.modele'

     version = fields.Selection([('2005','2005'),('2006','2006'),('2007','2007'),('2008','2008'),('2009','2009'),
                                 ('2010','2010'),('2011','2011'),('2012','2012'),('2013','2013'),('2014','2014'),
                                 ('2015','2015'),('2016','2016'),('2017','2017'),('2018','2018'),('2019','2019'),
                                 ('2020','2020'),('2021','2021'),])
     puissance = fields.Integer()
     energie = fields.Integer()
     nbr_place = fields.Integer()
     nbr_porte = fields.Integer()
     vitesse_maximale = fields.Integer()
     consommation_moyenne = fields.Integer()
     capacite_coffre = fields.Integer()
     sexe = fields.Selection([('manuelle','Manuelle'),('automatique','Automatique')])
     longueur = fields.Float();
     largeur = fields.Float();
     hauteur = fields.Float();
     confort = fields.Selection([('faible','faible'),('moyen','Moyen'),('luxe','Luxe')])