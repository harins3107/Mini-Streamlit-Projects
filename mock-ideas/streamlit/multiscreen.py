import streamlit as st

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Calculator", "About","Movie recommender"])

# Home Page
if page == "Home":
    st.title("🏠 Home Page")
    st.write("Welcome to my app!")

# Calculator Page
elif page == "Calculator":
    st.title("🧮 Calculator")
    a = st.number_input("Enter first number")
    b = st.number_input("Enter second number")
    if st.button("Add"):
        st.write("Result =", a+b)

# About Page
elif page == "About":
    st.title("ℹ️ About")
    st.write("This is a demo app using Streamlit.")

elif page == "Movie recommender":
    st.title("🎬 Movie Recommender")
    st.write("This section will recommend movies based on your preferences.")
    movie= st.text_input("Enter a movie you like")
    if st.button("Recommend"):
        st.write(f"Based on your interest in '{movie}', we recommend:")
        st.write("- Movie 1")
        st.write("- Movie 2")
        st.write("- Movie 3")

