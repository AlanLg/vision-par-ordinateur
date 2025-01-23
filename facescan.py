import cv2

cap = cv2.VideoCapture(0)

haar_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')

while True:
    ret, frame = cap.read()
    if not ret:
        "No stream from webcam"
        break

    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces_rect = haar_cascade.detectMultiScale(gray_img, 1.1, 9)

    for (x, y, w, h) in faces_rect:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        BLACK = (255, 255, 255        # BLACK = (255, 255, 255)
        # font = cv2.FONT_HERSHEY_SIMPLEX
        # font_size = 1.1
        # font_color = BLACK
        # font_thickness = 2
        # text = 'IMPOSTER'
        # cv2.putText(frame, text, (x, y), font, font_size, font_color, font_thickness, cv2.LINE_AA)
)
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_size = 1.1
        font_color = BLACK
        font_thickness = 2
        text = 'IMPOSTER'
        cv2.putText(frame, text, (x, y), font, font_size, font_color, font_thickness, cv2.LINE_AA)

    cv2.imshow("Webcam", frame)
    if cv2.waitKey(1) == ord('q'):
        break
