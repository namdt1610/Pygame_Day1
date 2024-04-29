class Animation:
    def __init__(self, frames, duration):
        """
        frames: danh sách các frame hình ảnh
        duration: tổng thời gian của một chu kỳ animation
        """
        self.frames = frames
        self.duration = duration
        self.current_time = 0
        self.current_frame_index = 0

    def update(self, dt):
        """
        Cập nhật trạng thái của animation. Nên được gọi một lần mỗi frame.
        dt: thời gian đã trôi qua kể từ frame trước đó
        """
        self.current_time += dt
        while self.current_time >= self.duration:
            self.current_time -= self.duration
            self.current_frame_index = (self.current_frame_index + 1) % len(self.frames)

    def get_current_frame(self):
        """
        Lấy frame hiện tại của animation.
        """
        return self.frames[self.current_frame_index]
