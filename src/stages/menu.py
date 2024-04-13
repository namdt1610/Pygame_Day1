from src.components.button import Button
from src.components.entity import Entity
from src.components.label import Label
from src.components.sprite import Sprite


def new_game():
    from src.core.engine import engine
    engine.switch_to("Play")


def quit_game():
    from src.core.engine import engine
    engine.running = False


def menu():
    Entity(Sprite("menu.png", is_ui=True))
    new_game_button = Entity(Label("main/Pixellari.ttf", "New Game", 80, (255, 255, 255)).check_hover())
    quit_game_button = Entity(Label("main/Pixellari.ttf", "Quit", 80, (255, 255, 255)).check_hover())

    new_button_size = new_game_button.get(Label).get_bounds()
    quit_button_size = quit_game_button.get(Label).get_bounds()

    from src.core.camera import camera
    new_game_button.x = camera.width / 2 - new_button_size.width / 2
    new_game_button.y = camera.height - 300
    quit_game_button.x = camera.width / 2 - quit_button_size.width / 2
    quit_game_button.y = camera.height - 200

    new_game_button.add(Button(new_game, new_button_size))
    quit_game_button.add(Button(quit_game, new_button_size))
