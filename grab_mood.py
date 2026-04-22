import streamlit as st

def grab_recommendation():

    dict = {
        "Genre": "Film",
        "Subgenre": "comedy/animation",
        "Title": "The Lego Movie",
        "details": 
        {
            "Director": "Phil Lord, Christopher Miller",
            "Release Year": 2014,
            "Rating": 7.7,
            "Synopsis": "An ordinary Lego construction worker, thought to be the prophesied 'Special', is recruited to join a quest to stop an evil tyrant from gluing the Lego universe into eternal stasis.",
            "imdb_link": "https://www.imdb.com/title/tt1490017/"
        }
    }

    return dict
    

def display_card():
    recommendation = grab_recommendation()

    
    st.markdown(f"### {recommendation['Title']} ({recommendation['details']['Release Year']})")

    st.image(r"C:\Users\Brend\Documents\HCI-Final\Lego_movie.jpg", width=300)
    st.markdown(f"**Genre:** {recommendation['Genre']} - {recommendation['Subgenre']}")
    st.markdown(f"**Director:** {recommendation['details']['Director']}")
    st.markdown(f"**Rating:** {recommendation['details']['Rating']}/10")
    st.markdown(f"**Synopsis:** {recommendation['details']['Synopsis']}")
    st.markdown(f"[More info on IMDb]({recommendation['details']['imdb_link']})")