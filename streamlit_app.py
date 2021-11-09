import streamlit as st

header=st.container()
dataset=st.container()
features=st.container()
modeltraining=st.container()
prediction=st.container()

with header:
    st.title('Skin Disease Classification')
with dataset:
    st.title('Skin Disease Image Classification sample')
with features:
    st.title('lesion_id,image_id,type,age,sex,localization')
    age = st.number_input("Age", min_value=18, max_value=100, step=1)
with modeltraining:
    st.title('CNN Model Architecture')
with prediction:
    st.title('Predicting the Skin Disease Type')
