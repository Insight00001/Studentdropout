import streamlit as st
from sklearn.preprocessing import StandardScaler
import pandas as pd
import joblib
import numpy as np
df = pd.read_csv('cleaned_data.csv')

def preprocess_data(data):
    scaler = StandardScaler()
    scaler.fit(data)
    scale = scaler.transform(data)
    return scale
def make_prediction(data):
    model = joblib.load('XGBoost.pkl')
    data = preprocess_data(data)
    return model.predict(data)

def pad_features(data,number_features=36,default_value=0):
    if len(data)<number_features:
        data = data + [default_value]*(number_features-len(data))
    return data


st.set_page_config(page_title='Predict Student Dropout',
                   page_icon='bar_chart',
                   layout = 'centered',

                   )
st.title("Student Dropout Prediction")
st.divider()
student_name=st.text_input('Enter your name')

application_model = st.selectbox('Select your Application mode',df['Application mode'].unique())
course = st.selectbox('Select your course',df['Course'].unique())
tution = st.selectbox('Select your tuition fee status',df['Tuition fees up to date'].unique())
gender = st.selectbox('Select Your Gender',df['Gender'].unique())
scholarship = st.selectbox('Select scholarship status',df['Scholarship holder'].unique())
curricular_1st_enrolled = st.selectbox("Select your curricular units for first semester(enrolled)",df['Curricular units 1st sem (enrolled)'].unique())
curricular_1st_evaluate = st.selectbox("Select your curricular units for first semester(evaluate)",df['Curricular units 1st sem (evaluations)'].unique())
curricular_1st_approved = st.selectbox("Select your curricular units for first semester(approved)",df['Curricular units 1st sem (approved)'].unique())
curricular_1st_grade = st.text_input("Enter your grade for first semester")
curricular_2nd_credited = st.selectbox("Select your credit units for 2nd semester credit",df['Curricular units 2nd sem (credited)'].unique())
curricular_2nd_enrolled = st.selectbox("Select your units for 2nd semester enrolled",df['Curricular units 2nd sem (enrolled)'].unique())
curricular_2nd_evaluations = st.selectbox("Select your units for 2nd semester evaluations",df['Curricular units 2nd sem (evaluations)'].unique())
curricular_2nd_approved = st.selectbox("Select your credit units for 2nd semester approved",df['Curricular units 2nd sem (approved)'].unique())
curricular_2nd_grade = st.text_input("Enter your grade for 2nd semester")

try:
    data_entry = [int(application_model),int(course),int(tution),int(gender),int(scholarship),int(curricular_1st_enrolled),
                 int(curricular_1st_evaluate),int(curricular_1st_approved),float(curricular_1st_grade),int(curricular_2nd_credited),int(curricular_2nd_enrolled),
                 int(curricular_2nd_evaluations),int(curricular_2nd_approved),float(curricular_2nd_grade)]
    data_entry = pad_features(data_entry)
    data_entry = np.array(data_entry).reshape(1,-1)
    

except Exception as e:
    # Handle the exception and show the error message
    st.error(f"Fill in all fields: {e}")
    data_entry = None
  


pred = st.button('Click to predict')
if pred:
    ans = make_prediction(data_entry)
    if ans==0:
        st.write(student_name + ' you might Dropout')
    elif ans==1:
        st.write(student_name + ' you are Enrolled')
    else:
        st.write(student_name +  ' you are likely going to Graduate')
