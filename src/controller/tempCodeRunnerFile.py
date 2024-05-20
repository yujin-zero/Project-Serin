                    distance = 400
                    x = self.player.rect.x + distance * math.cos(angle)
                    y = self.player.rect.y + distance * math.sin(angle)
                    monster = monster_class(x, y)
                    self.game_object.add(monster)
