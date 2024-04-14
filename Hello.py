import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to Team Dead or Alive's Submission! 👋")

st.sidebar.success("Choose a screen to visit")

st.markdown(
    """
    ### Overview: 

    Over the last four hours we were tasked with taking the Quantum Monte Carlo algorithm and optimizing it. We took this as
    minimizing the depth of the circuit which performed the actual operation. 

    ### Use Case:
    In the Capgemini/Hartform/Quantinuum challenge we're concentrated on a specific use case–the insurance industry. Thus with these assumtpions 
    in hand, our goal was to minimize the depth while utilizing a reasonable amount of ancillary/auxillary quibits.

    ### Our Approach:
    At a high level we studied the theory behind the classical algorithm and the quantum algorithm given to us. We then proceeded to
    solve some problems with the scaling as the qubits increased, using concepts such as convolutions to 

"""
)