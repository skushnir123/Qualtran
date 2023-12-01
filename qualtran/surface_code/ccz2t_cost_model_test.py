#  Copyright 2023 Google LLC
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import numpy as np

from qualtran.surface_code.algorithm_summary import AlgorithmSummary
from qualtran.surface_code.ccz2t_cost_model import (
    get_ccz2t_costs,
    get_ccz2t_costs_from_error_budget,
    get_ccz2t_costs_from_grid_search,
)


def test_vs_spreadsheet():
    re = get_ccz2t_costs_from_error_budget(
        n_magic=AlgorithmSummary(t_gates=10**8, toffoli_gates=10**8),
        n_algo_qubits=100,
        error_budget=0.01,
        phys_err=1e-3,
        cycle_time_us=1,
    )

    np.testing.assert_allclose(re.failure_prob, 0.0084, rtol=1e-3)
    np.testing.assert_allclose(re.footprint, 4.00e5, rtol=1e-3)
    np.testing.assert_allclose(re.duration_hr, 7.53, rtol=1e-3)


def test_grid_search_runs():
    # TODO: a better test vs some published reference
    cost, factory, db = get_ccz2t_costs_from_grid_search(
        n_magic=AlgorithmSummary(t_gates=10**8, toffoli_gates=10**8),
        n_algo_qubits=100,
        phys_err=1e-3,
        cycle_time_us=1,
    )
    assert factory.distillation_l1_d == 15
    assert factory.distillation_l2_d == 23
    assert db.data_d == 25
