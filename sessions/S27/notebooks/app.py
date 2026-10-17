# app.py - a small Streamlit web app that uses a trained model.
#
# To run it on your laptop, open a terminal in this folder and type:
#     streamlit run app.py
# If "streamlit" is not found, type this instead:
#     python -m streamlit run app.py
#
# How Streamlit works: every time the user changes an input, this whole file
# runs again, from the first line to the last. So read it from top to bottom.
#
# IMPORTANT: this is a Python SCRIPT, not a notebook. Do not run it cell by
# cell, and do not run it inside a notebook. Run it in a terminal with the
# command shown above. (The session notebook writes this same file for you,
# so you do not need to copy it by hand.)

import streamlit as st          # the web-app library (the only new tool today)
import numpy as np              # to make the row of input numbers
import joblib                   # to load the saved model file from the notebook
from sklearn.datasets import load_iris   # only for the species names below


# --- Block 1: load the saved model (only once) ----------------------------- #
# @st.cache_resource tells Streamlit: run this function only ONCE, then keep
# the result in memory and use it again on every later run. Without it, the
# file would be loaded again on every click, and the app would be slow.
@st.cache_resource
def load_model():
    # Read the saved model file that the notebook made with joblib.dump.
    # The file is in the same folder as this script (and in the same repo),
    # so the file name alone is enough.
    return joblib.load("iris_model.joblib")


# Load the model, and the names of the three species.
model = load_model()
species_names = load_iris().target_names   # setosa, versicolor, virginica


# --- Block 2: the page heading --------------------------------------------- #
st.title("Iris flower classifier")
st.write(
    "Enter the four measurements of a flower (in centimetres). The model "
    "will guess its species. The model was trained once and saved. This app "
    "only loads the saved model and predicts."
)


# --- Block 3: collect the inputs from the user ----------------------------- #
# Each slider is one line. It gives back the number that the user chose.
# The sliders are in the sidebar on the left, so the page stays clean.
st.sidebar.header("Flower measurements")
sepal_length = st.sidebar.slider("Sepal length (cm)", 4.0, 8.0, 5.1)
sepal_width = st.sidebar.slider("Sepal width (cm)", 2.0, 4.5, 3.5)
petal_length = st.sidebar.slider("Petal length (cm)", 1.0, 7.0, 1.4)
petal_width = st.sidebar.slider("Petal width (cm)", 0.1, 2.5, 0.2)

# Show the inputs again, so the user can see the numbers the model used.
st.subheader("Your inputs")
st.write("Sepal length:", sepal_length, "cm")
st.write("Sepal width :", sepal_width, "cm")
st.write("Petal length:", petal_length, "cm")
st.write("Petal width :", petal_width, "cm")


# --- Block 4: predict, and show the answer --------------------------------- #
# The model needs a 2D array with one row per flower, so we make one row.
# The numbers MUST be in the same order as in training.
input_row = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

# Call the model. This is the f(x) step, the main job of the app.
predicted_number = model.predict(input_row)[0]
predicted_name = species_names[predicted_number]

# How sure the model is about the chosen species, as a percentage.
probabilities = model.predict_proba(input_row)[0]
confidence_percent = round(100 * probabilities[predicted_number], 1)

# Show the prediction in large text, with the confidence next to it.
st.subheader("Prediction")
st.metric(label="Predicted species", value=predicted_name)
st.write("Model confidence:", confidence_percent, "%")
