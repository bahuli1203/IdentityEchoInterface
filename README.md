# Identity Echo Interface

A simple Streamlit application built as part of the MirAI School of Technology – Virtual Summer Internship 2026.

## 📌 Objective

This application collects a user's name and message, validates the input, and displays a personalized response. It also estimates the approximate AI token usage based on the message length.

## 🚀 Features

- User-friendly Streamlit interface
- Name input field
- Message input field
- Input validation
- Error message for empty name
- Warning message for empty message
- Personalized success message
- Estimated token count using the formula:
  - 1 token ≈ 4 characters
- Displays token estimate using Streamlit's `st.info()`

## 🛠️ Technologies Used

- Python
- Streamlit

## 📂 Project Structure

```
IdentityEchoInterface/
│── app.py
│── requirements.txt
│── README.md
```

## ▶️ Installation

1. Clone the repository:

```bash
git clone <your-repository-url>
```

2. Navigate to the project folder:

```bash
cd IdentityEchoInterface
```

3. Install the dependencies:

```bash
pip install -r requirements.txt
```

4. Run the application:

```bash
streamlit run app.py
```

## 📋 How It Works

1. Enter your name.
2. Enter your message.
3. Click the **Transmit** button.
4. The application:
   - Validates the inputs.
   - Displays a personalized success message.
   - Calculates the message length.
   - Estimates the token count.
   - Displays the estimated token usage.

## 📷 Output

- Error if the name is empty.
- <img width="1916" height="1021" alt="image" src="https://github.com/user-attachments/assets/f94f0c80-0d7c-4dc7-a5e4-8bddb8d45bbe" />

- Warning if the message is empty.
- Success message when both fields are provided.
- Token usage estimate displayed as a system check.

## 👩‍💻 Author

Shravani Dhuri
