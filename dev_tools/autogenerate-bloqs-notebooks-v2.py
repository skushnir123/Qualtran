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

"""Autogeneration of Jupyter notebooks.

For each module listed in the `NOTEBOOK_SPECS` global variable (in this file)
we write a notebook with a title, module docstring,
standard imports, and information on each bloq listed in the
`bloq_specs` field. For each gate, we render a docstring and diagrams.

## Adding a new gate.

 1. Create a new function that takes no arguments
    and returns an instance of the desired gate.
 2. If this is a new module: add a new key/value pair to the NOTEBOOK_SPECS global variable
    in this file. The key should be the name of the module with a `NotebookSpec` value. See
    the docstring for `NotebookSpec` for more information.
 3. Update the `NotebookSpec` `bloq_specs` field to include a `BloqNbSpec` for your new gate.
    Provide your factory function from step (1).

## Autogen behavior.

Each autogenerated notebook cell is tagged, so we know it was autogenerated. Each time
this script is re-run, these cells will be re-rendered. *Modifications to generated _cells_
will not be persisted*.

If you add additional cells to the notebook it will *preserve them* even when this script is
re-run

Usage as a script:
    python dev_tools/autogenerate-bloqs-notebooks-v2.py
"""

from typing import List

from qualtran_dev_tools.bloq_finder import get_bloqdocspecs
from qualtran_dev_tools.git_tools import get_git_root
from qualtran_dev_tools.jupyter_autogen_v2 import NotebookSpecV2, render_notebook

import qualtran.bloqs.arithmetic.addition
import qualtran.bloqs.arithmetic.sorting
import qualtran.bloqs.basic_gates.swap
import qualtran.bloqs.block_encoding
import qualtran.bloqs.chemistry.df.double_factorization
import qualtran.bloqs.chemistry.pbc.first_quantization.prepare_t
import qualtran.bloqs.chemistry.pbc.first_quantization.prepare_uv
import qualtran.bloqs.chemistry.pbc.first_quantization.projectile.select_and_prepare
import qualtran.bloqs.chemistry.pbc.first_quantization.select_t
import qualtran.bloqs.chemistry.pbc.first_quantization.select_uv
import qualtran.bloqs.chemistry.sf.single_factorization
import qualtran.bloqs.chemistry.sparse.prepare
import qualtran.bloqs.chemistry.thc.prepare
import qualtran.bloqs.chemistry.trotter.grid_ham.inverse_sqrt
import qualtran.bloqs.chemistry.trotter.grid_ham.qvr
import qualtran.bloqs.data_loading.qrom
import qualtran.bloqs.factoring.mod_exp
import qualtran.bloqs.mcmt.and_bloq
import qualtran.bloqs.multiplexers.apply_gate_to_lth_target
import qualtran.bloqs.qft.two_bit_ffft
import qualtran.bloqs.reflection
import qualtran.bloqs.rotations.phasing_via_cost_function
import qualtran.bloqs.rotations.quantum_variable_rotation
import qualtran.bloqs.state_preparation.prepare_uniform_superposition
import qualtran.bloqs.swap_network.cswap_approx
import qualtran.bloqs.swap_network.multiplexed_cswap
import qualtran.bloqs.swap_network.swap_with_zero

SOURCE_DIR = get_git_root() / 'qualtran/'

