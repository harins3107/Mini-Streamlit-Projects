import streamlit as st

st.set_page_config(page_title="Rocket Game 🚀", page_icon="🚀")

# Store rocket height in session_state
if "height" not in st.session_state:
    st.session_state.height = 0

st.title("🚀 Rocket Launch Game")

st.write(f"Rocket Height: **{st.session_state.height} meters**")

# Launch button
if st.button("Launch 🚀"):
    st.session_state.height += 10

# Reset button
if st.button("Reset 🔄"):
    st.session_state.height = 0

# Show rocket progress
st.progress(min(st.session_state.height, 100))  # Limit bar to 100

if st.session_state.height >= 100:
    st.success("🎉 Rocket reached space!")
else:
    st.info("Keep clicking launch to reach space!")
