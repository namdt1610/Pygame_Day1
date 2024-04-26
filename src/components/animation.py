import pygame

class Animation:
    def __init__(self, images, duration):
        """
        images: a list of image paths or pygame.Surface objects
        duration: total duration of one loop of the animation
        """
        self.frames = [pygame.image.load(img) if isinstance(img, str) else img for img in images]
        self.duration = duration
        self.current_time = 0
        self.current_frame_index = 0

    def update(self, dt):
        """
        Update the animation state. Should be called once per frame.
        dt: time elapsed since the last frame
        """
        self.current_time += dt
        while self.current_time >= self.duration:
            self.current_time -= self.duration
            self.current_frame_index = (self.current_frame_index + 1) % len(self.frames)

    def get_current_frame(self):
        """
        Get the current frame of the animation.
        """
        return self.frames[self.current_frame_index]