NOTEBOOK_SPECS: List[NotebookSpecV2] = [
    NotebookSpecV2(
        title='T Gate',
        module=qualtran.bloqs.basic_gates.t_gate,
        bloq_specs=[qualtran.bloqs.basic_gates.t_gate._T_GATE_DOC],
    ),
    NotebookSpecV2(
        title='S Gate',
        module=qualtran.bloqs.basic_gates.s_gate,
        bloq_specs=[qualtran.bloqs.basic_gates.s_gate._S_GATE_DOC],
    ),
    NotebookSpecV2(
        title='Toffoli',
        module=qualtran.bloqs.basic_gates.toffoli,
        bloq_specs=[qualtran.bloqs.basic_gates.toffoli._TOFFOLI_DOC],
    ),
    NotebookSpecV2(
        title='Swap Network',
        module=qualtran.bloqs.swap_network,
        bloq_specs=[
            qualtran.bloqs.basic_gates.swap._CSWAP_DOC,
            qualtran.bloqs.swap_network.cswap_approx._APPROX_CSWAP_DOC,
            qualtran.bloqs.swap_network.swap_with_zero._SWZ_DOC,
            qualtran.bloqs.swap_network.multiplexed_cswap._MULTIPLEXED_CSWAP_DOC,
        ],
    ),
    NotebookSpecV2(
        title='Modular Exponentiation',
        module=qualtran.bloqs.factoring.mod_exp,
        bloq_specs=[qualtran.bloqs.factoring.mod_exp._MODEXP_DOC],
        directory=f'{SOURCE_DIR}/bloqs/factoring',
    ),
    NotebookSpecV2(
        title='Modular Multiplication',
        module=qualtran.bloqs.factoring.mod_mul,
        bloq_specs=[qualtran.bloqs.factoring.mod_mul._MODMUL_DOC],
        directory=f'{SOURCE_DIR}/bloqs/factoring',
    ),
    NotebookSpecV2(
        title='Prepare Uniform Superposition',
        module=qualtran.bloqs.state_preparation.prepare_uniform_superposition,
        bloq_specs=[
            qualtran.bloqs.state_preparation.prepare_uniform_superposition._PREP_UNIFORM_DOC
        ],
        directory=f'{SOURCE_DIR}/bloqs/',
    ),
    NotebookSpecV2(
        title='Apply to Lth Target',
        module=qualtran.bloqs.multiplexers.apply_gate_to_lth_target,
        bloq_specs=[qualtran.bloqs.multiplexers.apply_gate_to_lth_target._APPLYLTH_DOC],
        directory=f'{SOURCE_DIR}/bloqs/',
    ),
    NotebookSpecV2(
        title='QROM',
        module=qualtran.bloqs.data_loading.qrom,
        bloq_specs=[qualtran.bloqs.data_loading.qrom._QROM_DOC],
    ),
    # --------------------------------------------------------------------------
    # -----   Chemistry   ------------------------------------------------------
    # --------------------------------------------------------------------------
    NotebookSpecV2(
        title='First Quantized Hamiltonian',
        module=qualtran.bloqs.chemistry.pbc.first_quantization,
        bloq_specs=[
            qualtran.bloqs.chemistry.pbc.first_quantization.select_and_prepare._FIRST_QUANTIZED_PREPARE_DOC,
            qualtran.bloqs.chemistry.pbc.first_quantization.select_and_prepare._FIRST_QUANTIZED_SELECT_DOC,
            qualtran.bloqs.chemistry.pbc.first_quantization.prepare_t._PREPARE_T,
            qualtran.bloqs.chemistry.pbc.first_quantization.prepare_uv._PREPARE_UV,
            qualtran.bloqs.chemistry.pbc.first_quantization.select_t._SELECT_T,
            qualtran.bloqs.chemistry.pbc.first_quantization.select_uv._SELECT_UV,
        ],
        directory=f'{SOURCE_DIR}/bloqs/chemistry/pbc/first_quantization',
    ),
    NotebookSpecV2(
        title='First Quantized Hamiltonian with Quantum Projectile',
        module=qualtran.bloqs.chemistry.pbc.first_quantization.projectile,
        bloq_specs=[
            qualtran.bloqs.chemistry.pbc.first_quantization.projectile.select_and_prepare._FIRST_QUANTIZED_WITH_PROJ_PREPARE_DOC,
            qualtran.bloqs.chemistry.pbc.first_quantization.projectile.select_and_prepare._FIRST_QUANTIZED_WITH_PROJ_SELECT_DOC,
        ],
        directory=f'{SOURCE_DIR}/bloqs/chemistry/pbc/first_quantization/projectile',
    ),
    NotebookSpecV2(
        title='Double Factorization',
        module=qualtran.bloqs.chemistry.df.double_factorization,
        bloq_specs=[
            qualtran.bloqs.chemistry.df.double_factorization._DF_ONE_BODY,
            qualtran.bloqs.chemistry.df.double_factorization._DF_BLOCK_ENCODING,
        ],
        directory=f'{SOURCE_DIR}/bloqs/chemistry/df',
    ),
    NotebookSpecV2(
        title='Sparse',
        module=qualtran.bloqs.chemistry.sparse,
        bloq_specs=[
            qualtran.bloqs.chemistry.sparse.prepare._SPARSE_PREPARE,
            qualtran.bloqs.chemistry.sparse.select_bloq._SPARSE_SELECT,
        ],
        directory=f'{SOURCE_DIR}/bloqs/chemistry/sparse',
    ),
    NotebookSpecV2(
        title='Single Factorization',
        module=qualtran.bloqs.chemistry.sf.single_factorization,
        bloq_specs=[
            qualtran.bloqs.chemistry.sf.single_factorization._SF_ONE_BODY,
            qualtran.bloqs.chemistry.sf.single_factorization._SF_BLOCK_ENCODING,
        ],
        directory=f'{SOURCE_DIR}/bloqs/chemistry/sf',
    ),
    NotebookSpecV2(
        title='Trotter Bloqs',
        module=qualtran.bloqs.chemistry.trotter.grid_ham,
        bloq_specs=[
            qualtran.bloqs.chemistry.trotter.grid_ham.inverse_sqrt._POLY_INV_SQRT,
            qualtran.bloqs.chemistry.trotter.grid_ham.inverse_sqrt._NR_INV_SQRT,
            qualtran.bloqs.chemistry.trotter.grid_ham.qvr._QVR,
            qualtran.bloqs.chemistry.trotter.grid_ham.kinetic._KINETIC_ENERGY,
            qualtran.bloqs.chemistry.trotter.grid_ham.potential._PAIR_POTENTIAL,
            qualtran.bloqs.chemistry.trotter.grid_ham.potential._POTENTIAL_ENERGY,
        ],
        directory=f'{SOURCE_DIR}/bloqs/chemistry/trotter',
    ),
    NotebookSpecV2(
        title='Tensor Hypercontraction',
        module=qualtran.bloqs.chemistry.thc,
        bloq_specs=[
            qualtran.bloqs.chemistry.thc.prepare._THC_UNI_PREP,
            qualtran.bloqs.chemistry.thc.prepare._THC_PREPARE,
            qualtran.bloqs.chemistry.thc.select_bloq._THC_SELECT,
        ],
        directory=f'{SOURCE_DIR}/bloqs/chemistry/thc',
    ),
    NotebookSpecV2(
        title='And',
        module=qualtran.bloqs.mcmt.and_bloq,
        bloq_specs=[
            qualtran.bloqs.mcmt.and_bloq._AND_DOC,
            qualtran.bloqs.mcmt.and_bloq._MULTI_AND_DOC,
        ],
        directory=f'{SOURCE_DIR}/bloqs/',
    ),
    NotebookSpecV2(
        title='Block Encoding',
        module=qualtran.bloqs.block_encoding,
        bloq_specs=[
            qualtran.bloqs.block_encoding._BLACK_BOX_BLOCK_BLOQ_DOC,
            qualtran.bloqs.block_encoding._CHEBYSHEV_BLOQ_DOC,
        ],
        directory=f'{SOURCE_DIR}/bloqs/',
    ),
    NotebookSpecV2(
        title='Reflection',
        module=qualtran.bloqs.reflection,
        bloq_specs=[qualtran.bloqs.reflection._REFLECTION_DOC],
        directory=f'{SOURCE_DIR}/bloqs/',
    ),
    NotebookSpecV2(
        title='Multi-Paulis',
        module=qualtran.bloqs.mcmt.multi_control_multi_target_pauli,
        bloq_specs=[
            qualtran.bloqs.mcmt.multi_control_multi_target_pauli._C_MULTI_NOT_DOC,
            qualtran.bloqs.mcmt.multi_control_multi_target_pauli._CC_PAULI_DOC,
        ],
        directory=f'{SOURCE_DIR}/bloqs/',
    ),
    # --------------------------------------------------------------------------
    # -----   Arithmetic   -----------------------------------------------------
    # --------------------------------------------------------------------------
    NotebookSpecV2(
        title='Addition',
        module=qualtran.bloqs.arithmetic.addition,
        bloq_specs=[
            qualtran.bloqs.arithmetic.addition._ADD_DOC,
            qualtran.bloqs.arithmetic.addition._ADD_OOP_DOC,
            qualtran.bloqs.arithmetic.addition._ADD_K_DOC,
        ],
    ),
    NotebookSpecV2(
        title='Sorting',
        module=qualtran.bloqs.arithmetic.sorting,
        bloq_specs=[
            qualtran.bloqs.arithmetic.sorting._COMPARATOR_DOC,
            qualtran.bloqs.arithmetic.sorting._BITONIC_SORT_DOC,
        ],
        directory=f'{SOURCE_DIR}/bloqs/arithmetic/',
    ),
    NotebookSpecV2(
        title='State Preparation Using Rotations',
        module=qualtran.bloqs.state_preparation.state_preparation_via_rotation,
        bloq_specs=[
            qualtran.bloqs.state_preparation.state_preparation_via_rotation._STATE_PREP_VIA_ROTATIONS_DOC
        ],
        directory=f'{SOURCE_DIR}/bloqs/state_preparation/',
    ),
    NotebookSpecV2(
        title='Multiplication',
        module=qualtran.bloqs.arithmetic.multiplication,
        bloq_specs=[
            qualtran.bloqs.arithmetic.multiplication._PLUS_EQUALS_PRODUCT_DOC,
            qualtran.bloqs.arithmetic.multiplication._PRODUCT_DOC,
            qualtran.bloqs.arithmetic.multiplication._SQUARE_DOC,
            qualtran.bloqs.arithmetic.multiplication._SUM_OF_SQUARES_DOC,
            qualtran.bloqs.arithmetic.multiplication._SCALE_INT_BY_REAL_DOC,
            qualtran.bloqs.arithmetic.multiplication._MULTIPLY_TWO_REALS_DOC,
            qualtran.bloqs.arithmetic.multiplication._SQUARE_REAL_NUMBER_DOC,
        ],
    ),
    NotebookSpecV2(
        title='Comparison',
        module=qualtran.bloqs.arithmetic.comparison,
        bloq_specs=[
            qualtran.bloqs.arithmetic.comparison._GREATER_THAN_DOC,
            qualtran.bloqs.arithmetic.comparison._GREATER_THAN_K_DOC,
            qualtran.bloqs.arithmetic.comparison._EQUALS_K_DOC,
        ],
    ),
    NotebookSpecV2(
        title='Conversions',
        module=qualtran.bloqs.arithmetic.conversions,
        bloq_specs=[
            qualtran.bloqs.arithmetic.conversions._SIGNED_TO_TWOS,
            qualtran.bloqs.arithmetic.conversions._TO_CONTG_INDX,
        ],
    ),
    NotebookSpecV2(
        title='Quantum Variable Rotation',
        module=qualtran.bloqs.rotations.quantum_variable_rotation,
        bloq_specs=[
            qualtran.bloqs.rotations.quantum_variable_rotation._QVR_ZPOW,
            qualtran.bloqs.rotations.quantum_variable_rotation._QVR_PHASE_GRADIENT,
        ],
        directory=f'{SOURCE_DIR}/bloqs/rotations/',
    ),
    NotebookSpecV2(
        title='Phasing via Cost function',
        module=qualtran.bloqs.rotations.phasing_via_cost_function,
        bloq_specs=[qualtran.bloqs.rotations.phasing_via_cost_function._PHASING_VIA_COST_FUNCTION],
        directory=f'{SOURCE_DIR}/bloqs/rotations/',
    ),
    # --------------------------------------------------------------------------
    # -----   QFT          -----------------------------------------------------
    # --------------------------------------------------------------------------
    NotebookSpecV2(
        title='Two Bit FFFT Gate',
        module=qualtran.bloqs.qft.two_bit_ffft,
        bloq_specs=[qualtran.bloqs.qft.two_bit_ffft._TWO_BIT_FFFT_DOC],
    ),
]


def render_notebooks():
    for nbspec in NOTEBOOK_SPECS:
        render_notebook(nbspec)


def check_all_bloqs_included():
    bspecs = get_bloqdocspecs()
    rendered_bspecs = []
    for nbspec in NOTEBOOK_SPECS:
        rendered_bspecs += [bspec for bspec in nbspec.bloq_specs]

    undoc = set(bspecs) - set(rendered_bspecs)
    if undoc:
        print("\nWarning: found a BloqDocSpec for these, but they're not in any NotebookSpecs:")
        for bspec in undoc:
            print('   ', bspec.bloq_cls.__name__)


if __name__ == '__main__':
    render_notebooks()
    check_all_bloqs_included()
