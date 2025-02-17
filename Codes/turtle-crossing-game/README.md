# 🐢 Turtle Crossing Game

A simple **Turtle Crossing Game** built using Python's `turtle` module. Guide the turtle to cross the road while avoiding moving cars. Each successful crossing increases the level and speeds up the cars!

## 🎮 How to Play
- **Move Up**: Press the `Up Arrow` key to move the turtle forward.
- **Avoid Cars**: If the turtle collides with a car, the game is over.
- **Win the Level**: Reach the top of the screen to level up and make the cars move faster.

## 🛠️ Project Structure
📂 turtle-crossing-game/ 
├── turtle_crossing_game.py # Main game loop & logic 
├── player.py # Player (Turtle) movement 
├── car_manager.py # Controls car generation & movement 
├── scoreboard_turtle.py # Score tracking & level management


### **1️⃣ `turtle_crossing_game.py` (Main Game)**
- Initializes the game screen.
- Handles player movement.
- Spawns and moves cars.
- Detects collisions and checks for level completion.

### **2️⃣ `player.py` (Turtle Player)**
- Moves the turtle upwards.
- Resets position after crossing the road.

### **3️⃣ `car_manager.py` (Car Movement)**
- Spawns random cars in different colors.
- Moves cars towards the left.
- Increases speed when the player levels up.

### **4️⃣ `scoreboard_turtle.py` (Scoreboard)**
- Displays the current level.
- Shows "GAME OVER" when the player loses.

## 🚀 How to Run the Game
### **1. Install Python**
Ensure Python 3 is installed on your system. Download it from [python.org](https://www.python.org/downloads/).

### **2. Clone this repository**
```bash
git clone https://github.com/Reza-1988/turtle-crossing-game.git
cd turtle-crossing-game
python turtle_crossing_game.py

