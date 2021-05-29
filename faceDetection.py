import cv2
from colors import white, black, blue

def detectFace():
    counter = 0
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    cap = cv2.VideoCapture(0)
    cv2.namedWindow('face-detection', cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty('face-detection', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    while True:
        _, frame = cap.read()
        frame = cv2.flip(frame, 1)

        cv2.putText(frame, "Waiting for user...", (65, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, black, 2)
        cv2.rectangle(frame, (40, 10), (600, 450), black, 2)
        cv2.rectangle(frame, (50, 20), (590, 440), blue, 2)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        if (len(faces) == 1):
            (x, y, w, h) = faces[0]
            if (w > 150 and h > 150):
                counter = counter + 1
                cv2.rectangle(frame, (x, y), (x + w, y + h), blue, 2)
                if(counter == 20):
                    cap.release()
                    return True

        # Display
        cv2.imshow('face-detection', frame)

        # Stop if escape key is pressed
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

    # Release the VideoCapture object
    cap.release()
    cv2.destroyAllWindows()
    return False


# print(detectFace())