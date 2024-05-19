class Camera:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.x = 0
        self.y = 0
    
    def update(self, target_rect, boundary_width, boundary_height):
        self.x = target_rect.x - self.screen_width // 2 + target_rect.width // 2
        self.y = target_rect.y - self.screen_height // 2 + target_rect.height // 2

        self.x = max(0, min(self.x, boundary_width - self.screen_width))
        self.y = max(0, min(self.y, boundary_height - self.screen_height))
