# U.S. States Game 🗺️🌍

## Overview
The **U.S. States Game** is an interactive Python game built using the `turtle` and `pandas` libraries. The goal of the game is to guess the names of all 50 U.S. states. As you guess correctly, the state names are written on a blank U.S. map at their correct locations. If you exit the game before guessing all states, it generates a CSV file listing the states you missed, so you can learn them later!

---

## Directory Structure
u.s-states-game/
├── us_states_game.py  # Main Python script for the game
├── blank_states_img.gif # Blank U.S. map image used in the game
├── 50_states.csv # CSV file containing state names and coordinates
└── README.md # This file


---

## Features
- Displays a blank U.S. map using `turtle`.
- Prompts the user to input state names.
- Writes correctly guessed state names on the map at their corresponding coordinates.
- Tracks the number of correctly guessed states (e.g., "X/50 States Correct").
- Allows exiting the game by typing "Exit".
- Saves a list of unguessed states to a file (`states_should_learn.csv`) when exiting.

---

## Prerequisites
To run this game, you need the following installed:
- **Python 3.x** (tested with Python 3.12)
- **Libraries**:
  - `turtle` (comes with Python standard library)
  - `pandas` (install via Conda or pip)

### Installation
1. **Clone the repository** (if using Git):
   ```bash
   git clone <Reza-1988>
   cd u.s-states-game
   python us_states_game.py