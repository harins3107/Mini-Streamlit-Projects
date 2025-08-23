import streamlit as st

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Stack Applications","Queue Applications"])

if page == "Stack Applications":
    st.title("Stack Applications")

    if "stk" not in st.session_state:
        st.session_state.stk = []

    values = []
    val = st.number_input(f"Enter value:", value=0, key="val_input")
    values.append(val)

    if st.button("Append"):
        st.session_state.stk.extend(values)
        st.success(f"Appended values: {values}")

    if st.button("Pop"):
        if st.session_state.stk:
            popped_val = st.session_state.stk.pop()
            st.success(f"Popped value: {popped_val}")
        else:
            st.error("Stack is empty, cannot pop")        

    if st.button("Display Stack"):
        if st.session_state.stk:
            st.write(st.session_state.stk)
        else:
            st.info("Stack is empty")

if page == "Queue Applications":
    st.title("Queue Applications")

    if "queue" not in st.session_state:
        st.session_state.queue = []

    q_values = []
    q_val = st.number_input(f"Enter value:", value=0, key="q_val_input")
    q_values.append(q_val)

    if st.button("Enqueue"):
        st.session_state.queue.extend(q_values)
        st.success(f"Enqueued values: {q_values}")

    if st.button("Dequeue"):
        if st.session_state.queue:
            dequeued_val = st.session_state.queue.pop(0)
            st.success(f"Dequeued value: {dequeued_val}")
        else:
            st.error("Queue is empty, cannot dequeue")        

    if st.button("Display Queue"):
        if st.session_state.queue:
            st.write(st.session_state.queue)
        else:
            st.info("Queue is empty") 
