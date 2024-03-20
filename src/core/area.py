from src.core.map import Map

area = None
map_folder_location = "../content/maps"


class Area:
    def __init__(self, area_file, tile_types):
        self.map = None
        self.entities = []
        global area
        area = self
        self.tile_types = tile_types
        self.load_area_file(area_file)

    def reset_everything(self):
        from src.components.physics import triggers, bodies
        from src.components.sprite import sprites
        from src.components.entity import active_objs
        triggers.clear()
        bodies.clear()
        sprites.clear()
        active_objs.clear()
        self.entities = []

    # Search for the first entity of a kind
    def search_for_first(self, kind):
        for e in self.entities:
            c = e.get(kind)
            if c is not None:
                return e

    # Load the area file
    def load_area_file(self, area_file):
        from src.data.objects import create_entity

        # Read all the data from the file
        file = open(map_folder_location + "/" + area_file, "r")
        data = file.read()
        file.close()

        self.reset_everything()

        # Split up the data by minus signs
        chunks = data.split('-')
        tile_map_data = chunks[0]
        entity_data = chunks[1]

        # Load the map
        self.map = Map(tile_map_data, self.tile_types)

        # Load the entities
        self.entities = []
        entity_lines = entity_data.split('\n')[1:]
        for line in entity_lines:
            try:
                items = line.split(',')
                id = int(items[0])
                x = int(items[1])
                y = int(items[2])
                self.entities.append(create_entity(id, x, y, items[3:]))
            except Exception as e:
                print(f"Error parsing line: {line}. Error: {str(e)}")
