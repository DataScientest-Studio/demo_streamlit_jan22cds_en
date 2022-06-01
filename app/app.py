# Core Pkg
import streamlit as st

# Custom modules
from streamlit_base import bases_streamlit # Basic streamlit function
from demo_stream_titanic import demo_streamlit # Basic ML web app with stremlit

def main():

    # List of pages
    liste_menu = ["bases streamlit", "demo_ML"]

    # Sidebar
    menu = st.sidebar.selectbox("selectionner votre activité", liste_menu)

    # Page navigation
    if menu == liste_menu[0]:
        bases_streamlit()
    else:
        demo_streamlit()


if __name__ == '__main__':
    main()