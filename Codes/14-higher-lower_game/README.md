# Higher or Lower Game

A simple Python game where players guess which account has more followers on Instagram.

## How It Works
1. The game displays two random accounts with their description and country.
2. Players must guess which account has more followers by typing 'A' or 'B'.
3. The game tracks your score for consecutive correct guesses.
4. The game ends when the player makes a wrong guess.

## Features
- Randomized account selection from a dataset.
- Tracks the player's score across rounds.
- Clean and simple CLI interface.

## Requirements
- Python 3.x
- The following files must be available:
  - `game_data.py`: Contains a list of accounts with `name`, `description`, `country`, and `follower_count`.
  - `art.py`: Contains ASCII art for the game logo and visual separator.

## How to Play
1. Clone the repository and ensure all required files are in the same directory.
2. Run the script:
   ```bash
   python higher_lower.py
