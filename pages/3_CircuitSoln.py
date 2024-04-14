import streamlit as st

st.markdown(
    """
    #Here's the default circuit we were given:

    ![Default Circuit](../../default_circuit.png)

    # And here's the implementation we designed:

    
    Note the use of adders in this circuit due to the powerful nature of the 
    QFT adder which scales linearly in depth with the number of qubits.
    ![Adder Table](../../adders.png)
    
    """
)