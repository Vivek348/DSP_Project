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
with modeltraining:
    st.title('CNN Model Architecture')
with prediction:
    st.title('Predicting the Skin Disease Type')
