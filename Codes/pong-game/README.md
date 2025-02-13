# Pong Game 🏓

A classic **Pong Game** implemented in Python using the `turtle` module. Play with a friend and compete to see who scores the most!

## 🎮 How to Play
- **Player 1 (Left Paddle)**
  - Move Up: `W`
  - Move Down: `S`
  
- **Player 2 (Right Paddle)**
  - Move Up: `Up Arrow`
  - Move Down: `Down Arrow`

- **Goal:** Hit the ball with the paddle to prevent it from going off-screen. If a player misses, the opponent scores a point.

## Project Structure
📂 pong-game/ 
├── pong_game.py # Main game logic 
├── paddle.py # Paddle class (player controls) 
├── ball.py # Ball movement & physics 
├── net.py # Net display in the middle 
├── scoreboard_pong.py # Score tracking & display


### **🔹 1. `pong_game.py` (Main Game File)**
This file:
- Initializes the game screen
- Creates the paddles, ball, scoreboard, and net
- Handles user input (keyboard controls)
- Runs the main game loop (collision detection, scoring, etc.)

### **🔹 2. `paddle.py` (Paddle Class)**
- Manages paddle movement (`go_up()` and `go_down()`)
- Allows players to control paddles with keyboard inputs

### **🔹 3. `ball.py` (Ball Class)**
- Handles ball movement (`move()`)
- Implements bouncing mechanics (`bounce_x()`, `bounce_y()`)
- Resets ball position when a player scores (`reset_position()`)

### **🔹 4. `net.py` (Net Class)**
- Displays the **net** in the middle of the screen for better visual representation.

### **🔹 5. `scoreboard_pong.py` (Scoreboard Class)**
- Tracks and displays the score
- Updates the score when a player scores a point

## 🚀 How to Run the Game
### **1. Install Python**
Ensure Python 3 is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### **2. Clone this repository**
```bash
git clone https://github.com/Reza-1988/pong-game.git
cd pong-game
python pong_game.py
