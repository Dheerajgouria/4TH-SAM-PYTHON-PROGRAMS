import cv2
import time
import os

# Load the classifiers
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade  = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Start the camera (0 = default camera)
cap = cv2.VideoCapture(0)

# Check if camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera. Please grant camera permissions in System Preferences.")
    print("System Preferences > Security & Privacy > Camera > Allow Terminal/Python")
    exit(1)

print("Camera started. Looking for face and eyes...")

photo_count = 0
save_folder = "/Users/mac/Desktop/face detection capture"
os.makedirs(save_folder, exist_ok=True)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Camera not working!")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
        # Draw rectangle around face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Look for eyes inside the face region only
        face_gray = gray[y:y+h, x:x+w]
        face_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(face_gray, scaleFactor=1.1, minNeighbors=10)

        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(face_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

        # Both face AND eyes detected — capture!
        if len(eyes) >= 1:
            photo_count += 1
            filename = os.path.join(save_folder, f"photo_{photo_count}.jpg")
            cv2.imwrite(filename, frame)
            print(f"Photo captured: {filename}")
            time.sleep(2)  # Wait 2 seconds before capturing again

    # Show live preview window
    cv2.imshow("Face & Eye Detection", frame)

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print("Camera stopped.")