from FPS import FPS
from FPS import ScreenCaptureStream
import cv2

# 使用 ScreenCaptureStream 類來捕捉螢幕影像
capture_width, capture_height = 1280, 720
vs = ScreenCaptureStream(capture_width, capture_height).start()

# 初始化 FPS 計算器並開始計數
fps = FPS().start()

while True:
    # 從螢幕影像流中讀取幀
    frame = vs.read()
    
    # 在幀上顯示當前的 FPS
    cv2.putText(frame, f"FPS: {fps.fps()}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    # 顯示螢幕影像
    cv2.imshow("Screen Capture", frame)

    # 更新幀數
    fps.update()

    # 按下 'ESC' 鍵退出循環
    if cv2.waitKey(1) == 27:
        break

# 停止螢幕捕捉並釋放所有資源
vs.stop()
fps.stop()
cv2.destroyAllWindows()
