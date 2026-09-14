import statsmodels.formula.api as smf


def _formula(response, predictors):
    terms = " + ".join(predictors)
    return "{} ~ {}".format(response, terms if terms else "1")

def forward_selected(data, response):
    """Linear model designed by forward selection.

    Parameters:
    -----------
    data : pandas DataFrame with all possible predictors and response

    response: string, name of response column in data

    Returns:
    --------
    model: an "optimal" fitted statsmodels linear model
           with an intercept
           selected by forward selection
           evaluated by adjusted R-squared
    """
    if response not in data.columns:
        raise ValueError("response must be a column in data")

    remaining = set(data.columns)
    remaining.remove(response)
    selected = []
    current_score, best_new_score = 0.0, 0.0
    while remaining and current_score == best_new_score:
        scores_with_candidates = []
        for candidate in remaining:
            formula = _formula(response, selected + [candidate])
            score = smf.ols(formula, data).fit().rsquared_adj
            scores_with_candidates.append((score, candidate))
        scores_with_candidates.sort()
        best_new_score, best_candidate = scores_with_candidates.pop()
        if current_score < best_new_score:
            remaining.remove(best_candidate)
            selected.append(best_candidate)
            current_score = best_new_score
    formula = _formula(response, selected)
    model = smf.ols(formula, data).fit()
    print(model.summary())
    return model


def backward_selected(data, response):
    """Linear model designed by backward selection.

    Parameters:
    -----------
    data : pandas DataFrame with all possible predictors and response

    response: string, name of response column in data

    Returns:
    --------
    model: an "optimal" fitted statsmodels linear model
           with an intercept
           selected by backward selection
           evaluated by parameters p-value
    """
    if response not in data.columns:
        raise ValueError("response must be a column in data")

    remaining = set(data._get_numeric_data().columns)
    if response in remaining:
        remaining.remove(response)
    cond = True

    while remaining and cond:
        formula = _formula(response, sorted(remaining))
        print('_______________________________')
        print(formula)
        model = smf.ols(formula, data).fit()
        score = model.pvalues.drop(labels="Intercept", errors="ignore")
        worst_candidate = score.idxmax()
        worst_pvalue = score.loc[worst_candidate]
        if worst_pvalue > 0.05:
            print('remove', worst_candidate, '(p-value :', round(worst_pvalue, 3), ')')
            remaining.remove(worst_candidate)
        else:
            cond = False
            print('is the final model !')
        print('')
    print(model.summary())
    
    return model
        
        