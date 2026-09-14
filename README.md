# Projet 7 - Prediction de revenus

Ce projet analyse la mobilite intergenerationnelle des revenus et etudie des modeles permettant d'estimer le revenu potentiel d'une personne.

## Contenu

Le notebook [Partie_1_P7.ipynb](Partie_1_P7.ipynb) prepare les donnees :

- traite les valeurs manquantes ;
- represente les revenus et les indices de Gini ;
- attribue une classe de revenus parentale selon le coefficient d'elasticite ;
- produit `analyse.csv`.

Le notebook [Partie_2_P7.ipynb](Partie_2_P7.ipynb) compare ensuite des modeles statistiques et verifie leurs hypotheses.

Les fonctions reutilisables sont regroupees dans [functions1.py](functions1.py) et [functions2.py](functions2.py). Les tests rapides sont dans [test_functions.py](test_functions.py).

## Installation et utilisation

```bash
python -m venv .venv
python -m pip install -r requirements.txt
python -m unittest -v
```

Ouvrir ensuite les notebooks depuis la racine du projet et les executer dans l'ordre. Les chemins de donnees sont relatifs a cette racine.

## Donnees

- `country_code.csv` : codes pays ISO3-3166 Alpha-3 ;
- `data-projet7.csv` : revenus par quantile, pays et annee ;
- `gdim.csv` : coefficients de mobilite intergenerationnelle ;
- `gini.csv` : indices de Gini ;
- `population.csv` : population par pays.

Les donnees sources sont conservees dans le depot pour permettre la reproduction de l'analyse. `analyse.csv` est le resultat intermediaire genere par le premier notebook.

## Validation

Les tests verifient notamment la reproductibilite de la simulation, la gestion des valeurs egales dans les quantiles, l'indexation des probabilites conditionnelles et la selection backward des variables.

## Auteur

Cheikhou FOFANA
