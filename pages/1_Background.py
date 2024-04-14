import streamlit as st

st.markdown(
    '''
    # The Classical Monte Carlo
    The Monte Carlo System is the repeated simulated sampling of various events to predict expected results. It is used widely in various industries including finance and insurance, with its application specifically in estimating the risk associated with certain assets in extreme and typical scenarios. In typical computing, however, this process is incredibly expensive due to the high computations necessary to set up each simulation.

    # The Shift to Quantum Monte Carlo Simulation
    In quantum computing, the usage of qubits and superposition enables these simulations to compute faster by using the probability of various combinations of qubit states as amplitudes that form a distribution of possibilities. The problem that then arises is the exponential increase in circuit depth that results from this. Circuit depth is the maximum number of quantum gates used on a single qubit path and represents the time needed to make these computations. As more qubits are used in the simulation, the circuit depth increases exponentially, making the benefits of the quantum model fade once scaled.

    '''
)