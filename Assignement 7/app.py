import streamlit as st
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("🌸 Iris Flower Prediction App")

sepal_length = st.slider('Sepal Length', 4.0, 8.0, 5.8)
sepal_width = st.slider('Sepal Width', 2.0, 5.0, 3.0)
petal_length = st.slider('Petal Length', 1.0, 7.0, 4.0)
petal_width = st.slider('Petal Width', 0.1, 2.5, 1.2)

input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

if st.button('Predict'):
    prediction = model.predict(input_data)[0]
    probabilities = model.predict_proba(input_data)[0]
    species = ['Setosa', 'Versicolor', 'Virginica']

    st.success(f"Predicted Species: {species[prediction]}")

    prob_df = pd.DataFrame({'Species': species, 'Probability': probabilities})
    st.dataframe(prob_df)

    fig, ax = plt.subplots()
    sns.barplot(x='Species', y='Probability', data=prob_df, ax=ax)
    st.pyplot(fig)
