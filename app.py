import streamlit as st
from grab_mood import grab_recommendation, display_recommendation

st.set_page_config(
    page_title="Mood Matcher",
    page_icon="🎭",
    layout="wide"
)

if "page" not in st.session_state:
    st.session_state["page"] = "Hello"

st.markdown("""
<style>
.stApp {
    background-color: #DDE1E7;
}

div.block-container {
    padding-top: 1.5rem;
    padding-bottom: 1.5rem;
}

/* Phone shell */
div[data-testid="stVerticalBlockBorderWrapper"] {
    background: #111111;
    border-radius: 48px;
    padding: 2.8rem 0.9rem 1.8rem 0.9rem;
    box-shadow: 0 24px 55px rgba(0, 0, 0, 0.22);
    border: 4px solid #1b1b1b;
    position: relative;
    max-width: 390px;
    margin: auto;
    overflow: hidden;
}

/* Inner screen area */
div[data-testid="stVerticalBlockBorderWrapper"] > div {
    background: linear-gradient(180deg, #ffffff 0%, #f7f8fb 100%);
    border-radius: 36px;
    padding: 1.2rem 1rem 1.2rem 1rem;
    margin-top: 0.8rem;
    min-height: 640px;
    position: relative;
    overflow: hidden;
}

/* Top speaker / notch */
div[data-testid="stVerticalBlockBorderWrapper"]::before {
    content: "";
    position: absolute;
    top: 14px;
    left: 50%;
    transform: translateX(-50%);
    width: 115px;
    height: 24px;
    background: #000000;
    border-radius: 0 0 18px 18px;
    z-index: 20;
}

/* Small speaker detail */
div[data-testid="stVerticalBlockBorderWrapper"]::after {
    content: "";
    position: absolute;
    top: 22px;
    left: 50%;
    transform: translateX(-50%);
    width: 42px;
    height: 5px;
    background: #2a2a2a;
    border-radius: 999px;
    z-index: 21;
}

/* Bottom home indicator */
div[data-testid="stVerticalBlockBorderWrapper"] > div::after {
    content: "";
    position: absolute;
    bottom: 10px;
    left: 50%;
    transform: translateX(-50%);
    width: 110px;
    height: 5px;
    background: #d1d5db;
    border-radius: 999px;
}

/* Main buttons */
.stButton > button {
    width: 100%;
    border-radius: 16px;
    font-weight: 600;
    font-size: 1rem;
    padding: 0.8rem 1rem;
    border: none;
    box-shadow: 0 6px 14px rgba(0, 0, 0, 0.08);
    transition: all 0.2s ease;
}

.stButton > button:hover {
    transform: translateY(-1px);
}

/* Inputs if you use them later */
.stTextInput input,
.stNumberInput input,
div[data-baseweb="select"] > div {
    border-radius: 14px;
}

/* Welcome page text styling */
.welcome-wrap {
    text-align: center;
    padding-top: 2.2rem;
    padding-bottom: 1rem;
}

.welcome-emoji {
    font-size: 3rem;
    margin-bottom: 0.5rem;
}

.welcome-title {
    font-size: 2rem;
    font-weight: 700;
    color: #111111;
    margin-bottom: 0.35rem;
    letter-spacing: -0.02em;
}

.welcome-subtitle {
    font-size: 1rem;
    color: #4B5563;
    line-height: 1.5;
    margin-bottom: 1.4rem;
    padding-left: 0.4rem;
    padding-right: 0.4rem;
}

.welcome-section-label {
    text-align: center;
    font-size: 0.88rem;
    color: #6B7280;
    margin-top: 1rem;
    margin-bottom: 0.45rem;
}

.welcome-divider {
    height: 1px;
    background: rgba(0,0,0,0.08);
    margin-top: 1.2rem;
    margin-bottom: 1.2rem;
    border-radius: 999px;
}

/* Secondary text style */
.small-muted {
    text-align: center;
    font-size: 0.8rem;
    color: #6B7280;
    margin-top: 1.2rem;
}
            
/* Top nav container spacing */
.top-nav {
    margin-bottom: 8px;
}

/* ONLY style buttons inside the top nav */
.top-nav div[data-testid="stButton"] > button {
    height: 42px;
    width: 42px;
    min-width: 42px;
    border-radius: 999px;
    padding: 0;
    font-size: 1.1rem;
    background-color: #F3F4F6;
    border: none;
}

/* Center title */
.top-nav-title {
    text-align: center;
    font-weight: 600;
    font-size: 2rem;
    padding-top: 6px;
    color: #111;
}
</style>
""", unsafe_allow_html=True)


def phone_shell():
    left, center, right = st.columns([1.2, 1.0, 1.2])
    with center:
        return st.container(border=True, height=700)


if st.session_state["page"] == "Hello":
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

        st.markdown('<div class="welcome-divider"></div>', unsafe_allow_html=True)

        with col2:
            st.markdown('<div class="welcome-section-label">Want to know more?</div>', unsafe_allow_html=True)
            if st.button("How it Works", key="learn_more", use_container_width=True):
                st.warning("Learn more functionality coming soon!")

        st.markdown("""
            <div class="small-muted">
                Personalized recommendations for movies, shows, music, books, games, and podcasts.
            </div>
        """, unsafe_allow_html=True)

elif st.session_state["page"] == "Intro Page":
    with phone_shell():
        st.title("Set Your Preferences")
        st.write("This helps us give you better recommendations.")
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
            step=1
        )

        entertainment_type = st.selectbox(
            "Preferred entertainment",
            ["Select one", "Movies", "TV Shows", "Music", "Books", "Games", "Podcasts"]
        )

        favorite_genre = st.selectbox(
            "Favorite genre",
            ["Select one", "Comedy", "Drama", "Action", "Horror", "Romance", "Sci-Fi", "Fantasy", "Documentary"]
        )

        recommendation_style = st.radio(
            "Recommendation style",
            ["Popular picks", "Hidden gems", "A mix of both"],
            horizontal=False
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
                st.session_state["page"] = "Mood Matcher"
                st.rerun()

elif st.session_state["page"] == "Mood Matcher":
    with phone_shell():

        # NAV BAR
        st.markdown('<div class="top-nav">', unsafe_allow_html=True)

        nav_left, nav_center, nav_right = st.columns([1, 3, 1])

        with nav_left:
            if st.button("☰", key="menu_button"):
                st.warning("Menu coming soon!")

        with nav_center:
            st.markdown(
                "<div class='top-nav-title'>Mood Matcher</div>",
                unsafe_allow_html=True
            )

        with nav_right:
            if st.button("👤", key="profile_button"):
                st.warning("Profile coming soon!")

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
                st.warning("Profile coming soon!")

        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)

        display_recommendation(st.session_state["recommendation_number"])

        if st.button("Find Another Match", key="find_another_match", use_container_width=True):
            st.session_state["recommendation_number"] += 1

            if st.session_state["recommendation_number"] > 2:
                st.session_state["recommendation_number"] = 1

            st.rerun()