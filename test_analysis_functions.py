import unittest

import numpy as np
import pandas as pd

from income_mobility import (
    compute_quantiles,
    conditional_distributions,
    generate_incomes,
    proba_cond,
    quantiles,
)
from model_selection import backward_selected


class FunctionsTestCase(unittest.TestCase):
    def test_generate_incomes_is_reproducible(self):
        first = generate_incomes(20, 0.5, random_state=7)
        second = generate_incomes(20, 0.5, random_state=7)
        self.assertTrue(np.array_equal(first[0], second[0]))
        self.assertTrue(np.array_equal(first[1], second[1]))

    def test_quantiles_handle_ties_and_lists(self):
        self.assertEqual(quantiles([1, 1, 2, 3], 2).tolist(), [1, 1, 2, 2])

    def test_probability_uses_one_based_quantile_labels(self):
        sample = compute_quantiles(range(1, 101), range(1, 101), 10)
        matrix = conditional_distributions(sample, 10)
        self.assertEqual(proba_cond(1, 1, matrix), 1.0)

    def test_backward_selection_keeps_significant_predictor(self):
        data = pd.DataFrame(
            {
                "y": range(1, 9),
                "x": range(1, 9),
                "noise": [2, 1, 2, 1, 2, 1, 2, 1],
            }
        )
        model = backward_selected(data, "y")
        self.assertIn("x", model.params.index)


if __name__ == "__main__":
    unittest.main()
