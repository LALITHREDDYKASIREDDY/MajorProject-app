import streamlit as st
import web
import time

def show(update_page):
    st.title("Water Quality Monitorng System")
    st.divider()
    st.header("Introduction")
    paragraph="Rising population, pollution, and climate change are depleting safe water resources. Traditional water quality testing is manual, costly, and lacks real-time feedback. Wireless sensor network (WSN) systems face issues with energy, security, and coverage. IoT offers more efficient, secure, and real-time monitoring solutions. By leveraging IoT, we aim to overcome WSN limitations for water quality monitoring. Real-time data on water quality parameters will be available on a monitoring website. This ensures timely action to maintain acceptable water quality levels."
    st.write(paragraph)
    if st.button("Let's Go"):
        st.session_state["selected_page"] = "Project"
        st.rerun()
            