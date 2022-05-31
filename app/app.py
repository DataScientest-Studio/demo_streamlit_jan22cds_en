# Core Pkg
import streamlit as st

# custom pkg
from streamlit_base import bases_streamlit
from demo_stream_titanic import demo_streamlit

def main():
    liste_menu = ["bases streamlit", "demo_ML"]
    menu = st.sidebar.selectbox("selectionner votre activité", liste_menu)
    if menu == liste_menu[0]:
        bases_streamlit()
    else:
        demo_streamlit()



if __name__ == '__main__':
    main()