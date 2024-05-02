import pickle
import streamlit as st

# Load the models
with open('model.pkl', 'rb') as f:
    lab_model = pickle.load(f)

with open('model2.pkl', 'rb') as f:
    lab_resources_model = pickle.load(f)

# Create a Streamlit app
st.title('Lab Prediction and Resources')

# Get user input
user_id = st.number_input('Enter User ID')
course_study = st.text_input('Enter Course of Study')

# Make predictions
if st.button('Predict'):
    lab = lab_model.predict([[user_id, course_study]])
    lab_resources = lab_resources_model.predict([[user_id, course_study]])

    # Display the results
    st.write('Predicted Lab:', lab[0])
    st.write('Lab Resources:', lab_resources[0])
