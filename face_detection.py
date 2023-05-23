import cv2
#Read image path
img = cv2.imread('sample1.jpg')
#convert image to greyscale
gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
#Load the classifier
face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
#perform face detection
face = face_classifier.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40))
for (x, y, w, h) in face:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 10)
cv2.imwrite("output.jpg",img)
