import streamlit as st
import pandas as pd
import numpy as np
import plotly_express as px



# Function to reset form fields
def reset_form():
    st.session_state.passenger_class = 0
    st.session_state.gender = 0
    st.session_state.embarkation = 0
    st.session_state.age = 25
    st.session_state.siblings_spouses = 0
    st.session_state.parents_children = 0
    st.session_state.fare = 50
    st.session_state.slider_val = 25
    st.rerun()

# Initialize session state for form submission tracking
if "form_submitted" not in st.session_state:
    st.session_state.form_submitted = False

# Title
st.markdown("### Would you survive the Titanic disaster?")

# Form Creation
with st.form("my_form"):
    # Passenger Class Selection
    option_map = {0: "First Class", 1: "Second Class", 2: "Third Class"}
    st.segmented_control(
        "What passenger class are you?",
        options=option_map.keys(),
        format_func=lambda option: option_map[option],
        key="passenger_class"
    )

    # Gender Selection
    option_map = {0: "Male", 1: "Female"}
    st.segmented_control(
        "What is your gender?",
        options=option_map.keys(),
        format_func=lambda option: option_map[option],
        key="gender"
    )

    # Age
    st.slider('How old are you?', 0, 80, key="age")

    # Number of Siblings/Spouses
    st.slider('How many siblings and spouses were with you?', 0, 8, key="siblings_spouses")

    # Number of Parents/Children
    st.slider('How many parents and children were abroad with you?', 0, 6, key="parents_children")

    # Fare Paid (with $ sign)
    st.slider('How much did you pay for your cruise ticket (in 1910 USD)?', 0, 512, key="fare", format="$%d")

    # Embarkation Port Selection
    option_map = {0: "Cherbourg", 1: "Queenstown", 2: "Southampton"}
    st.segmented_control(
        "Which port did you embark from?",
        options=option_map.keys(),
        format_func=lambda option: option_map[option],
        key="embarkation"
    )

    # Add a horizontal line for visual separation
    st.markdown("---")

    # Submit & Reset Buttons inside the form
    col1, col2 = st.columns(2)
    with col2:
        submitted = st.form_submit_button("Submit")

    with col1:
        reset = st.form_submit_button("Reset", on_click=reset_form)

# Handle Form Submission
if submitted:
    st.session_state.form_submitted = True  # Mark form as submitted

# Display results **if form was submitted**
if st.session_state.form_submitted:
    st.success(
        f"**Form Submitted! **\n\n"
        f"**Class:** {option_map[st.session_state.passenger_class]}\n\n"
        f"**Gender:** {option_map[st.session_state.gender]}\n\n"
        f"**Age:** {st.session_state.age}\n\n"
        f"**Siblings/Spouses:** {st.session_state.siblings_spouses}\n\n"
        f"**Parents/Children:** {st.session_state.parents_children}\n\n"
        f"**Fare Paid:** ${st.session_state.fare}\n\n"
        f"**Embarkation:** {option_map[st.session_state.embarkation]}\n\n"
    )