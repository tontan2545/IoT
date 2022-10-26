import face_recognition
import cv2

file_location = './assets/Face.jpg'

img = face_recognition.load_image_file(file_location)
face_location = face_recognition.face_locations(img)
print(f'There are {len(face_location)} people in this image')

x0 = face_location[0][3]
y0 = face_location[0][0]
x1 = face_location[0][1]
y1 = face_location[0][2]

img2 = cv2.imread(file_location)
cv2.rectangle(img2,(x0,y0),(x1,y1),(255,0,0),3)
cv2.imshow('Face Location Draw rectangle',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()