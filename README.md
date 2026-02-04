# Snake Game (Python Turtle)

## 🎯 Project Objective
This project is designed to practice event-driven programming, basic game logic design, and code refactoring using Python.  
The goal is to build a clean and maintainable implementation of the classic Snake game rather than focusing on advanced graphics or effects.

---

## 🕹️ Project Overview
This project implements a Snake game using the Python Turtle library.  
The overall game flow is managed through a controller-based structure, separating keyboard input, movement logic, collision detection, and score management to improve readability and maintainability.

---

## 🔧 Key Features
- **Event-Driven Game Loop**  
  Uses `ontimer` instead of a traditional infinite loop  
- **Keyboard Controls**  
  WASD keys for directional movement  
- **Dynamic Difficulty**  
  Game speed increases as the snake grows  
- **Collision Detection**  
  Handles both wall collisions and self-collisions  
- **Score System**  
  Displays the current score and tracks the highest score  

---

## 📁 Project Structure
```text
.
├── snake.py        # Main game implementation
├── .gitignore
└── README.md
```

## 🚀 Quick Start

### Requirements
- Python 3.x

### Run the Game
```bash
python snake.py
```

## 🧠 Design Notes
- Game logic is organized using a controller class  
- Updates are scheduled with an event-driven approach  
- Rendering and game state management are clearly separated  

---

## 📌 Notes
This project is intended for learning and portfolio demonstration purposes, focusing on code structure and logic design rather than production-level optimization.