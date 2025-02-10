import streamlit as st
import pickle
#import numpy as np

# Load the saved model
with open("titanic_predictor.sav", "rb") as file:
    model = pickle.load(file)

# Function to make predictions
def predict_survival(model, features):
    prediction = model.predict([features])
    return "Survived" if prediction[0] == 1 else "Did Not Survive"

def reset_form():
    st.session_state.passenger_class = 0
    st.session_state.gender = 0
    st.session_state.embarkation = 0
    st.session_state.age = 25
    st.session_state.siblings_spouses = 0
    st.session_state.parents_children = 0
    st.session_state.fare = 50
    st.session_state.form_submitted = False
    st.rerun()

def main():
    st.markdown("### Would you survive the Titanic disaster?")

    # Initialize session state for form submission tracking
    if "form_submitted" not in st.session_state:
        st.session_state.form_submitted = False

    # Form Creation
    with st.form("my_form"):
        # Passenger Class Selection
        class_map = {0: "First Class", 1: "Second Class", 2: "Third Class"}
        st.segmented_control(
            "What passenger class are you?",
            options=class_map.keys(),
            format_func=lambda option: class_map[option],
            key="passenger_class"
        )

        # Gender Selection
        gender_map = {0: "Male", 1: "Female"}
        st.segmented_control(
            "What is your gender?",
            options=gender_map.keys(),
            format_func=lambda option: gender_map[option],
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
        embark_map = {0: "Cherbourg", 1: "Queenstown", 2: "Southampton"}
        st.segmented_control(
            "Which port did you embark from?",
            options=embark_map.keys(),
            format_func=lambda option: embark_map[option],
            key="embarkation"
        )

        # Add a horizontal line for visual separation
        st.markdown("---")

        # Submit & Reset Buttons inside the form
        col1, col2 = st.columns(2)
        with col2:
            submitted = st.form_submit_button("Submit")

        with col1:
            st.form_submit_button("Reset", on_click=reset_form)

    # Handle Form Submission
    if submitted:
        st.session_state.form_submitted = True  # Mark form as submitted

    # Display results **if form was submitted**
    if st.session_state.form_submitted:
        st.success(
            f"**Form Submitted! **\n\n"
            f"**Class:** {class_map[st.session_state.passenger_class]}\n\n"
            f"**Gender:** {gender_map[st.session_state.gender]}\n\n"
            f"**Age:** {st.session_state.age}\n\n"
            f"**Siblings/Spouses:** {st.session_state.siblings_spouses}\n\n"
            f"**Parents/Children:** {st.session_state.parents_children}\n\n"
            f"**Fare Paid:** ${st.session_state.fare}\n\n"
            f"**Embarkation:** {embark_map[st.session_state.embarkation]}\n\n"
        )

        # Prepare features for prediction
        Pclass = st.session_state.passenger_class
        Sex = 1 if st.session_state.gender == 1 else 0
        Age = st.session_state.age
        SibSp = st.session_state.siblings_spouses
        Parch = st.session_state.parents_children
        Fare = st.session_state.fare

        features = [Pclass, Sex, Age, SibSp, Parch, Fare]

        # Prediction Button
        if st.button("Predict"):
            result = predict_survival(model, features)
            st.write(f"### Prediction: {result}")

if __name__ == "__main__":
    main()