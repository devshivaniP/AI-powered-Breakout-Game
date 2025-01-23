# AI-Powered Breakout Game

This project is a Python-based breakout game built using the Pygame library. The game features an AI-controlled paddle, dynamic brick layouts, and engaging gameplay mechanics. It is a great demonstration of basic game development concepts and the integration of AI for automation.

---

## Features

- **Player or AI-Controlled Paddle**: 
  - Play manually or let the AI control the paddle.
- **Dynamic Brick Layout**:
  - A grid of bricks with multiple rows and columns.
- **Collision Detection**:
  - Ball interacts with bricks, paddle, and screen edges.
- **Win/Lose Conditions**:
  - Win by clearing all bricks or lose when the ball misses the paddle.

---

## Prerequisites

1. **Python**: Ensure you have Python 3.7 or later installed.
2. **Pygame Library**: Install Pygame using the following command:

   ```bash
   pip install pygame
   ```

---


## Gameplay Instructions

1. **Manual Control**:
   - Use the Left and Right arrow keys to move the paddle.
2. **AI Control**:
   - Enable AI by setting `ai_enabled = True` in the code.
3. Avoid letting the ball fall below the paddle.
4. Clear all the bricks to win the game.

---

## Code Overview

### Key Components

- **Paddle**: 
  - Moves horizontally at the bottom of the screen to deflect the ball.
- **Ball**: 
  - Bounces around the screen, destroying bricks and interacting with the paddle.
- **Bricks**: 
  - Arranged in a grid; disappear when hit by the ball.
- **AI Logic**: 
  - Tracks the ball's position and moves the paddle automatically.

### Main Functions

- `main()`: Handles the main game loop.
- `collision_detection()`: Manages ball interactions with bricks and paddle.
- `draw()`: Updates the screen with the latest game state.

---

## Customization

1. **Change Game Difficulty**:
   - Modify `ball_dx` and `ball_dy` for ball speed.
   - Adjust `paddle_speed` for paddle movement speed.
2. **Modify Brick Layout**:
   - Change `BRICK_ROWS` and `BRICK_COLUMNS` for different grids.
3. **Enable/Disable AI**:
   - Toggle `ai_enabled` in the code.

---

## Future Improvements

- **Dynamic Difficulty**: Increase ball speed as the game progresses.
- **Power-Ups**: Add features like multi-ball or paddle size changes.
- **Scoring System**: Display scores for bricks destroyed.
- **Sound Effects**: Add sound for ball collisions and other events.

---

## Credits

- Developed using Python and Pygame.
- Inspired by the classic Breakout game.

---

## License

This project is open-source and available for personal or educational use. Feel free to modify and expand the code.

