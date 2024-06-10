

class HealthBoostItem:
    def __init__(self, health_increase):
        self.health_increase = health_increase

    def apply(self, character):
        character.max_health += self.health_increase
        character.health += self.health_increase
        if character.health > character.max_health:
            character.health = character.max_health
