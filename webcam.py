import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        "No stream from webcam"
        break
    # Ajouter une étape de processing de l'image :
    # ...
    cv2.imshow("Webcam", frame)
    if cv2.waitKey(1) == ord('q'):
        break
