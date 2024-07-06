from FPS import FPS
from FPS import ScreenCaptureStream
import cv2
from ultralytics import YOLO
from tracker import YOLOTracker
from FPS import FPS
from FPS import ScreenCaptureStream

# 使用 ScreenCaptureStream 類來捕捉螢幕影像
capture_width, capture_height = 1280, 720
vs = ScreenCaptureStream(capture_width, capture_height).start()

# 初始化 FPS 計算器並開始計數
fps = FPS().start()

# 初始化 YOLOTracker
# 加載 YOLO 模型
model = YOLO('models/yolov5l6.pt')
CLASS_NAMES = model.names
tracker = YOLOTracker(model)
tracker.start()

while True:
    # 從螢幕影像流中讀取幀
    frame = vs.read()
    
    # 更新 YOLOTracker 中的最新幀
    tracker.update_frame(frame)

    # 獲取 YOLOTracker 中的最新檢測結果
    results = tracker.get_results()

    # 繪製檢測結果
    if results is not None:
        for result in results:
            for box in result.boxes:
                cls_id = int(box.cls)
                if CLASS_NAMES[cls_id] == 'person':
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    confidence = float(box.conf[0])
                    # 繪製矩形框
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    # 在框上標記置信度
                    cv2.putText(frame, f'{confidence:.2f}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

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