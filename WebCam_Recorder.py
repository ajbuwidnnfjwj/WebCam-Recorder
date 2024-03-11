import cv2 as cv
import numpy as np

vid_num = 0
fourcc = 'XVID'
webcam = cv.VideoCapture(0)
out = cv.VideoWriter()

contrast = 1
contrast_step = 0.1
brightness = 0
brightness_step = 1

while webcam.isOpened():
    status, frame = webcam.read()
    
    frame = contrast * frame + brightness
    frame[frame < 0] = 0
    frame[frame > 255] = 255
    frame = frame.astype(np.uint8)

    key = cv.waitKey(10)
    if key == 27:
        break
    elif key == ord('+'):
        contrast += contrast_step
    elif key == ord('-'):
        contrast -= contrast_step
    elif key == ord(']'):
        brightness += brightness_step
    elif key == ord('['):
        brightness -= brightness_step
    elif key == ord(' '):
        h, w, *_ = frame.shape
        out.open('./record{}.avi'.format(vid_num), cv.VideoWriter_fourcc(*fourcc), webcam.get(cv.CAP_PROP_FPS), (w, h))
        while key != 27:
            status, frame = webcam.read()
            cv.circle(frame, (w//2,10), radius=5, color=(0, 0, 255), thickness=5)
            if status:
                frame = contrast * frame + brightness
                frame[frame < 0] = 0
                frame[frame > 255] = 255
                frame = frame.astype(np.uint8)
                cv.imshow("WebCam Recorder", frame)
                out.write(frame)

            key = cv.waitKey(10)
            if key == ord(' '):
                vid_num += 1
                break
            elif key == ord('+'):
                contrast += contrast_step
            elif key == ord('-'):
                contrast -= contrast_step
            elif key == ord(']'):
                brightness += brightness_step
            elif key == ord('['):
                brightness -= brightness_step
        else:
            break

    if status:
        cv.imshow("WebCam Recorder", frame)
else:
    canvas = np.full((120, 60), 255, dtype=np.uint8)
    cv.putText(canvas, 'Cannot find camera', (canvas.shape[1]//2, canvas.shape[0]//2), cv.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 0))
    cv.waitKey()
    cv.destroyAllWindows()
    exit()

out.release()