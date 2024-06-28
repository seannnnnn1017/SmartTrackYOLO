from ultralytics import YOLO

model = YOLO('models\yolov9c.pt')

result=model.track('input_videos\Packaging-Box-Manufacturing-Business02.jpg',conf=0.9, save=True)
#print(result)
#print('boxes:')
#for box in result[0].boxes:
#    print(box)