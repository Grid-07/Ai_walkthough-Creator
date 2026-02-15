WALL_THICKNESS = 0.2
DEFAULT_HEIGHT = 3.0

class GeometryGenerator:

    def generate_room(self, room):
        x, y = room["position"]
        width = room["width"]
        length = room["length"]

        room_box = {
            "type": "room",
            "position": [x + width/2, y + length/2, DEFAULT_HEIGHT/2],
            "size": [width, length, DEFAULT_HEIGHT]
        }

        walls = self._generate_walls(x, y, width, length)

        return {
            "room": room_box,
            "walls": walls
        }

    def _generate_walls(self, x, y, width, length):
        walls = []

        # Bottom wall
        walls.append(self._wall(
            x + width/2,
            y - WALL_THICKNESS/2,
            width,
            WALL_THICKNESS
        ))

        # Top wall
        walls.append(self._wall(
            x + width/2,
            y + length + WALL_THICKNESS/2,
            width,
            WALL_THICKNESS
        ))

        # Left wall
        walls.append(self._wall(
            x - WALL_THICKNESS/2,
            y + length/2,
            WALL_THICKNESS,
            length
        ))

        # Right wall
        walls.append(self._wall(
            x + width + WALL_THICKNESS/2,
            y + length/2,
            WALL_THICKNESS,
            length
        ))

        return walls

    def _wall(self, center_x, center_y, width, depth):
        return {
            "type": "wall",
            "position": [center_x, center_y, DEFAULT_HEIGHT/2],
            "size": [width, depth, DEFAULT_HEIGHT]
        }

    def generate_floor(self, floor_plan):
        objects = []

        for room in floor_plan["rooms"]:
            generated = self.generate_room(room)
            objects.append(generated["room"])
            objects.extend(generated["walls"])

        return objects
