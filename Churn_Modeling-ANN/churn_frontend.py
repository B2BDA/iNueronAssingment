# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st
import pickle
import numpy as np
from tensorflow.keras.models import load_model
from numpy import hstack
model = load_model('churn.h5')
scl = pickle.load(open('scaling.pkl','rb'))
geo_lbl = pickle.load(open('Geography_step_0.pkl','rb'))
geo_ohe = pickle.load(open('Geography_step_1.pkl','rb'))
gender_ohe = pickle.load(open('Gender_one_h_enc_.pkl','rb'))

def main():
    st.markdown("""
    <div style ="background-color:orange;padding:13px">
    <h1 style ="color:black;text-align:center;">Churn Prediction DL App </h1>
    </div>
    """, unsafe_allow_html = True)

    st.header("Enter Customer Data")

    CreditScore = st.text_input("Enter CreditScore")
    Geography = st.text_input("Enter Geography")
    Gender = st.text_input("Enter Gender")
    Age = st.text_input("Enter Age")
    Tenure = st.text_input("Enter Tenure")
    Balance = st.text_input("Enter Balance")
    NumOfProducts = st.text_input("Enter NumOfProducts")
    HasCrCard = st.text_input("Enter HasCrCard")
    IsActiveMember = st.text_input("Enter IsActiveMember")
    EstimatedSalary = st.text_input("Enter EstimatedSalary")
    if (Geography != '') and (Gender != ''):
        geo_in = geo_ohe.transform(geo_lbl.transform([Geography]).reshape(-1,1)).toarray()

        gender_in = gender_ohe.transform(np.array(Gender).reshape(-1,1)).toarray()

        input_data = []
        for i in [int(CreditScore), int(Age), int(Tenure), float(Balance), int(NumOfProducts), int(HasCrCard), int(IsActiveMember),float(EstimatedSalary)]:
            input_data.append(i)
        print(input_data)
        input_data = hstack((np.array(input_data).reshape(-1,8), geo_in[0].reshape(1,-1), gender_in[0].reshape(1,-1)))
        input_data = scl.transform(input_data)

        if st.button("Sumbit") == True:
            prediction = model.predict_classes(input_data)
            print(prediction)
            prediction_label = {0:'Low Churn Probability', 1:'High Churn Probability'}
            st.write(prediction_label.get(prediction[0][0]))

if __name__=="__main__":
    main()