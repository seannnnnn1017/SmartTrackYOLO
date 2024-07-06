import cv2
import numpy as np
import pyautogui
from FPS import FPS

# 螢幕大小
screen_width, screen_height = pyautogui.size()

# 設置捕捉視窗大小
capture_width, capture_height = 1280, 720

# 創建影片寫入對象
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('screen_capture.avi', fourcc, 20.0, (capture_width, capture_height))
fps = FPS().start()

### 主程式 ###
while True:
    # 獲取螢幕截圖
    screenshot = pyautogui.screenshot()
    #time.sleep(0.01)  # 增加延遲以減少CPU負載
    
    # 將截圖轉換為OpenCV圖像
    frame = np.array(screenshot)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # 調整捕捉視窗的大小
    frame = cv2.resize(frame, (capture_width, capture_height))
    
    # 將螢幕截圖寫入影片文件 
    out.write(frame)
    


    cv2.putText(frame, f"FPS: {int(fps.fps())}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    # 顯示螢幕截圖
    cv2.imshow('Screen Capture', frame)
    fps.update()
    # 按'ESC'鍵退出循環
    if cv2.waitKey(1) == 27:
        break

# 釋放影片捕獲對象和關閉窗口
fps.stop()
out.release()
cv2.destroyAllWindows()
