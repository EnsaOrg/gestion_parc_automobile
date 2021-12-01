# gestion_patrimoine_public
Il s'agit de notre projet de semestre qui consiste à développer un mode ERP qui permet de gérer le patrimoine communal à travers une base de données patrimoine et des modules des procédures qui l'alimentent et la mettent à jour.

# Cahier de charge

1. Introduction
Le patrimoine est défini comme l’ensemble des biens possédés à un moment donné et ayant une valeur économique. Le patrimoine de la commune est constitué de l’ensemble de ses biens meubles et immeubles.
Le futur système vise à fournir des informations relatives à la maîtrise foncière, à la maîtrise des équipements, aux règles d’utilisation et différents modes de gestion de biens communaux prévus par les textes réglementaires.
Le logiciel de gestion du patrimoine doit permettre la mise en place d’un référentiel unique et partagé par l’ensemble des services, le suivi règlementaire et documentaire de tous les biens, la fourniture aux gestionnaires des tableaux de pilotage du patrimoine. Il doit aussi permettre la sécurisation de son patrimoine, la mise en place de programme préventif pour une amélioration de la performance des équipements

2. Spécifications fonctionnelles et techniques
2.1. Les principales exigences fonctionnelles de l’outil de gestion du patrimoine sont :
* Une structure en arborescence du patrimoine avec un nombre de niveaux illimité
* Une gestion multi entités pour l’attribution des biens par site et service.
* Un générateur d’écran afin de modéliser tous les types d’actif : immobilier, équipements, véhicules, voirie et réseaux urbains, espaces verts, équipements sportifs, mobilier, engins, matériel technique, sites tertiaires, téléphonie, parc informatique ...
* Un référencement de chaque élément dans un réseau intelligent
* Un suivi et une répartition des affectations comprenant l’occupation des locaux et la gestion des zones d’occupation
* La gestion administrative des biens
* Le calcul des surfaces avec une consolidation à chaque niveau de l’arborescence
* Une gestion documentaire intégrée avec classement et recherche thématique
* Le traitement des biens réformés, détruits ou vendus
* La gestion des contrats avec des alertes en cas d’évènements liés à ceux-ci
* Un carnet de santé associé à chaque élément du patrimoine avec la réactualisation automatique de l’état des biens à partir d’indicateurs de vétusté
* La gestion de la conformité à la réglementation afin de s'assurer que les règles de sécurité pour les ERP (Etablissement recevant du public), les règles de construction, visites, normes d'hygiène soient respectées
* Des alertes automatiques et programmables sur les visites et les contrôles
* L’historique et le suivi des actions et des évènements survenus sur un patrimoine (mise en service, changements d’affectation, travaux effectués ...)
* Une aide à la décision sur la gestion du patrimoine en termes financiers (maîtrise des dépenses, investissements), d’optimisation des affectations, d’état du patrimoine et de renouvellement, de sécurité.

2.2. Spécifications techniques
Le sous système patrimoine doit permettre de gérer le patrimoine communal à travers une base de données patrimoine et des modules des procédures qui l’alimentent et la mettent à jour ;

Le sous système est composé des modules suivants :
- Opérations Liées au patrimoine communal privé:
o Les acquisitions : permet le suivi des dossiers relatifs à la procédure d’acquisition des biens ;
o Acquisition des biens immobiliers à titre gratuit ;
o Acquisition des biens immobiliers à titre onéreux ;
o Cession des biens immobiliers du patrimoine communal privé par voie d’adjudication ;
o Cession des biens immobiliers du patrimoine communal privé de grès à grès ;
o Echange ;
o Dons et Legs ;
o Baux Normaux ;
o Baux Emphytéotiques ;

- Opérations Liées au patrimoine communal public
o Classement Formel ;
o Classement Tacite ou sans formalités spéciales ;
o Déclassement Formel ;
o Déclassement Tacite ou sans formalités préalables ;
o Occupation Temporaire du patrimoine communal public avec emprise (de grès à grès) ;
o Occupation Temporaire du patrimoine communal public avec emprise (par mise en concurrence) ;
o Occupation Temporaire du patrimoine communal public sans emprise ;
o Délimitation du Domaine Public Communal ;
o Procédures d’Alignement :
- Arrêté d’Alignement « simple » ;
- Arrêté de Cessibilité ;
- Arrêté d’Alignement Emportant Cessibilité .

3.3. Minimum des fonctionnalités à implémenter
En somme le futur système d’information devra permettre :
- La gestion d’un référentiel immobilier :
La description physique du patrimoine (caractéristiques du foncier, de l’immobilier bâti : données de localisation, données juridiques, données d’urbanisme, valeurs,...,)
- La gestion d’un référentiel mobilier :
La description physique du patrimoine (caractéristiques quantitatives et qualitatives, et types d’équipements (matériel, engins, mobilier, véhicules,…)
- Des actions sur ce patrimoine : ajouts/suppressions ; fusion /éclatement
- La couverture de la gestion de procédures métiers qui se traduisent par des actions sur le référentiel : acquisition, cession, apurement, location, affectation,…
Les fonctionnalités attendues pour la gestion de ces procedures metiers couvrent :
* Une structure en arborescence du patrimoine avec un nombre de niveaux illimité ;
* Une gestion multi entités pour l’attribution des biens par site et service gestionnaire ;

* Un générateur d’écran afin de modéliser tous les types d’actif : immobilier, équipements, véhicules, voirie, espaces verts, équipements sportifs, mobilier, engins, matériel technique, parc informatique ...
* La gestion administrative des biens ;
* Une gestion documentaire intégrée avec classement et recherche thématique ;
* Le traitement des biens réformés, détruits ou vendus ;
* Un carnet de santé associé à chaque élément du patrimoine avec la réactualisation automatique de l’état des biens à partir d’indicateurs de vétusté ;
* Le suivi des évenements associés à l’avancement de la procedure ;
* La gestion des données propre à une procedure ;
* Automatisation de l’ensemble des actes de gestion (actes de vente, contrat de location, PV, cahier de charges,…) ;
* Le suivi des affaires juridiques et contentieuses concernant le patrimoine ;
* Suivi des étapes des dossiers de procédures avec des alertes automatiques et programmables;
* L’historique et le suivi des actions et des évènements survenus sur un patrimoine (mise en service, changements d’affectation, travaux effectués ...)
* Une aide à la decision sur la gestion du patrimoine permettant l’analyse des données et la production de tableaux de bord ; en termes financiers (maîtrise des dépenses, investissements), d’optimisation des affectations, d’état du patrimoine et de renouvellement,…
* Mise à jour automatique du référentiel du patrimoine à partir des dossiers de procédures :
- Réservation des biens pour les procédures concernées (cession, affectation, location,…)
- Radiation des terrains et des procédures qui aboutissent à un transfert de propriété ;
- Alimentation du patrimoine pour les procédures qui aboutissent à une acquisition ;
- Changement d’une référence foncière (non immatriculé, titre) suite à une procédure d’apurement du patrimoine.
- Modification des superficies des références foncières des terrains conformément aux procédures d’apurement du patrimoine.



