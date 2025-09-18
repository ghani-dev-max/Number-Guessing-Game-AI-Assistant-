# Number Guessing Game (AI Assistant)

A Python-based number guessing game where both the AI and the user take turns guessing numbers.  
The AI uses binary search to guess efficiently, while the user tries to beat the AI within limited attempts.

## Features
- Two modes:
  1. **AI guesses your number**  
  2. **You guess AI's number**
- Dynamic attempt limits based on range size (log2 of the range).
- Scoreboard to track rounds won by AI and user.
- Clear, simple instructions for both modes.

## Requirements
- Python 3.x (no external libraries required)

## How to Play

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/number-guessing-game.git
   cd number-guessing-game
   ```

2. Run the game:
   ```bash
   python number_guessing_game.py
   ```

3. Choose a game mode:
   - **1** → AI tries to guess your number.  
   - **2** → You try to guess AI's number.  

4. Follow the on-screen instructions:
   - If AI is guessing: type `low`, `high`, or `correct`.  
   - If you are guessing: type numbers until you find the secret one.  

## License
This project is released under the MIT License.
