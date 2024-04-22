from src.components.usable import Usable

npc_folder_location = "../content/npcs"
npc_talk_distance = 150


class NPC(Usable):
    def __init__(self, obj_name, npc_file):
        super().__init__(obj_name)
        self.npc_file = npc_file

    # When the player interacts with the NPC
    def on(self, other, distance):
        from src.components.player import Player
        player = other.get(Player)
        if distance < npc_talk_distance:
            file = open(npc_folder_location + "/" + self.npc_file, "r")
            data = file.read()
            file.close()
            lines = data.split('\n')
            print(lines)

            from src.components.ui.dialogue_view import DialogueView
            DialogueView(lines, self, player)

        else:
            player.show_message("I need to get closer")
