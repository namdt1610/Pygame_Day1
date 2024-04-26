from src.core.engine import Engine
from src.stages.menu import menu
from src.stages.play import play

e = Engine("DayOne")
# e.register("Menu", menu)
e.register("Play", play)
e.switch_to("Play")
e.run()
