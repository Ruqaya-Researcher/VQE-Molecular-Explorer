
import numpy as np

from scipy.optimize import minimize


def cost_function(

    parameters,

    ansatz,

    hamiltonian,

    estimator

):

    pub = (

        ansatz,

        [hamiltonian],

        [parameters]

    )

    result = estimator.run([pub]).result()

    energy = result[0].data.evs[0]

    return energy


def run_vqe(

    hamiltonian,

    ansatz,

    optimizer,

    estimator

):

    initial_parameters = np.random.random(

        ansatz.num_parameters

    ) * 2 * np.pi

    result = minimize(

        cost_function,

        initial_parameters,

        args=(

            ansatz,

            hamiltonian,

            estimator

        ),

        method=optimizer["method"],

        options=optimizer["options"]

    )

    return result
