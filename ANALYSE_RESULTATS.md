# Analyse des resultats

## 1. Objet de l'etude

Le projet cherche a expliquer le revenu d'un enfant a partir de variables liees au pays et a l'origine sociale :

- le revenu moyen du pays (`mj` ou `ln_mj`) ;
- l'indice de Gini (`Gj`) ;
- la classe de revenu des parents (`c_i_parent`) ;
- le coefficient d'elasticite intergenerationnelle (`pj`).

Les resultats ci-dessous sont ceux sauvegardes dans `02_modelisation_revenus.ipynb`.

## 2. Resultats principaux

### Analyse de variance par pays

L'ANOVA montre que le pays d'appartenance explique une part importante de la variabilite du revenu enfant. Le modele ANOVA obtient un `R2` d'environ **49,6 %**.

Interpretation : les niveaux de revenus different fortement selon les pays. Cette variable capte cependant aussi des effets non observes propres aux pays : institutions, prix, education, marche du travail et qualite des donnees.

### Regression avec revenu moyen et Gini

Le modele utilisant le revenu moyen du pays et l'indice de Gini explique environ **72,9 %** de la variance de la variable dependante transformee en logarithme.

Le passage au logarithme est pertinent pour une variable de revenu : il reduit l'effet des valeurs extremes et permet une lecture plus proche d'une variation relative que d'une variation absolue.

### Regression complete

Le modele final utilise :

```text
ln_y_child ~ Gj + ln_mj + c_i_parent
```

Ses principaux resultats sont :

| Indicateur | Resultat |
|---|---:|
| Nombre d'observations | 5 800 000 |
| R2 | 0,785 |
| Variance expliquee | 78,5 % |
| Effet partiel de `Gj` | 10,55 % |
| Effet partiel de `ln_mj` | 62,33 % |
| Effet partiel de `c_i_parent` | 5,62 % |
| VIF des variables | environ 1,00 a 1,08 |

Les coefficients estimes sont :

| Variable | Coefficient | Lecture prudente |
|---|---:|---|
| `Gj` | -1,6521 | A revenu moyen comparable, un Gini plus eleve est associe a un revenu enfant plus faible dans ce modele. |
| `ln_mj` | 0,9864 | Le revenu moyen du pays est le facteur explicatif le plus important. |
| `c_i_parent` | 0,0113 | Une classe parentale plus elevee est associee a un revenu enfant plus eleve. |

Les trois variables sont significatives au seuil de 5 % dans la sortie sauvegardee. Le modele est donc globalement significatif selon le test de Fisher.

## 3. Diagnostics du modele

### Colinearite

Les facteurs d'inflation de variance sont proches de 1. Il n'y a pas d'indice de colinearite problematique entre les variables explicatives retenues.

### Homoscedasticite

Le test de Breusch-Pagan donne une p-value proche de 0. L'hypothese d'homoscedasticite est rejetee : la variance des residus depend des valeurs predites ou des variables explicatives.

Les coefficients et les tests devraient donc etre controles avec des erreurs standards robustes, par exemple HC3, avant toute conclusion inferentielle.

### Normalite des residus

Les tests de Kolmogorov-Smirnov et de Jarque-Bera donnent une p-value proche de 0. La normalite des residus est rejetee.

Avec 5,8 millions d'observations, ces tests sont tres sensibles a de petits ecarts. Il faut completer leur lecture par des graphiques, des quantiles, l'analyse des residus et surtout une evaluation hors echantillon.

## 4. Interpretation generale

Le revenu moyen du pays est le principal determinant statistique observe : il explique environ 62,33 % de la variance dans la decomposition presentee. Le contexte national domine donc la prediction du revenu enfant.

L'origine sociale conserve un effet mesurable : la classe de revenu des parents explique environ 5,62 % de la variance apres prise en compte du pays et du Gini. Cela va dans le sens d'une persistance intergenerationnelle des revenus.

Le signe negatif du coefficient du Gini suggere qu'une plus forte inegalite est associee a un revenu enfant plus faible, toutes choses egales par ailleurs dans ce modele. Cette association ne permet toutefois pas de conclure que reduire le Gini provoquerait directement une hausse du revenu individuel.

## 5. Limites a retenir

1. **Pas de validation hors echantillon** : les `R2` proviennent de l'ajustement sur les donnees utilisees pour estimer les coefficients. La performance predictive reelle n'est pas mesuree.
2. **Observations repetees** : le jeu de donnees est construit a partir de quantiles par pays. Les 5,8 millions de lignes ne representent pas necessairement 5,8 millions d'individus independants.
3. **Dependance des observations** : les variables nationales sont repetees pour de nombreuses lignes. Les p-values classiques peuvent donc etre trop optimistes.
4. **Hypotheses lineaires imparfaites** : heteroscedasticite et non-normalite des residus sont detectees.
5. **Risque de confusion entre association et causalite** : le modele n'identifie pas un effet causal du Gini, du revenu national ou du revenu parental.
6. **Comparaison des criteres AIC/BIC** : les modeles ne doivent pas etre compares uniquement par AIC ou BIC lorsqu'ils n'ont pas exactement la meme variable dependante ou la meme echelle.

## 6. Recommandations pour ameliorer la prediction

- separer les donnees en ensembles d'apprentissage et de test ;
- mesurer la MAE et la RMSE sur l'ensemble de test ;
- utiliser des erreurs standards robustes ou un modele hierarchique par pays ;
- tenir compte du poids et de la structure des quantiles ;
- tester des interactions, notamment `ln_mj * c_i_parent` ;
- comparer avec une regression regularisee et un modele non lineaire ;
- conserver une analyse par pays ou par region pour verifier la stabilite des coefficients ;
- documenter explicitement la construction de `analysis_dataset.csv` et la gestion des valeurs manquantes.

## Conclusion

Le modele final est informatif et explique une part importante de la variabilite du logarithme du revenu enfant (`R2 = 78,5 %`). Le revenu moyen du pays est le facteur le plus important, tandis que l'origine sociale apporte une information supplementaire. En revanche, la performance predictive et la validite inferentielle ne sont pas encore etablies hors echantillon. La prochaine etape prioritaire est donc une validation avec donnees de test et une estimation robuste a la dependance entre observations.
