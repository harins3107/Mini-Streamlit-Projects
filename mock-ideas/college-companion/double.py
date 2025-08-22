import streamlit as st
st.title("Double a Number App")

num = st.number_input("Enter a number", min_value=1, max_value=100, value=10)
if st.button("Double it"):
    st.write("Result:", num * 2)
st.write("This app doubles the number you enter.")


