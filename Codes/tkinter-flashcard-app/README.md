# Flashcard App - Learn Language with Ease! 📚

Welcome to the **Flashcard App**, a simple and interactive tool to help you learn Language words and their English 
translations using flashcards. Built with Python, `tkinter`, and `pandas`, this app makes language learning fun and engaging! 🌟

## Overview

This app displays French words on a flashcard, flips to show the English translation after 3 seconds, and lets you mark
words as "known" or move to the next card. Known words are removed from the learning list and saved for future sessions.

### Features
- Learn French words with their English translations.
- Automatic card flip after 3 seconds.
- Mark words as "known" to remove them from the learning list.
- Save progress to a CSV file for future sessions.

## Directory Structure

- `tkinter_flashcard_app/`
  - `flashcard_app.py`: The main Python script for the flashcard app.
  - `data/`
    - `french_words.csv`: The original dataset of French-English word pairs.
    - `words_to_learn.csv`: The updated list of words to learn (auto-generated).
  - `images/`
    - `card_front.png`: Image for the front of the flashcard.
    - `card_back.png`: Image for the back of the flashcard.
    - `right.png`: Image for the "known" button.
    - `wrong.png`: Image for the "next card" button.

## Prerequisites

- Python 3.x installed on your system.
- Required libraries: `tkinter` (usually included with Python), `pandas`.

## Installation

1. **Clone the Repository** (if applicable):
   ```bash
   git clone https://github.com/Reza-1988/DailyCoding/Codes.git
   cd tkinter-flashcard-app
   flashcard_app.py