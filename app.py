import streamlit as st

# Task 1: The UI Shell
st.title("The Identity Echo Interface")
st.write("Enter your name and message below, then click **Transmit**.")

# Task 2: Multi-Data Collection
user_name = st.text_input("Enter your Name")
user_message = st.text_input("Enter your Message")

# Task 3: The Action Gate
if st.button("Transmit"):

    # Task 4: Conditional Routing (Edge Cases)
    if user_name.strip() == "":
        st.error("Please provide your name.")

    elif user_message.strip() == "":
        st.warning("Please type a message to transmit.")

    # Task 5: Formatted Output
    else:
        st.success(
            f"Transmission successful! Greetings, {user_name}. We received your message: {user_message}"
        )

        # Advanced Challenge
        character_count = len(user_message)
        token_count = character_count / 4

        st.info(
            f"System Check: Your message contains {character_count} characters and will consume approximately {token_count:.2f} tokens from our context window."
        )
