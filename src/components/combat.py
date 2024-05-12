class Combat:
    def __init__(self, health, on_death):
        self.amount = None
        self.entity = None
        self.health = health
        self.max_health = health
        self.global_cooldown = 0
        self.equipped = None
        self.regen = 0.01
        self.on_death = on_death
        self.weapon_sprite = None
        from src.core.engine import engine
        engine.active_objs.append(self)

    # Equip an item
    def equip(self, item):
        from src.components.entity import Entity
        from src.components.sprite import Sprite
        self.equipped = item
        if self.equipped is not None:
            print(self.entity, "equipping", self.equipped.icon_name)
            self.weapon_sprite = Entity(Sprite(self.equipped.icon_name)).get(Sprite)

    # Unequip an item
    def unequip(self):
        print("calling unequipped")
        self.equipped = None
        self.weapon_sprite.entity.delete_self()
        self.weapon_sprite = None
        print("Weapon sprite", self.weapon_sprite)

    # Breakdown an item
    def breakdown(self):
        from src.core.engine import engine
        engine.active_objs.remove(self)

    # Attack another entity
    def attack(self, other):
        damage = int(self.equipped.stats['damage'])
        if self.equipped is None:
            damage = 1

        # If we are still on cooldown
        if self.global_cooldown > 0:
            return

        other.health -= damage
        self.global_cooldown = self.equipped.stats['cooldown'] * 60
        print(self.global_cooldown)

        from src.core.effect import create_hit_text
        create_hit_text(other.entity.x, other.entity.y, str(damage), (255, 0, 0))
        # Effect(self.entity.x, self.entity.y, 0, 0, 5, self.equipped.icon)

        print(f"Took {damage} damage. Has {other.health}")
        if other.health <= 0:
            other.on_death(other.entity)

    # Perform an attack
    def perform_attack(self):
        if self.equipped is None:
            return
        if self.equipped.type == "weapon":
            from src.components.physics import get_bodies_within_circle
            nearby_objs = get_bodies_within_circle(self.entity.x,
                                                   self.entity.y,
                                                   self.equipped.stats['range'])
            print("Nearby Objs", nearby_objs)
            for o in nearby_objs:
                print(o.entity.components)
                if o.entity.has(Combat) and o.entity != self.entity:
                    self.attack(o.entity.get(Combat))

    def update(self):
        if self.global_cooldown > 0:
            self.global_cooldown -= 1
        if self.health < self.max_health:
            self.health += self.regen
        if self.health > self.max_health:
            self.health = self.max_health

        if self.weapon_sprite is not None:
            self.weapon_sprite.entity.x = self.entity.x
            self.weapon_sprite.entity.y = self.entity.y + 16
