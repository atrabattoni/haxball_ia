import colors
import cv2
import mss
import time
import image_processing as ip
import ia

DSIZE = (420, 205)

time.sleep(1)
with mss.mss() as sct:

    monitor = ip.get_monitor(ip.screenshot(sct))

    while True:
        t0 = time.time()

        img = ip.get_frame(sct, monitor)
        img = cv2.resize(img, DSIZE, interpolation=cv2.INTER_AREA)

        xp, yp = ip.locate(img, DSIZE, colors.red)
        xb, yb = ip.locate(img, DSIZE, colors.white)
        ia.moveTowardBall(xp, yp, xb, yb)

        fps = 1 / (time.time() - t0)
        print(fps)
        # cv2.imshow('output', img)
        # if cv2.waitKey(10) & 0xFF == ord("q"):
        #     cv2.destroyAllWindows()
        #     cv2.waitKey(1)
        #     break
