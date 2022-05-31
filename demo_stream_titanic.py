# Core Pkg
import pandas as pd 
import seaborn as sns 
import streamlit as st 
import matplotlib.pyplot as plt 
import numpy as np 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

# Custom function
@st.cache
def train_model(model_choisi, X_train, y_train, X_test, y_test) :
    if model_choisi == 'Regression Logisitic' : 
        model = LogisticRegression()
    elif model_choisi == 'Decision Tree' : 
        model = DecisionTreeClassifier()
    elif model_choisi == 'KNN' : 
        model = KNeighborsClassifier()
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)
    return score

def demo_streamlit():
    ### Mettre des titres
    st.title("mon premier streamlit en machien learning")

    st.subheader("par Emilie, Fred et... DataScientest")

    ### Mettre une image 

    st.image("titanic.jpeg")


    ### Mettre du markdown 

    st.markdown("## Nous allons utilisé les données des passagers du titanic")

    ### Lecture du fichier csv et affichage 

    df = pd.read_csv('titanic.csv')


    ### Mettre du code 
    st.text("import des données avec la commande: ")
    with st.echo(): 
        df = pd.read_csv('titanic.csv')


    ### Afficher les données 

    if st.checkbox("Afficher les données") : 
        st.dataframe(df)

    if st.checkbox("Afficher les données manquantes") : 
        st.dataframe(df.isna().sum())


    ### Preprocessing 


    df = df.dropna()

    df = df.drop(['sex', 'title', 'cabin', 'embarked'], axis = 1)

    y = df['survived']

    X = df.drop('survived', axis =1 )

    train_size = st.sidebar.slider(label = "Choix de la taille de l'échantilllon de train", min_value = 0.2, max_value = 1.0, step = 0.05)

    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = train_size)


    ### Afficher un graphique 

    st.text('Graphique')

    st.set_option('deprecation.showPyplotGlobalUse', False)

    sns.countplot(df['pclass'])

    st.pyplot()
    ### Classification 


    model = LogisticRegression() 

    model.fit(X_train, y_train)

    st.write("Score test with logisitic regression" , model.score(X_test,y_test))



    model_choisi = st.selectbox(label = "choix de modèle" , options = ['Regression Logisitic', 'Decision Tree', 'KNN'])


    # Entrainement du dmoèle
    st.write("Score test", train_model(model_choisi, X_train, y_train, X_test, y_test))