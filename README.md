# Projet 7 - Prédiction de revenus

Ce projet analyse la mobilité intergénérationnelle des revenus et étudie des modèles permettant d'estimer le revenu potentiel d'une personne.

## Contenu

Le notebook [01_preparation_donnees.ipynb](01_preparation_donnees.ipynb) prépare les données :

- traite les valeurs manquantes ;
- représente les revenus et les indices de Gini ;
- attribue une classe de revenus parentale selon le coefficient d'élasticité ;
- produit `analysis_dataset.csv`.

Le notebook [02_modelisation_revenus.ipynb](02_modelisation_revenus.ipynb) compare ensuite des modèles statistiques et vérifie leurs hypothèses.

Les fonctions réutilisables sont regroupées dans [income_mobility.py](income_mobility.py) et [model_selection.py](model_selection.py). Les tests rapides sont dans [test_analysis_functions.py](test_analysis_functions.py).

## Installation et utilisation

```bash
python -m venv .venv
python -m pip install -r requirements.txt
python -m unittest -v
```

Ouvrir ensuite les notebooks depuis la racine du projet et les exécuter dans l'ordre. Les chemins de données sont relatifs à cette racine.

## Données

- `country_codes.csv` : codes pays ISO3-3166 Alpha-3 ;
- `world_income_distribution.csv` : revenus par quantile, pays et année ;
- `intergenerational_mobility.csv` : coefficients de mobilité intergénérationnelle ;
- `gini_indices.csv` : indices de Gini ;
- `population_by_country.csv` : population par pays.

Les données sources sont conservées dans le dépôt pour permettre la reproduction de l'analyse. `analysis_dataset.csv` est le résultat intermédiaire généré par le premier notebook.

## Validation

Les tests vérifient notamment la reproductibilité de la simulation, la gestion des valeurs égales dans les quantiles, l'indexation des probabilités conditionnelles et la sélection backward des variables.

## Auteur

Cheikhou FOFANA
