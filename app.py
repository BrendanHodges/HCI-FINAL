import streamlit as st
import pandas as pd
import numpy as np
from grab_mood import display_card

# Page config
st.set_page_config(
    page_title="Mood Matcher",
    page_icon="🎭",
    layout="centered"
)

st.markdown("""
    <style>
        .main {
            padding-top: 1rem;
        }

        .logo-text {
            text-align: center;
            font-size: 42px;
            font-weight: 600;
            margin-bottom: 10px;
        }

        .greeting-text {
            font-size: 22px;
            font-weight: 500;
            margin-top: 40px;
            margin-bottom: 20px;
        }

        .section-space {
            margin-top: 30px;
        }
    </style>
""", unsafe_allow_html=True)

# Session state setup
if "user_name" not in st.session_state:
    st.session_state.user_name = "John"

if "mood" not in st.session_state:
    st.session_state.mood = ""

# Top header area
col1, col2, col3 = st.columns([1, 4, 1])

with col1:
    if "sidebar_open" not in st.session_state:
        st.session_state.sidebar_open = False

    if st.button("☰"):
        st.session_state.sidebar_open = not st.session_state.sidebar_open

    if st.session_state.sidebar_open:
        with st.sidebar:
            st.title("MENU")

            page = st.radio(
                "Choose a section:",
                ["Home", "What's popular", "Previous Choices", "Account Settings", "Help Center"]
            )

            st.divider()

with col2:
    st.markdown('<div class="logo-text">MM</div>', unsafe_allow_html=True)

st.divider()

# Greeting section
st.markdown(
    f'<div class="greeting-text">Good Afternoon {st.session_state.user_name}, how are you feeling today?</div>',
    unsafe_allow_html=True
)

# Mood input
mood_input = st.text_input(
    label="",
    placeholder="Type your mood here..."
)

# Save mood
if mood_input:
    st.session_state.mood = mood_input

# Button to move forward later
if st.button("Submit Mood"):
    if st.session_state.mood:
        st.success(f"Your mood was saved as: {st.session_state.mood}")
        display_card()
    else:
        st.warning("Please enter a mood first.")

st.divider()