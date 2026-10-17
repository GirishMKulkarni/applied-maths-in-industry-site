# app.py - a tiny Streamlit web app that serves a trained model.
#
# Run it locally from this folder with:
#     streamlit run app.py
#
# Streamlit's mental model: this whole script runs again, top to bottom, every
# time the user changes an input. So we read the script like a recipe.
#
# IMPORTANT: this is a plain Python SCRIPT, not a notebook. Do not run it cell
# by cell, and do not run it inside a notebook. Run it with the
# "streamlit run app.py" command shown above. (The session notebook also writes
# this exact file to disk for you, so you never have to copy it by hand.)

import streamlit as st          # the web-app library (the only new tool here)
import numpy as np              # to build the input row of numbers
import joblib                   # to load the model file we saved in the notebook
from sklearn.datasets import load_iris   # only for the species names below


# --- Block 1: load the trained model (once) -------------------------------- #
# @st.cache_resource tells Streamlit: run this function only ONCE, then reuse
# its result on every later rerun. Without it, the file would be re-read on
# every click, which is slow and wasteful.
@st.cache_resource
def load_model():
    # Read the model we saved in the notebook with joblib.dump.
    # The file sits next to this script in the repo, so a plain name works.
    return joblib.load("iris_model.joblib")


# Load the model and the human-readable species names.
model = load_model()
species_names = load_iris().target_names   # e.g. setosa, versicolor, virginica


# --- Block 2: the page heading --------------------------------------------- #
st.title("Iris flower classifier")
st.write(
    "Enter a flower's four measurements (in centimetres) and the model will "
    "guess its species. The model was trained once and saved; this app just "
    "loads it and predicts."
)


# --- Block 3: collect the inputs from the user ----------------------------- #
# Each slider is one function call that returns the number the user chose.
# We put the sliders in the sidebar to keep the page tidy.
st.sidebar.header("Flower measurements")
sepal_length = st.sidebar.slider("Sepal length (cm)", 4.0, 8.0, 5.1)
sepal_width = st.sidebar.slider("Sepal width (cm)", 2.0, 4.5, 3.5)
petal_length = st.sidebar.slider("Petal length (cm)", 1.0, 7.0, 1.4)
petal_width = st.sidebar.slider("Petal width (cm)", 0.1, 2.5, 0.2)

# Echo the inputs back so the user can see exactly what was used.
st.subheader("Your inputs")
st.write("Sepal length:", sepal_length, "cm")
st.write("Sepal width :", sepal_width, "cm")
st.write("Petal length:", petal_length, "cm")
st.write("Petal width :", petal_width, "cm")


# --- Block 4: predict and display the answer ------------------------------- #
# The model expects a 2D array with one row per flower, so we make one row.
# The order of the numbers MUST match the order used during training.
input_row = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

# Call the model: this is the f(x) step, the whole point of the app.
predicted_number = model.predict(input_row)[0]
predicted_name = species_names[predicted_number]

# How confident the model is, as a percentage for the chosen species.
probabilities = model.predict_proba(input_row)[0]
confidence_percent = round(100 * probabilities[predicted_number], 1)

# Show the prediction big and clear, with its confidence as context.
st.subheader("Prediction")
st.metric(label="Predicted species", value=predicted_name)
st.write("Model confidence:", confidence_percent, "%")
