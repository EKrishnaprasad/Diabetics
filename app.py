import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import pickle
df=pd.read_csv('diabetes.csv')
clf=open('rfc.pickle', 'rb')
st.title('web deployment of medical diagnostic app')
st.subheader('is the person diabetic?')
st.set_option('deprecation.showPyplotGlobalUse', False)
if st.sidebar.checkbox('View Data',False):
    st.write(df)
    st.pyplot()
if st.sidebar.checkbox('view distribution',False):
    df.hist()
    plt.tight_layout()
    #df.barplot()
    st.pyplot()
model = open('rfc.pickle','rb')
rfc=pickle.load(model)
clf.close()
pregs=st.number_input('Pregnancies',0,17,0)
glu=st.slider('Glucose',44,199,44)
bp=st.slider('BloodPressure',20,140,20)
skin=st.slider('SkinThickness',7,99,7)
ins=st.slider('Insulin',14,850,14)
bmi = st.slider('BMI',18,67,10)
dbp=st.slider('DiabetesPedigreeFunction',0.07,2.8,0.07)
age=st.slider('Age',21,85,21)
data = [[pregs,glu,bp,skin,ins,bmi,dbp,age]]
if st.button('Predict'):
    if rfc.predict(data)[0] ==1:
        st.subheader('You have Diabetes')
    else:
        st.subheader("You don't have Diabetes")
