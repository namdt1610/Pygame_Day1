from pygame import Rect

bodies = []
triggers = []


# Reset the physics for the next area
def reset_physics():
    global bodies, triggers
    bodies.clear()
    triggers.clear()


# Check the collision between two objects
class PhysicalObj:
    def __init__(self, x, y, width, height):
        self.entity = None
        self.hitbox = Rect(x, y, width, height)

    def is_colliding_with(self, other):
        x = self.entity.x + self.hitbox.x
        y = self.entity.y + self.hitbox.y
        other_x = other.entity.x + other.hitbox.x
        other_y = other.entity.y + other.hitbox.y
        if x < other_x + other.hitbox.width and \
                x + self.hitbox.width > other_x and \
                y < other_y + other.hitbox.height and \
                y + self.hitbox.height > other_y:
            return True
        else:
            return False


# Trigger when collide with player
class Trigger(PhysicalObj):
    def __init__(self, on, x=0, y=0, width=32, height=32):
        super().__init__(x, y, width, height)
        triggers.append(self)
        self.on = on


# Declare the body of the object and check if the position is valid
class Body(PhysicalObj):
    def __init__(self, x=0, y=0, width=32, height=32):
        super().__init__(x, y, width, height)
        bodies.append(self)

    def is_position_valid(self):
        from src.core.area import area
        # Check if the position is valid
        x = self.entity.x + self.hitbox.x
        y = self.entity.y + self.hitbox.y
        if area.map.is_rect_solid(x, y, self.hitbox.width, self.hitbox.height):
            return False
        for body in bodies:
            if body != self and body.is_colliding_with(self):
                return False
        return True
