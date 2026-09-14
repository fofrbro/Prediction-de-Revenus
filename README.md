# Projet 7 - Prédiction de revenus

Ce projet analyse la mobilité intergénérationnelle des revenus et étudie des modèles permettant d'estimer le revenu potentiel d'une personne.

## Contenu

Le notebook [Partie_1_P7.ipynb](Partie_1_P7.ipynb) prépare les données :

- traite les valeurs manquantes ;
- représente les revenus et les indices de Gini ;
- attribue une classe de revenus parentale selon le coefficient d'élasticité ;
- produit `analyse.csv`.

Le notebook [Partie_2_P7.ipynb](Partie_2_P7.ipynb) compare ensuite des modèles statistiques et vérifie leurs hypothèses.

Les fonctions réutilisables sont regroupées dans [functions1.py](functions1.py) et [functions2.py](functions2.py). Les tests rapides sont dans [test_functions.py](test_functions.py).

## Installation et utilisation

```bash
python -m venv .venv
python -m pip install -r requirements.txt
python -m unittest -v
```

Ouvrir ensuite les notebooks depuis la racine du projet et les exécuter dans l'ordre. Les chemins de données sont relatifs à cette racine.

## Données

- `country_code.csv` : codes pays ISO3-3166 Alpha-3 ;
- `data-projet7.csv` : revenus par quantile, pays et année ;
- `gdim.csv` : coefficients de mobilité intergénérationnelle ;
- `gini.csv` : indices de Gini ;
- `population.csv` : population par pays.

Les données sources sont conservées dans le dépôt pour permettre la reproduction de l'analyse. `analyse.csv` est le résultat intermédiaire généré par le premier notebook.

## Validation

Les tests vérifient notamment la reproductibilité de la simulation, la gestion des valeurs égales dans les quantiles, l'indexation des probabilités conditionnelles et la sélection backward des variables.

## Auteur

Cheikhou FOFANA
