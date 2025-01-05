import streamlit as st
import math
import pickle

model=pickle.load(open('LogisticRegression_model1.pkl','rb'))

st.header("Titanic Survival Prediction")

# Input fields for passenger details
col1, col2, col3 = st.columns(3)
with col1:
    Pclass = st.selectbox("Class of Passenger", ("Premiere", "Executive", "Economy"))
with col2:
    Sex = st.selectbox("Gender", ("Male", "Female"))
with col3:
    Age = st.number_input("Age of passenger", min_value=0)

col4, col5 = st.columns(2)
with col4:
    SibSp = st.number_input("Siblings/Spouses", min_value=0)
with col5:
    Parch = st.number_input("Parents/Children", min_value=0)

col7, col8 = st.columns(2)
with col7:
    Fare = st.number_input("Fare of Journey", min_value=0.0)
with col8:
    Embarked = st.selectbox("Picking Point", ("Cherbourg", "Queenstown", "Southampton"))

# Prediction button
if st.button("Predict"):
   pclass = 1 
   if Pclass=="Economy": 
    pclass = 3 
    if Pclass=="Executive":
      pclass = 2

    # Convert Sex to numerical value
    gender = 0
    if Sex == "Female":
     gender = 1

    age = float(Age)  # Keep as float
    sibsp = float(SibSp)  # Keep as float
    parch = float(Parch)  # Keep as float
    fare = float(Fare)  # Keep as float

    # Convert Embarked to numerical value
    embarked = 0
    if Embarked == "Queenstown": 
        embarked = 1 
    elif Embarked == "Southampton": 
        embarked = 2

    # Make prediction
    result = model.predict([[pclass, gender, age, sibsp, parch, fare, embarked]])
    
    # Output labels
    output_labels = {1: "The passenger will Survive", 
                     0: "The passenger will not survive"}
    
    st.markdown(f"## {output_labels[result[0]]}")
    