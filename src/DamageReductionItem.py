class DamageReductionItem:
    def __init__(self, damage_reduction):
        self.damage_reduction = damage_reduction

    # def apply(self, character):
    #     character.damage_reduction = self.damage_reduction
    #     character.health += character.damage_reduction
    #     if character.health < 0:
    #         character.kill()
