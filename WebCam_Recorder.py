import cv2 as cv

path = './record.avi'
fourcc = 'XVID'
webcam = cv.VideoCapture(0)
out = cv.VideoWriter()

while webcam.isOpened():
    status, frame = webcam.read()

    if status:
        cv.imshow("test", frame)

    key = cv.waitKey(10)
    if key == 27:
        break
    elif key == ord(' '):
        h, w, *_ = frame.shape
        out.open(path, cv.VideoWriter_fourcc(*fourcc), webcam.get(cv.CAP_PROP_FPS), (w, h))
        while key != 27:
            status, frame = webcam.read()
            cv.circle(frame, (w//2,10), radius=10, color=(0, 0, 255), thickness=5)
            if status:
                cv.imshow("test", frame)
                out.write(frame)

            key = cv.waitKey(10)
            if key == ord(' '):
                break
        else:
            break

else:
    print("?")
    exit()
out.release()