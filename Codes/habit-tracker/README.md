# Habit Tracker with Pixela API

This Python application creates a habit tracker using the [Pixela API](https://pixe.la/). It allows you to register a user, create a graph to track your deep thinking time in minutes, and manage daily entries (pixels) by posting, updating, or deleting them.

## Features
- Registers a Pixela user account.
- Creates a graph to track minutes spent on deep thinking.
- Posts daily pixel data based on user input.
- Updates or deletes pixel entries for specific dates.

## Project Files
- **`habit_tracker.py`**: The main script handling user creation, graph setup, and pixel management.

## Prerequisites
- **Python 3.x** installed.
- Required library:
  - `requests`: For making API calls.
- A Pixela account (you’ll create this via the script).
- Environment variables for security (optional but recommended).

## Installation
1. **Clone or download this repository** to your local machine.
2. **Install the required library**:
   ```bash
   pip install requests
   git clone https://github.com/Reza-1988/DailyCoding/Codes.git
   cd habit-tracker.git
   python habit_tracker.py