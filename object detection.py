### croped images
import os
import cv2
import matplotlib.pyplot as plt

path = '/content/drive/MyDrive/Data/AR03-101-01'
for img in os.listdir(path):
  if img.endswith('.png'):
    image = os.path.join(path,img)
    image_read = cv2.imread(image)
    a = cv2.cvtColor(image_read, cv2.COLOR_BGR2RGB)
    x, y, w, h = 500,400,1200,1200
    crop = a[y:y+h, x:x+w]

  plt.imshow(crop)
  plt.show()

crop.shape



### Object Detection
import cv2
face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")


frames_capture = cv2.VideoCapture(0)


def detect_bounding_box(vid):
    gray_image = cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray_image, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(vid, (x, y), (x + w, y + h), (0, 255, 0), 4)
    return faces


while True:

    result, frame = frames_capture.read()  
    if result is False:
        break  

    faces = detect_bounding_box(frame)  
    cv2.imshow(frame) 
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

frames_capture.release()
cv2.destroyAllWindows()

