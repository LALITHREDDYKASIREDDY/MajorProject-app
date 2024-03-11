import streamlit as st
from joblib import load
import project
import time
from sklearn.preprocessing import StandardScaler
import os


def main():
    script_directory = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(script_directory, "xgboost_model.pkl")
    model = load(model_path)
    st.header("Water Quality Monitoring System")
    input_data = project.fun()
    container = st.container(border=True)
    container.header("Water Paramters")
    childContainer=container.container(border=True)
    col1,col2,col3=childContainer.columns(3)
    with col1:
        st.write("Ph")
        st.container().write(input_data[0])
    with col2:
        st.write("Turbidity")
        st.container().write(input_data[1])
    with col3:
        st.write("Total Dissolved Solids")
        st.container().write(input_data[2])
    col4,col5,col6=childContainer.columns(3)
    with col4:
        st.write("Temperature")
        st.container().write(0)
    with col5:
        st.write("Electrical Conductivity")
        st.container().write(0)
    childContainer2=container.container(border=True)
    with col6:
        st.write("Disolved Oxygen")
        st.container().write(0)
    childContainer2=container.container(border=True)
    col1,col2,col3=childContainer2.columns(3)

    with col2:
        st.subheader("Prediction")
    
        with st.spinner("predicting"):
            print(input_data)
            scaler = StandardScaler()
            prediction=model.predict(scaler.fit_transform([input_data]))
            print(prediction)
            time.sleep(1)
        st.write("Not Drinkable" if prediction[0]==0 else "Drinkable")

    