import streamlit as st
import streamlit_option_menu as som
import model
import home
import web
import contact
import time

if "selected_page" not in st.session_state:
    st.session_state.selected_page = "Home"

def render_page(selected_page):
    with st.spinner("Loading..."):
        time.sleep(1)
    if selected_page == "Home":
        home.show(update_page)
    elif selected_page == "Project":
        web.main()
    elif selected_page == "Contact":
        contact.show()
    elif selected_page == "Results":
        model.show()

def update_page(selected_page):
    st.session_state["selected_page"] = selected_page

options = ["Home", "Project","Results","Contact"]

selected_page = som.option_menu(
    key=st.session_state["selected_page"],
    menu_title=None,
    options=options,
    icons=["house","book","","envelope"],
    default_index=options.index(st.session_state["selected_page"]),
    orientation="horizontal",
    on_change=update_page
)
update_page(selected_page)
render_page(st.session_state.selected_page)