import random

import streamlit as st

def grab_recommendation(number):
    print(st.session_state['saved_mood'])
    if st.session_state['saved_mood'].lower() in ["happy", "joyful", "excited"]:
        if number == 1:
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
                "link": "https://www.imdb.com/title/tt1490017/",
            },
            "Image Link": "images/Lego_movie.jpg"
            }

        if number == 2:
            dict = {
                "Genre": "TV Show",
                "Subgenre": "comedy",
                "Title": "Parks and Recreation",
                "details":
                {
                    "Director": "Greg Daniels, Michael Schur",
                    "Release Year": 2009,
                    "Rating": 8.6,
                    "Synopsis": "The absurd antics of an Indiana town's public officials as they pursue sundry projects to make their city a better place.",
                    "link": "https://www.imdb.com/title/tt1266020/"
                },
                "Image Link": "images/parks_recs.jpg"
            }
        
        if number == 3:
            dict = {
                "Genre": "Book",
                "Subgenre": "fiction",
                "Title": "The Rosie Project",
                "details":
                {
                    "Director": "Graeme Simsion",
                    "Release Year": 2013,
                    "Rating": 4.1,
                    "Synopsis": "Don Tillman, a brilliant yet socially awkward professor of genetics, has decided it's time he found a wife. In the orderly, evidence-based manner with which he approaches all things, he designs the Wife Project to find his perfect partner: a sixteen-page questionnaire that covers everything from a potential partner's susceptibility to seasickness to her favorite type of cheese. Rosie Jarman is everything Don is not looking for: fiery, spontaneous, and a heavy drinker. But when Rosie enlists Don's help to find her biological father, Don's orderly life is thrown into chaos, and the two embark on a project that is equal parts DNA research and dating.",
                    "link": "https://www.goodreads.com/book/show/16181778-the-rosie-project"},
                "Image Link": "images/The_Rosie_Project.jpg",
            }
                
            

    
    elif st.session_state['saved_mood'].lower() in ["sad", "down", "depressed", "heartbroken", "bored", "lonely"]:
        if number == 1:
            dict = {
                "Genre": "TV Show",
                "Subgenre": "drama",
                "Title": "BoJack Horseman",
                "details":
                {
                    "Director": "Raphael Bob-Waksberg",
                    "Release Year": 2014,
                    "Rating": 8.7,
                    "Synopsis": "BoJack Horseman was the star of the hit TV show 'Horsin' Around' in the 90s, but now he's washed up, living in a nice house, and addicted to booze. He decides to make a comeback by writing a tell-all autobiography with the help of his ghostwriter, Diane Nguyen.",
                    "link": "https://www.imdb.com/title/tt3398228/"
                },
                "Image Link": "images/Bojack_Horseman.jpg"
            }
        if number == 2:
            dict = {
                "Genre": "Film",
                "Subgenre": "drama/romance",
                "Title": "Eternal Sunshine of the Spotless Mind",
                "details":
                {
                    "Director": "Michel Gondry",
                    "Release Year": 2004,
                    "Rating": 8.3,
                    "Synopsis": "When their relationship turns sour, a couple undergoes a medical procedure to have each other erased from their memories.",
                    "link": "https://www.imdb.com/title/tt0338013/"
                },
                "Image Link": "images/eternal_sunshine.jpg"
            }
        
        if number == 3:
            dict = {
                "Genre": "Book",
                "Subgenre": "fiction",
                "Title": "The Perks of Being a Wallflower",
                "details":
                {
                    "Director": "Stephen Chbosky",
                    "Release Year": 1999,
                    "Rating": 4.2,
                    "Synopsis": "The Perks of Being a Wallflower is a coming-of-age novel that follows the story of Charlie, a socially awkward high school freshman who is struggling to find his place in the world. Through a series of letters to an anonymous friend, Charlie shares his experiences with friendship, love, and mental health as he navigates the challenges of adolescence.",
                    "link": "https://www.goodreads.com/book/show/22628.The_Perks_of_Being_a_Wallflower"
                },
                "Image Link": "images/perks.jpg"
            }
        
    else:
        dict = {
                "Genre": "Book",
                "Subgenre": "fiction",
                "Title": "The Perks of Being a Wallflower",
                "details":
                {
                    "Director": "Stephen Chbosky",
                    "Release Year": 1999,
                    "Rating": 4.2,
                    "Synopsis": "The Perks of Being a Wallflower is a coming-of-age novel that follows the story of Charlie, a socially awkward high school freshman who is struggling to find his place in the world. Through a series of letters to an anonymous friend, Charlie shares his experiences with friendship, love, and mental health as he navigates the challenges of adolescence.",
                    "link": "https://www.goodreads.com/book/show/22628.The_Perks_of_Being_a_Wallflower"
                },
                "Image Link": "images/perks.jpg"
            }

    return dict
    

def display_recommendation(number):
    if "saved_mood" not in st.session_state or not st.session_state["saved_mood"]:
        st.warning("Please enter a mood first.")
        return

    recommendation = grab_recommendation(number)

    st.markdown(
        f"<h2 style='text-align:center; margin-bottom: 12px;'>{recommendation['Title']}</h2>",
        unsafe_allow_html=True
    )

    image_col, info_col = st.columns([1.25, 1])

    with image_col:
        st.image(recommendation["Image Link"], use_container_width=True)

    with info_col:
        st.caption("Genre:")
        st.markdown(f"### {recommendation['Genre']}")

        st.caption("Subgenre:")
        st.write(recommendation["Subgenre"])

        st.caption("Details:")
        st.write(f"• {recommendation['details']['Release Year']}")
        st.write(f"• {recommendation['details']['Director']}")
        st.write(f"• {recommendation['details']['Rating']}/10")

    st.markdown("---")

    st.caption("Synopsis")
    st.write(recommendation["details"]["Synopsis"])

    st.link_button(
        "More Info",
        recommendation["details"]["link"],
        use_container_width=True
    )

    reaction_col1, reaction_col2, reaction_col3 = st.columns(3)

    with reaction_col1:
        st.caption("Not Feeling It 🔴")
        if st.button("👎", key=f"bad_{number}", use_container_width=True):
         
            st.session_state["recommendation_number"] += 1

            if st.session_state["recommendation_number"] > 3:
                st.session_state["recommendation_number"] = 1

                st.rerun()

    with reaction_col2:
        st.caption("On track 🟡")
        if st.button("✊", key=f"okay_{number}", use_container_width=True):
            st.session_state["recommendation_number"] += 1

        if st.session_state["recommendation_number"] > 3:
            st.session_state["recommendation_number"] = 1

            st.rerun()
            

    with reaction_col3:
        st.caption("Love It 🟢")
        if st.button("👍", key=f"good_{number}", use_container_width=True):
            st.caption("Let's Watch!")