from src.components.usable import Usable

npc_folder_location = "../content/npcs"
npc_talk_distance = 150


class NPC(Usable):
    def __init__(self, obj_name, npc_file):
        super().__init__(obj_name)
        self.npc_file = npc_file
        self.has_read = False

    def on(self, other, distance):
        from src.components.player import Player
        player = other.get(Player)
        if distance < npc_talk_distance:
            if not self.has_read:
                file = open(npc_folder_location + "/" + self.npc_file, "r")
                data = file.read()
                file.close()
                lines = data.split('\n')

                from src.components.ui.dialogue_view import DialogueView
                DialogueView(lines, self, player)
                self.has_read = True
        else:
            player.show_message("I need to get closer")
