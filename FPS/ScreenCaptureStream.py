from threading import Thread
import cv2
import numpy as np
import pyautogui

class ScreenCaptureStream:
    def __init__(self, capture_width=1280, capture_height=720):
        # 设置捕获窗口的大小
        self.capture_width = capture_width
        self.capture_height = capture_height
        # 初始化第一帧
        self.frame = self.grab_screen()
        self.stopped = False

    def start(self):
        # 启动线程来更新屏幕捕获
        Thread(target=self.update, args=()).start()
        return self

    def update(self):
        while True:
            if self.stopped:
                return
            self.frame = self.grab_screen()

    def read(self):
        return self.frame

    def stop(self):
        self.stopped = True

    def grab_screen(self):
        # 获取屏幕截图
        screenshot = pyautogui.screenshot()
        # 将截图转换为OpenCV图像
        frame = np.array(screenshot)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # 转换颜色通道
        # 调整捕获窗口的大小
        frame = cv2.resize(frame, (self.capture_width, self.capture_height))
        return frame

