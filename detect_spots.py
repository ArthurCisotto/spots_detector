import os
from ultralytics import YOLO
import cv2
import numpy as np
from compare_imgs import *
import glob


# Erase all the content of the folder spots_detected
files = glob.glob('spots_detected/*')
for f in files:
    os.remove(f)

VIDEOS_DIR = os.path.join('.', 'videos')

video_path = os.path.join(VIDEOS_DIR, 'VIDEO1.mp4')
video_path_wo_format = video_path.split('.mp4')[0]
video_path_out = '{}_out_1.mp4'.format(video_path_wo_format)

cap = cv2.VideoCapture(video_path)
ret, frame = cap.read()
H, W, _ = frame.shape
out = cv2.VideoWriter(video_path_out, cv2.VideoWriter_fourcc(*'MP4V'), int(cap.get(cv2.CAP_PROP_FPS)), (W, H))

model_path = os.path.join('.', 'runs', 'detect', 'train7', 'weights', 'best.pt')

# Load a model
model = YOLO(model_path)  # load a custom model

threshold = 0.5

n = 0 # Number of imgs saved in spots_detected

while ret:

    results = model(frame)[0]

    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result

        if score > threshold:
            try:
                img_spot = frame[int(y1)-5:int(y2)+5, int(x1)-5:int(x2)+5]

                error = compare_imgs(img_spot, n)

                # If the error is too high, the image is different. So we save the new image
                if (error > 25) | (n==0):
                    cv2.imwrite(f'spots_detected/img_spot{n}.jpeg', img_spot)
                    n+=1

                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
                #cv2.putText(frame, results.names[int(class_id)].upper(), (int(x1), int(y1 - 10)),
                #            cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)

            except:
                pass

    out.write(frame)
    ret, frame = cap.read()

cap.release()
out.release()
cv2.destroyAllWindows()
