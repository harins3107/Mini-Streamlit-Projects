import streamlit as st

st.title("Simple Calculator")

a = st.number_input("Enter first number", value=0)
b = st.number_input("Enter second number", value=0)
operation = st.selectbox("Choose operation", ["Add", "Subtract", "Multiply", "Divide"])

if st.button("Calculate"):
    if operation == "Add":
        st.write("Result =", a+b)
    elif operation == "Subtract":
        st.write("Result =", a-b)
    elif operation == "Multiply":
        st.write("Result =", a*b)
    elif operation == "Divide":
        st.write("Result =", a/b if b != 0 else "Cannot divide by zero")
