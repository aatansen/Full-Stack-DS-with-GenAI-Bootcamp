# Gemini CLI Text Analyzer

A simple **Python command-line application*- that uses **Google Gemini (Generative AI)*- to perform basic NLP tasks like sentiment analysis, language translation, and language detection.

The app also includes a **basic in-memory user registration and login system**.

## Features

- User Registration & Login (in-memory)
- Sentiment Analysis
- Language Translation (English → Bangla)
- Language Detection
- Uses Google Gemini API (`gemini-2.5-flash`)
- Environment variable support using `python-dotenv`

## Tech Stack

- Python
- google-generativeai (Gemini)
- python-dotenv

## Project Structure

- `BaseModel`
  - Handles Gemini API configuration
  - Returns the AI model instance
- `AppFeatures`
  - User authentication (register/login)
  - Menu-based CLI navigation
  - NLP features using Gemini

## Requirements

- Python 3.9+
- Google Gemini API Key

## Installation

  ```sh
  pip install google-generativeai python-dotenv
  ```

## Environment Setup

Create a `.env` file in the root directory and add:

```env
GEMINI_API_KEY=your_api_key_here
```

## Run The App

  ```sh
  python app.py
  ```
