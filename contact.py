import streamlit as st

def Container(name,email_id,git):
    container=st.container(border=True)
    container.subheader(name)
    container.write("Email:{}".format(email_id))
    container.markdown("GitHub:"+git)
    return container
    

def show():
    st.header("Source Code")
    st.write("This project was completed in fulfillment of the major project requirement.")
    st.write("For source code, please visit the below link...")
    github_url = "https://github.com/LALITHREDDYKASIREDDY/MajorProject-app"
    st.markdown(f"[View source code on GitHub]({github_url})")
    st.header("Contact Us")
    st.write("For any queries:")
    col1,col2,col3=st.columns(3)
    with col1:
        Container("Lalith Reddy","@gmail.com",github_url)
    with col2:
        col2=Container("Pranay raj","@gmail.com",github_url)
    with col3:
        col3=Container("Rohith","@gmail.com",github_url)