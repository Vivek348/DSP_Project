import streamlit as st

header=st.beta_container()
dataset=st.beta_container()
features=st.beta_container()
modeltraining=st.beta_container()
prediction=st.beta_container()

with header:
    st.title('Skin Disease Classification')