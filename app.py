import streamlit as st
from grab_mood import grab_recommendation, display_recommendation

st.set_page_config(
    page_title="Mood Matcher",
    page_icon="🎭",
    layout="wide"
)

if "page" not in st.session_state:
    st.session_state["page"] = "Hello"

def load_css():
    with open("styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()
def phone_shell():
    left, center, right = st.columns([1.2, 1.0, 1.2])
    with center:
        return st.container(border=True, height=650)


if st.session_state["page"] == "Hello":
    st.markdown("---")
    with phone_shell():
        st.markdown("""
            <div class="welcome-wrap">
                <div class="welcome-emoji">🎭</div>
                <div class="welcome-title">Mood Matcher</div>
                <div class="welcome-subtitle">
                    Find the perfect entertainment for how you feel,
                    without endless scrolling.
                </div>
            </div>
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown('<div class="welcome-section-label">New here?</div>', unsafe_allow_html=True)
            if st.button("Create an account", key="get_started", use_container_width=True):
                st.session_state["page"] = "Intro Page"
                st.rerun()

        with col2:
            st.markdown('<div class="welcome-section-label">Already have an account?</div>', unsafe_allow_html=True)
            if st.button("Login", key="login", use_container_width=True):
                st.warning("Login functionality coming soon!")

        with col2:
            st.markdown('<div class="welcome-section-label">Want to know more?</div>', unsafe_allow_html=True)
            if st.button("How it Works", key="learn_more", use_container_width=True):
                st.warning("Learn more functionality coming soon!")

        st.text("")
        st.text("")
        st.markdown('<div class="welcome-divider"></div>', unsafe_allow_html=True)

        st.markdown("""
            <div class="small-muted">
                Personalized recommendations for movies, shows, music, books, games, and podcasts.
            </div>
        """, unsafe_allow_html=True)

        st.markdown("---")

elif st.session_state["page"] == "Intro Page":
    st.markdown("---")
    with phone_shell():
        st.markdown("""
            <div class="welcome-wrap">
                <div class="welcome-emoji">🎭</div>
                <div class="welcome-title">Set your preferences</div>
                <div class="welcome-subtitle">
                    This helps us give you better recommendations.
                </div>
            </div>
        """, unsafe_allow_html=True)
        st.markdown("---")

        name = st.text_input(
            "Name",
            key="user_name",
            placeholder="Enter your name"
        )

        age = st.number_input(
            "Age",
            min_value=0,
            max_value=120,
            value=18,
            step=1,
            key="age"
        )

        entertainment_type = st.selectbox(
            "Preferred entertainment",
            ["Select one", "Movies", "TV Shows", "Music", "Books", "Games", "Podcasts"],
            key="entertainment_type"
        )

        favorite_genre = st.selectbox(
            "Favorite genre",
            ["Select one", "Comedy", "Drama", "Action", "Horror", "Romance", "Sci-Fi", "Fantasy", "Documentary"],
            key="favorite_genre"
        )

        recommendation_style = st.radio(
            "Recommendation style",
            ["Popular picks", "Hidden gems", "A mix of both"],
            horizontal=False,
            key="recommendation_style"
        )

        st.markdown("---")

        if st.button("Continue"):
            if not name:
                st.warning("Please enter your name before continuing.")
            elif age < 12:
                st.warning("Sorry, you must be at least 12 years old to use this app.")
                
            elif entertainment_type == "Select one":
                st.warning("Please choose a preferred entertainment type.")
                
            elif favorite_genre == "Select one":
                st.warning("Please choose a favorite genre.")
                
            else:
                st.session_state["saved_profile"] = {
                        "name": st.session_state["user_name"],
                        "age": st.session_state["age"],
                        "entertainment": st.session_state["entertainment_type"],
                        "genre": st.session_state["favorite_genre"],
                        "style": st.session_state["recommendation_style"],
                    }
                st.session_state["page"] = "Mood Matcher"
                st.rerun()

        st.markdown("---")
elif st.session_state["page"] == "Mood Matcher":
    st.markdown("---")
    with phone_shell():

        # NAV BAR
        st.markdown('<div class="top-nav">', unsafe_allow_html=True)

        nav_left, nav_center, nav_right = st.columns([1, 3, 1])

        with nav_left:
            if st.button("☰", key="menu_button"):
                st.session_state["page"] = "Menu"
                st.rerun()

        with nav_center:
            st.markdown(
                "<div class='top-nav-title'>Mood Matcher</div>",
                unsafe_allow_html=True
            )

        
        with nav_right:
            if st.button("👤", key="profile_button_recommendation"):
                st.session_state["page"] = "Profile"
                st.rerun()

        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown("<div style='height: 8px;'></div>", unsafe_allow_html=True)

        # PAGE INTRO
        st.markdown(
            "<p style='text-align:center; font-size:0.98rem; color:#555; margin-bottom:0.2rem;'>How are you feeling today?</p>",
            unsafe_allow_html=True
        )
        st.markdown(
            "<p style='text-align:center; font-size:0.88rem; color:#777; margin-top:0;'>Tell us your mood and a few quick preferences.</p>",
            unsafe_allow_html=True
        )

        st.markdown("---")

        # MOOD INPUT
        mood = st.text_input(
            "Your mood",
            key="mood",
            placeholder="e.g. happy, stressed, bored, excited"
        )

        st.markdown("<div style='height: 6px;'></div>", unsafe_allow_html=True)

        # ADDITIONAL PREFERENCES
        st.markdown(
            "<p style='font-weight:600; font-size:1rem; margin-bottom:0.4rem;'>A few quick preferences</p>",
            unsafe_allow_html=True
        )

        social_preference = st.radio(
            "Who are you with?",
            ["Alone", "With friends"],
            horizontal=True,
            key="social_preference"
        )

        depth_preference = st.radio(
            "What kind of experience do you want?",
            ["Light", "Thought-provoking"],
            horizontal=True,
            key="depth_preference"
        )

        length_preference = st.radio(
            "How much time do you have?",
            ["Quick", "Long"],
            horizontal=True,
            key="length_preference"
        )

        st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)

        # ACTION BUTTON
        match_clicked = st.button("Match My Mood", key="match_mood_btn", use_container_width=True)

        if match_clicked:
            if not mood.strip():
                st.warning("Please enter your mood first.")
            else:
                st.session_state["saved_mood"] = mood  # ← SAVE IT HERE
                st.session_state["page"] = "Recommendation"
                st.rerun()

elif st.session_state["page"] == "Recommendation":
    st.markdown("---")
    with phone_shell():

        if "recommendation_number" not in st.session_state:
            st.session_state["recommendation_number"] = 1

        # TOP NAV
        st.markdown('<div class="top-nav">', unsafe_allow_html=True)

        nav_left, nav_center, nav_right = st.columns([1, 3, 1])

        with nav_left:
            if st.button("←", key="back_from_recommendation"):
                st.session_state["page"] = "Mood Matcher"
                st.rerun()

        with nav_center:
            st.markdown(
                "<div class='top-nav-title'>Your Match</div>",
                unsafe_allow_html=True
            )

        with nav_right:
            if st.button("👤", key="profile_button_recommendation"):
                st.session_state["page"] = "Profile"
                st.rerun()

        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)

        display_recommendation(st.session_state["recommendation_number"])
        reaction_col1, reaction_col2, reaction_col3 = st.columns(3)

        st.markdown("---")

elif st.session_state["page"] == "Profile":
    st.markdown("---")
    with phone_shell():

        # NAV
        st.markdown('<div class="top-nav">', unsafe_allow_html=True)

        nav_left, nav_center, nav_right = st.columns([1, 3, 1])

        with nav_left:
            if st.button("←", key="back_from_profile"):
                st.session_state["page"] = "Mood Matcher"
                st.rerun()

        with nav_center:
            st.markdown(
                "<div class='top-nav-title'>Profile</div>",
                unsafe_allow_html=True
            )

        with nav_right:
            st.markdown("")

        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)

        # GET VALUES
        profile = st.session_state.get("saved_profile", {})

        name = profile.get("name", "—")
        age = profile.get("age", "—")
        entertainment = profile.get("entertainment", "—")
        genre = profile.get("genre", "—")
        style = profile.get("style", "—")

        # PROFILE CARD
        st.markdown(
            f"""
            <div style="
                background-color:#E5E7EB;
                border-radius:24px;
                padding:1rem;
                text-align:center;
                margin-bottom:1rem;
            ">
                <div style="font-size:2.2rem;">👤</div>
                <div style="font-size:1.3rem; font-weight:700; color:#111;">
                    {name}
                </div>
                <div style="font-size:0.8rem; color:#666;">
                    Mood Matcher User
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        # DETAILS (clean + compact)
        st.markdown("**Account Details**")

        col1, col2 = st.columns(2)

        with col1:
            st.caption("Age")
            st.write(age)

            st.caption("Favorite Genre")
            st.write(genre)

        with col2:
            st.caption("Entertainment")
            st.write(entertainment)

            st.caption("Recommendation Style")
            st.write(style)

        st.markdown("<div style='height: 25px;'></div>", unsafe_allow_html=True)

        st.markdown(
            f"""
            <div style="
                background-color:#E5E7EB;
                border-radius:22px;
                padding:1rem;
                margin-top:1rem;
            ">
                <div style="font-size:0.85rem; color:#777; margin-bottom:0.3rem;">
                    Recent Activity
                </div>
                <div style="font-size:1rem; font-weight:600; color:#111;">
                    Last mood searched: {st.session_state.get("saved_mood", "No mood searched yet")}
                </div>
                <div style="font-size:0.85rem; color:#666; margin-top:0.4rem;">
                    Your recommendations are based on your profile preferences and current mood.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

elif st.session_state["page"] == "Menu":
    st.markdown("---")
    with phone_shell():
        # TOP NAV
        st.markdown('<div class="top-nav">', unsafe_allow_html=True)

        nav_left, nav_center, nav_right = st.columns([1, 3, 1])

        with nav_left:
            if st.button("←", key="back_from_menu"):
                st.session_state["page"] = "Mood Matcher"
                st.rerun()

        with nav_center:
            st.markdown(
                "<div class='top-nav-title'>Menu</div>",
                unsafe_allow_html=True
            )

        with nav_right:
            st.markdown("")

        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown("<div style='height: 14px;'></div>", unsafe_allow_html=True)

        st.markdown(
            """
            <div style="
                background-color:#E5E7EB;
                border-radius:22px;
                padding:1rem;
                margin-bottom:1rem;
                text-align:center;
            ">
                <div style="font-size:1.4rem; font-weight:700; color:#111;">
                    Menu
                </div>
                <div style="font-size:0.9rem; color:#666; margin-top:0.25rem;">
                    Explore more options below.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button("🔥 What's Popular", key="popular_btn", use_container_width=True):
            st.session_state["page"] = "Popular"
            st.rerun()

        if st.button("🕘 Previous Choices", key="previous_choices_btn", use_container_width=True):
            st.session_state["page"] = "Previous Choices"
            st.rerun()

        if st.button("❓ Help Center", key="help_center_btn", use_container_width=True):
            st.session_state["page"] = "Help Center"
            st.rerun()

elif st.session_state["page"] == "Popular":
    with phone_shell():
        st.markdown("---")
        if st.button("← Back to Menu", key="back_popular"):
            st.session_state["page"] = "Menu"
            st.rerun()

        st.title("What's Popular")
        st.write("Popular recommendations will appear here.")

elif st.session_state["page"] == "Previous Choices":
    with phone_shell():
        st.markdown("---")
        if st.button("← Back to Menu", key="back_previous"):
            st.session_state["page"] = "Menu"
            st.rerun()

        st.title("Previous Choices")
        st.write("Your past matches will appear here.")

elif st.session_state["page"] == "Help Center":
    with phone_shell():
        st.markdown("---")
        if st.button("← Back to Menu", key="back_help"):
            st.session_state["page"] = "Menu"
            st.rerun()

        st.title("Help Center")
        st.write("Need help? This section can explain how Mood Matcher works.")