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
                "imdb_link": "https://www.imdb.com/title/tt1490017/",
            },
            "Image Link": r"C:\Users\Brend\Documents\HCI-Final\Lego_movie.jpg"
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
                    "imdb_link": "https://www.imdb.com/title/tt1266020/"
                },
                "Image Link": r"C:\Users\Brend\Documents\HCI-Final\parks_recs.jpg"
            }

    
    if st.session_state['saved_mood'].lower() in ["sad", "down", "depressed"]:
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
                    "imdb_link": "https://www.imdb.com/title/tt3398228/"
                },
                "Image Link": r"C:\Users\Brend\Documents\HCI-Final\BoJack_Horseman.png"
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
                    "imdb_link": "https://www.imdb.com/title/tt0338013/"
                },
                "Image Link": r"C:\Users\Brend\Documents\HCI-Final\eternal_sunshine.jpg"
            }

    return dict
    

def display_recommendation(number):
        if "saved_mood" not in st.session_state or not st.session_state["saved_mood"]:
            st.warning("Please enter a mood first.")
            return
        
        recommendation = grab_recommendation(number)
        st.markdown(
            f"""
            <div style="text-align: center; margin-bottom: 0.75rem;">
                <div style="font-size: 1.35rem; font-weight: 700; color: #111;">
                    {recommendation['Title']}
                </div>
                <div style="font-size: 0.95rem; color: #666; margin-top: 0.15rem;">
                    {recommendation['details']['Release Year']}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.image(recommendation["Image Link"], use_container_width=True)

        st.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)

        info_col1, info_col2 = st.columns(2)

        with info_col1:
            st.markdown("Genre")
            st.caption(f"{recommendation['Genre']}")

        with info_col2:
            st.markdown("Subgenre")
            st.caption(f"{recommendation['Subgenre']}")

        st.markdown("Director")
        st.caption(recommendation["details"]["Director"])

        st.markdown("Rating")
        st.caption(f"{recommendation['details']['Rating']}/10")

        st.markdown("Synopsis")
        st.caption(recommendation["details"]["Synopsis"])

        st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)

        st.link_button(
            "More Info on IMDb",
            recommendation["details"]["imdb_link"],
            use_container_width=True
        )

        st.markdown("<div style='height: 8px;'></div>", unsafe_allow_html=True)