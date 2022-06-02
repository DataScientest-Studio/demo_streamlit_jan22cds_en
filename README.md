# Streamlit Demo

## Why Streamlit:
The classic data science workflow is as follows:

![Workflow_data_scientist](/assets/streamlit_1.png "Pipeline MLOPS")

**Streamlit** is a python library (often referred to as a framework) that allows you to create beautiful graphical application interfaces in a very short time.

Streamlit acts **as a web interface** between the Python language and other libraries (e.g. HTML, CSS, Javascript, etc).

From the moment we want to create a graphical user interface, we can use Streamlit to visually communicate with the various stakeholders in the company.

## General information about Streamlit:
Some possibilities with streamlit:

![Fonctions de streamlit](/assets/streamlit_2.png)

## Streamlit installation:

What you will need:
* Text editor
* Installation command below:

``` python
Pip install streamlit 
#(pipenv install streamlit dans une environnement virtuel)
```

## Methodology for developing an application:

A possible working methodology:

1. **Design of the application window**: 

The first step is the design of the application window (see below).

![Visuel de l'application](/assets/streamlit_3.png)

→ Be imaginative: Imagine the 'look' of your future app (colours, layouts, menus, content etc.)

2. **Designing the architecture**:

The second step **is not writing lines of code** but designing the architecture of the application.

Draw the relationships between a set of files (design of the code directory architecture).

*Ex:*

![File relationship](/assets/streamlit_4.png)

Once you have the window and the architecture in mind, it is easier to write the corresponding code.

## How to launch the demo:

1. **Go to the app directory:**

``` bash
# Change directory
cd app
```
2. **Run the `app.py` script:**

``` python
# Run streamlit app
streamlit run app.py
```

## Exploration de streamlit:
Go demo 👉

## Additionnal ressources:
___
1. https://docs.streamlit.io/library/get-started/main-concepts
2. https://docs.streamlit.io/streamlit-cloud/get-started/deploy-an-app
3. [Streamlit example](https://towardsdatascience.com/streamlit-hands-on-features-and-tips-for-enhanced-app-user-experience-aef7be8035fa#:~:text=Streamlit%20is%20a%20free%2C%20open-source%2C%20all-python%20framework%20that,gained%20popularity%20among%20data%20science%20practitioners%20and%20enthusiasts.)

By SSIME - DataScientest
