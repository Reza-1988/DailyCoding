# Quizzler

A simple True/False quiz application built with Python, Tkinter, and the Open Trivia Database API.

## Features
- Fetches 10 boolean (True/False) questions from the [Open Trivia Database](https://opentdb.com/).
- Displays questions in a clean GUI with a canvas and buttons.
- Tracks and displays the user's score.
- Provides visual feedback (green for correct, red for incorrect) after each answer.

## How It Works
1. `data.py`: Retrieves quiz data from the Open Trivia Database API (default: 10 questions, category 18 - Science: Computers).
2. `question_model.py`: Defines the `Question` class to store question text and answers.
3. `quiz_brain.py`: Manages quiz logic, including question progression, scoring, and HTML entity decoding.
4. `ui.py`: Creates the Tkinter-based GUI with a canvas, score label, and True/False buttons.
5. `quizler_app.py`: Ties everything together, initializing the question bank and launching the app.

## Requirements
- Python 3.x
- `requests` library (`pip install requests`)
- Tkinter (usually included with Python)

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/Reza-1988/DailyCoding/Codes.git
   cd quizler-app.git
   python quizler_app.py