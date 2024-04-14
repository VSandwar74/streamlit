import streamlit as st

st.markdown(
    """
    #Here's the default circuit we were given:

    ![Default Circuit](https://i.ibb.co/fFt6138/Screenshot-2024-04-14-at-9-57-23-AM.png)

    To optimize the QMC process, the quantum gates can be parallelized, reducing the maximum amount of gates per qubit path, 
    thus reducing circuit depth. The first step of this is to deconvolve the probability qubits into separate smaller sets of qubits
    which can be handled separately. We then use the qiskit prob functions from the finance subpackage.
    This allows us to benefit from the fact that lower numbers of qubits have drastically quicker runtimes because of the exponential nature. 
    The |0> qubits are rotated and handled at the same time separately to reach their desired state, and are then added together in QFT adder circuits. 
    This then reconvolves the computed amplitudes from each qubit, giving a distinction   
    While initially, this creates a high cost to computing and is less efficient than the original model, when scaled up to higher counts of qubits, 
    this approach has incredibly reduced circuit depth with a fifth of the circuit depth at 16 qubits.

    Our trade off is we use more auxillary qubits (about one for each interaction), but the depth of the circuit is significantly reduced.

    # And here's the implementation we designed:

    ![Small circuit](https://i.ibb.co/GH1LMPk/Screenshot-2024-04-14-at-11-59-50-AM.png)

    Note the use of adders in this circuit due to the powerful nature of the 
    QFT adder which scales linearly in depth with the number of qubits.
    ![Adder Table](https://ibb.co/hRMfGm5)

    """
)