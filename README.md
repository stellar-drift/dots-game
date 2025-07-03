# dots-game
Just a little game built with Pygame (https://www.pygame.org/), done for practice



Gameplay
- Use arrow keys to move your dot
- Collect as many yellow dots as you can
- The enemy will chase you when you're nearby
- Game ends when you're caught


Features
- 2D pixel-style visuals using Pygame's built-in drawing tools
- Dynamic enemy AI with color & speed boost
- Score popups with smooth fade-out
- Sound effects and background music
- Game over overlay with clickable buttons

Future
- Currently game just starts once opened, will need to add a start screen 


Requirements
- Python 3.8+
- Pygame (https://pypi.org/project/pygame/)


Project Structure
.
|-- main.py             # Game loop and event handling
|-- settings.py         # Configurations and constants
|-- player.py           # Player class
|-- enemy.py            # Enemy class and behavior
|-- collectible.py      # Collectibles and score logic
|-- overlay.py          # Game over screen and buttons
|-- sounds/
|   |-- clave_low.mp3
|   |-- enemy_alert.mp3
|   |-- game_over.mp3
|   |-- spiritual_evolution_dance.mp3

        ** sound effects found on pixabay
        ** background music found on internet archive



How to Run the Game (if downloaded)
       ** the download file only is only for macOS at the moment

On macOS (.app)
1. Download 
2. Double-click the DotsGame.app file to open
3. If macOS warns about the app being from an unidentified developer, right click (or Ctrl_click) the app and select Open, then confirm you want to run it
4. Enjoy playing!

