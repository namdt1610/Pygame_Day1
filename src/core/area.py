from src.core.map import Map

area = None
map_folder_location = "../content/maps"


class Area:
    def __init__(self, area_file, tile_types):
        self.name = None
        self.map = None
        self.entities = []
        global area
        area = self
        self.tile_types = tile_types
        self.load_area_file(area_file)

    # Remove an entity to the area
    def remove_entity(self, e):
        self.entities.remove(e)
        for c in e.components:
            g = getattr(c, "breakdown", None)
            if callable(g):
                c.breakdown()

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

        self.name = area_file.split('.')[0].title().replace('_', ' ')

        from src.core.engine import engine
        engine.reset()

        # Split up the data by minus signs
        chunks = data.split('-')
        tile_map_data = chunks[0]
        entity_data = chunks[1]

        # Load the map
        self.map = Map(tile_map_data, self.tile_types)

        # Load the entities
        self.entities = []
        entity_lines = entity_data.split('\n')[1:]
        for i, line in enumerate(entity_lines, start=1):
            try:
                items = line.split(',')
                if all(item.strip() for item in items[:3]):  # Check if the first three items are not empty
                    id = int(items[0])
                    x = int(items[1])
                    y = int(items[2])
                    self.entities.append(create_entity(id, x, y, items[3:]))
                else:
                    print(f"Skipping line {i}: {line}\nReason: contains empty values.")
            except Exception as e:
                print(f"Error parsing line: {line}. Error: {str(e)}")
