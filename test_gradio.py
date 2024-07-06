import gradio as gr
from PIL import Image
import cv2
import numpy as np
from ultralytics import YOLO

# Load YOLO model
model = YOLO('models/yolov9c.pt')
CLASS_NAMES = model.names

def detect_and_track(image):
    if image is None:
        return 'ERROR: Please provide an image', None
    # Convert PIL Image to NumPy array
    np_image = np.array(image)

    # Convert RGB to BGR for OpenCV
    frame = cv2.cvtColor(np_image, cv2.COLOR_RGB2BGR)
    
    results = model.track(frame, conf=0.4, save=False)

    # Draw the boxes and labels
    for result in results:
        for box in result.boxes:
            cls_id = int(box.cls)
            if CLASS_NAMES[cls_id] == 'person':
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                confidence = float(box.conf[0])
                # Draw rectangle and label confidence
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, f'{confidence:.2f}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Convert back to RGB from BGR and then to PIL Image
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    return 'Detected and tracked',Image.fromarray(frame_rgb)

iface = gr.Interface(fn=detect_and_track, inputs="image", outputs=[gr.Textbox(label="output"),"image"])
iface.launch(share=True)
