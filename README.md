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
- <img width="1922" height="996" alt="image" src="https://github.com/user-attachments/assets/4c6109cd-1a37-4a01-8a97-d48efca74e24" />

- Warning if the message is empty.
- <img width="1916" height="1021" alt="image" src="https://github.com/user-attachments/assets/2c8aa6fe-004d-4a7c-a279-24684a7435df" />

- Success message when both fields are provided.
- Token usage estimate displayed as a system check.
- <img width="1919" height="1026" alt="image" src="https://github.com/user-attachments/assets/46f85c93-8ff6-4a6f-b2e4-4da2e3a4d3e2" />


## 👩‍💻 Author

Shravani Dhuri
