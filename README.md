# Digital Marketing Assistant Bot

This project includes two main components:

1. **Telegram Bot**: Helps generate relevant keywords, predicts industry trends, and provides answers to digital marketing FAQs.
2. **Flask Web Dashboard**: Displays industry trends fetched from an external API.

## Requirements

- Python 3.8+
- Install dependencies:
    ```bash
    pip install -r telegram-bot/requirements.txt
    pip install -r backend/requirements.txt
    ```

## Running the Application

1. **Run the Telegram Bot**:
    ```bash
    python bot.py
    ```
    Replace `YOUR_BOT_API_KEY` in the code with your actual Telegram bot API key.

2. **Run the Flask Web Dashboard**:
    ```bash
    python app.py
    ```
    Visit `http://127.0.0.1:5000/` to access the dashboard.

## Features

- **Telegram Bot**: 
  - Generate industry-specific keywords.
  - Fetch PPC industry trends.
  - Answer digital marketing FAQs.
  
- **Web Dashboard**: 
  - Fetch and display industry trends.

## Future Enhancements

- Integrate more complex keyword generation techniques.
- Improve the FAQ system with better AI-driven insights.
