# Snake Game 🐍

A classic **Snake Game** built using Python's `turtle` module. Control the snake, eat food to grow, and keep track of your score. Avoid hitting the walls or yourself to stay in the game!

## 🎮 How to Play
- Use the **arrow keys** to control the snake:
  - ⬆️ Up
  - ⬇️ Down
  - ⬅️ Left
  - ➡️ Right
- Eat the **blue food** to grow in size.
- The game ends if the snake collides with the walls or itself.

## 🛠 Files & Structure
📂 snake-game/  
├── snake_game.py # Main game file  
├── snake.py # Snake class (handles movement & growth)  
├── food.py # Food class (random spawning of food)  
├── scoreboard.py # Scoreboard class (keeps track of score & game over)  



### **1. `snake_game.py` (Main Game File)**
This file initializes the game, creates the snake, food, and scoreboard, and runs the game loop.

### **2. `snake.py` (Snake Class)**
- Manages the movement of the snake.
- Handles growing the snake when it eats food.
- Controls the direction changes.

### **3. `food.py` (Food Class)**
- Spawns food randomly on the screen.
- Refreshes the food position once eaten by the snake.

### **4. `scoreboard.py` (Scoreboard Class)**
- Keeps track of the player's score.
- Displays "GAME OVER" when the game ends.

## 🚀 Getting Started
### **1. Install Python**
Ensure you have Python 3 installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### **2. Clone this repository**
```bash
git clone https://github.com/Reza-1988/snake-game.git
cd snake-game
python snake_game.py
