'''
Extract usefull features from screenshots.
'''

import numpy as np
import scipy.ndimage as ndi
import colors


def screenshot(sct):
    return np.array(sct.grab(sct.monitors[0]))[:, :, :3]


def iscolor(img, color):
    return np.all(img == color, axis=-1)


def biggest(label, max_label):
    label_size = [(label == i).sum() for i in range(1, max_label + 1)]
    sorted_label = np.argsort(label_size) + 1
    biggest_label = sorted_label[-1]
    return label == biggest_label


def find(img, color):
    mask = iscolor(img, color)
    mask = biggest(*ndi.label(mask))
    return ndi.find_objects(mask, max_label=1)[0]


def get_monitor(img):
    box = find(img, colors.green)
    return {
        'left': box[1].start // 2,
        'top': box[0].start // 2,
        'width': (box[1].stop - box[1].start) // 2,
        'height': (box[0].stop - box[0].start) // 2
    }


def get_frame(sct, monitor):
    return np.array(sct.grab(monitor))[..., :3]


def box2loc(box, dsize):
    x = (box[1].start + box[1].stop) / 2
    y = dsize[1] - (box[0].start + box[0].stop) / 2
    return x, y


def locate(img, dsize, color):
    return box2loc(find(img, color), dsize)


# import cv2
#
# def mask2img(mask):
#     return 255*mask.astype('uint8')
#
#
# def imshow(img):
#     cv2.imshow('output', img)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
#     cv2.waitKey(1)
