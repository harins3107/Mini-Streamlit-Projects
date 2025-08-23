import streamlit as st

# Initialize page state
if "page" not in st.session_state:
    st.session_state.page = "home"

# Function to change page
def go_to(page_name):
    st.session_state.page = page_name

# Home Page
if st.session_state.page == "home":
    st.title("🏠 Home Page")
    st.write("Welcome!")
    if st.button("Go to Calculator"):
        go_to("calc")

# Calculator Page
elif st.session_state.page == "calc":
    st.title("🧮 Calculator Page")
    a = st.number_input("Enter a number", key="a")
    b = st.number_input("Enter another number", key="b")
    if st.button("Add"):
        st.write("Result =", a+b)
    if st.button("Back to Home"):
        go_to("home")
