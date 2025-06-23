# -*- coding: utf-8 -*-
"""
Created on Mon Jun 23 10:25:02 2025
@author: Vraj
"""
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Load models
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('heart(logistic).sva', 'rb'))
parkinsons_model = pickle.load(open("parkinson(svm).sva", 'rb'))

# Sidebar menu
with st.sidebar:
    selected = option_menu(
        'Multiple Disease Prediction System',
        ['Diabetes Prediction', 'Heart Prediction', 'Parkinson'],
        icons=['activity', 'heart', 'person'],
        default_index=0
    )

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction')

    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Pregnancies:')
        SkinThickness = st.text_input('Skin Thickness:')
        BMI = st.text_input('BMI:')
    with col2:
        Glucose = st.text_input('Glucose:')
        Insulin = st.text_input('Insulin:')
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function:')
    with col3:
        BloodPressure = st.text_input('Blood Pressure:')
        Age = st.text_input('Age:')

    diagnosis = ''
    if st.button('Diabetes Result'):
        try:
            input_list = [
                float(Pregnancies), float(Glucose), float(BloodPressure),
                float(SkinThickness), float(Insulin), float(BMI),
                float(DiabetesPedigreeFunction), float(Age)
            ]
            prediction = diabetes_model.predict([input_list])[0]
            diagnosis = "✅ Diabetic" if prediction == 1 else "❌ Not Diabetic"
        except ValueError:
            diagnosis = "⚠️ Please enter valid numerical values in all fields."
        st.success(diagnosis)

# Heart Prediction Page
if selected == 'Heart Prediction':
    st.title('Heart Disease Prediction')

    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.text_input('Age:')
        cp = st.text_input('Chest Pain Type (cp):')
        chol = st.text_input('Cholesterol (chol):')
        restecg = st.text_input('Resting ECG (restecg):')
        slope = st.text_input('Slope of ST (slope):')
    with col2:
        sex = st.text_input('Sex (0 = female, 1 = male):')
        trestbps = st.text_input('Resting BP (trestbps):')
        fbs = st.text_input('Fasting Blood Sugar (fbs):')
        thalach = st.text_input('Max Heart Rate (thalach):')
        ca = st.text_input('Number of Major Vessels (ca):')
    with col3:
        exang = st.text_input('Exercise Induced Angina (exang):')
        oldpeak = st.text_input('Oldpeak:')
        thal = st.text_input('Thal (0 = normal, 1 = fixed defect, 2 = reversible defect):')

    diagnosis = ''
    if st.button('Heart Disease Result'):
        try:
            input_list = [
                float(age), float(sex), float(cp), float(trestbps),
                float(chol), float(fbs), float(restecg), float(thalach),
                float(exang), float(oldpeak), float(slope), float(ca),
                float(thal)
            ]
            prediction = heart_disease_model.predict([input_list])[0]
            diagnosis = "❤️ Heart Disease Detected" if prediction == 1 else "💚 No Heart Disease"
        except ValueError:
            diagnosis = "⚠️ Please enter valid numerical values in all fields."
        st.success(diagnosis)

# Parkinson’s Prediction Page
if selected == 'Parkinson':
    st.title("Parkinson’s Disease Prediction")

    col1, col2, col3 = st.columns(3)
    with col1:
        fo = st.text_input("MDVP:Fo(Hz)")
        jitter_abs = st.text_input("MDVP:Jitter(Abs)")
        ppq = st.text_input("MDVP:PPQ")
        shimmer = st.text_input("MDVP:Shimmer")
        apq5 = st.text_input("Shimmer:APQ5")
        dda = st.text_input("Shimmer:DDA")
        dfa = st.text_input("DFA")
        spread2 = st.text_input("Spread2")

    with col2:
        fhi = st.text_input("MDVP:Fhi(Hz)")
        jitter_percent = st.text_input("MDVP:Jitter(%)")
        rap = st.text_input("MDVP:RAP")
        shimmer_db = st.text_input("MDVP:Shimmer(dB)")
        apq = st.text_input("MDVP:APQ")
        nhr = st.text_input("NHR")
        rpde = st.text_input("RPDE")
        d2 = st.text_input("D2")

    with col3:
        flo = st.text_input("MDVP:Flo(Hz)")
        ddp = st.text_input("Jitter:DDP")
        apq3 = st.text_input("Shimmer:APQ3")
        hnr = st.text_input("HNR")
        spread1 = st.text_input("Spread1")
        ppe = st.text_input("PPE")

    diagnosis = ''
    if st.button('Check Parkinson’s Result'):
        try:
            input_features = [
                float(fo), float(fhi), float(flo), float(jitter_percent),
                float(jitter_abs), float(rap), float(ppq), float(ddp),
                float(shimmer), float(shimmer_db), float(apq3), float(apq5),
                float(apq), float(dda), float(nhr), float(hnr),
                float(rpde), float(dfa), float(spread1), float(spread2),
                float(d2), float(ppe)
            ]
            prediction = parkinsons_model.predict([input_features])[0]
            diagnosis = "🧠 Parkinson's Detected" if prediction == 1 else "✅ No Parkinson's"
        except ValueError:
            diagnosis = "⚠️ Please enter valid numerical values in all fields."
        st.success(diagnosis)
