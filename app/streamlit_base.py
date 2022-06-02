# Core Pkg
import streamlit as st

def bases_streamlit():
    # streamlit features
    # TEXT
    # titre
    st.title("Streamlit crash course")

    # texte
    st.text("This is a text")

    # header \ subheader
    st.header("This is a header")
    st.subheader('This a subheader')

    # MARKDOWN
    st.markdown("## This is a markdown")

    # Link
    st.markdown('[link](https://google.com)')
    
    # Write HTML
    st.write("You can write HTML")
    html_page = """
    <div style="background-color:green;padding:50px">
        <p style="font-size:50px">Streamlit is awesome</p>
    </div>
    """
    st.markdown(html_page, unsafe_allow_html=True)
    
    #html_form = """
    #<div> 
    #    <form>
    #    <input type="text" name="firstname"/>
    #    </form>
    #</div>
    #"""
    #st.markdown(html_form, unsafe_allow_html=True)
    
    # Alert text
    st.write("Alert text")

    st.success("Success!")
    st.info("Iformation")
    st.warning("Un warning!")
    st.error("Une erreur")
    
    ## MEDIA
    # Image
    # import Image function
    from PIL import Image
    st.write("ouverture d'une image:")

    # open an image
    img = Image.open("OIP (2).jpeg")

    # Plot the image
    st.image(img, caption="DataScientest")
    
    # Audio
    #audio_file = open('name_of_file.ext', "rb")
    #audio_bytes = audio_file.read()
    #st.audio(audio_bytes, format="audio/mp3")
    
    # Video with URL
    st.subheader("une vidéo directement de YouTube:")
    st.video(data="https://www.youtube.com/watch?v=SNNK6z03TaA")
    
    ### WIDGET
    st.subheader("Let's talk about widgets")

    # Bouton
    st.button("Press ME")
    
    # getting interaction button
    if st.button("Appuyer"):
        st.success("Même pas mal!")
    
    # Checkbox
    if st.checkbox("Hide & seek"):
        st.success("showing")
    
    # Radio
    gender_list = ["Man", "Woman"]
    gender = st.radio("Sélectionner un genre", gender_list)
    if gender == gender_list[0]:
        st.info(f"gender is {gender}")
    
    # Select
    location = st.selectbox("Your Job", ["Data Scientist", "Dentist", "Doctor"])
    
    # Multiselect
    liste_course = st.multiselect("liste de course",
                                    ["tomates", "dentifrice", "écouteurs"])
    
    # Text imput
    name = st.text_input("your name", "your name here")
    st.text(name)
    
    # Number input
    age = st.number_input("Age", 5, 100)
    
    # text area
    message = st.text_area("Enter your message")
    
    # Slider
    niveau = st.slider("select the level", 2, 6)
    
    # Ballons
    if st.button("Press me again"):
        st.write("Yesss, you'r ready!")
        st.balloons()