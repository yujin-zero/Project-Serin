class Camera:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.x = 0
        self.y = 0

    def update(self, target):
        self.x = target.rect.centerx - self.screen_width // 2
        self.y = target.rect.centery - self.screen_height // 2

        self.x = max(0, min(self.x, target.boundary_width - self.screen_width))
        self.y = max(
            0, min(self.y, target.boundary_height - self.screen_height))
