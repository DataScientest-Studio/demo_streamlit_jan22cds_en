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
# st.cache is used to load the function into memory
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

    ### Create Title
    st.title("Streamlit Machine Learning Web app with Streamlit")
    st.header("The beginning of a great adventure")
    st.subheader("By DataScientest team")

    ### Add a picture
    st.write("Below is a picture of the Titanic:")
    st.image("titanic.jpeg")


    ### using Markdown
    st.markdown("### We will use the well famous titanic dataset for our study. Can we predict who survived?")

    ### reading dataset
    # Normally, you will store all the necessary path and env variables in a .env file
    dataset_path = '../data/titanic.csv'
    df = pd.read_csv(dataset_path)


    ### Showing code
    st.text("importing dataset with the folowing command: ")
    with st.echo(): 
        df = pd.read_csv(dataset_path)


    ### Showing the data
    if st.checkbox("Showing the data") :
        line_to_plot = st.slider("select le number of lines to show", min_value=3, max_value=df.shape[0])
        st.dataframe(df.head(line_to_plot))

    if st.checkbox("Missing values") : 
        st.dataframe(df.isna().sum())


    ### Preprocessing 

    # Drop Missing values
    df = df.dropna()

    # Drop some columns
    df = df.drop(['sex', 'title', 'cabin', 'embarked'], axis = 1)

    # Select the target
    y = df['survived']

    # Select the features
    X = df.drop('survived', axis =1 )

    # select how to split the data
    train_size = st.sidebar.slider(label = "Choix de la taille de l'échantilllon de train", min_value = 0.2, max_value = 1.0, step = 0.05)

    # Splitting the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = train_size)


    ### Display graph
    st.text('Class distribution with seaborn')
    st.set_option('deprecation.showPyplotGlobalUse', False)
    sns.countplot(df['pclass'])
    st.pyplot()

    ### Classification 

    #  Baseline model
    model = LogisticRegression() 

    # Model training
    model.fit(X_train, y_train)

    # Benchmark Model evaluation
    st.write("Logisitic regression accuracy (This is my Benchmark):" , model.score(X_test,y_test))

    # Other models
    model_list = ['Decision Tree', 'KNN']
    model_choisi = st.selectbox(label = "Select a model" , options = model_list)


    # Showing the accuracy for the orthers models (for comparison)
    st.write("Accuracy for some models for comparison: ")
    st.write("Score test", train_model(model_choisi, X_train, y_train, X_test, y_test))