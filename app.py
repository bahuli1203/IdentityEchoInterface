import streamlit as st

# Task 1
st.title("The Identity Echo Interface")
st.write("Enter your details below and click Transmit.")

# Task 2
user_name = st.text_input("Enter your Name")
user_message = st.text_input("Enter your Message")

# Task 3
if st.button("Transmit"):

    # Task 4
    if user_name == "":
        st.error("Please provide your name.")
    elif user_message == "":
        st.warning("Please type a message to transmit.")

    # Task 5
    else:
        st.success(
            f"Transmission successful! Greetings, {user_name}. We received your message: {user_message}"
        )

        # Advanced Challenge
        token_count = len(user_message) / 4
        st.info(
            f"System Check: Your message will consume approximately {token_count:.2f} tokens from our context window."
        )
