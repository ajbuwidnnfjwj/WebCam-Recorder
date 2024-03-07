import cv2 as cv
import numpy as np

vid_num = 0
fourcc = 'XVID'
webcam = cv.VideoCapture(0)
out = cv.VideoWriter()

while webcam.isOpened():
    status, frame = webcam.read()

    if status:
        cv.imshow("WebCam Recorder", frame)

    key = cv.waitKey(10)
    if key == 27:
        break
    elif key == ord(' '):
        h, w, *_ = frame.shape
        out.open('./record{}.avi'.format(vid_num), cv.VideoWriter_fourcc(*fourcc), webcam.get(cv.CAP_PROP_FPS), (w, h))
        while key != 27:
            status, frame = webcam.read()
            cv.circle(frame, (w//2,10), radius=5, color=(0, 0, 255), thickness=5)
            if status:
                cv.imshow("WebCam Recorder", frame)
                out.write(frame)

            key = cv.waitKey(10)
            if key == ord(' '):
                vid_num += 1
                break
        else:
            break
else:
    canvas = np.full((120, 60), 255, dtype=np.uint8)
    cv.putText(canvas, 'Cannot find camera', (canvas.shape[1]//2, canvas.shape[0]//2), cv.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 0))
    cv.waitKey()
    cv.destroyAllWindows()
    exit()

out.release()