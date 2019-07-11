import os

import numpy as np
from skimage.io import imread, imsave

from degas.color import white_balance

IMAGE_PATH = './tests/data/chelsea.png'
LOGS_DIR = './logs/test_wb/'


def test_cb_simple():
    src = imread(IMAGE_PATH)
    wb = white_balance.simple(src, f=.01, cut_off=0.01)

    assert src.shape == wb.shape
    assert not np.all(wb == 0)

    if not os.path.isdir(LOGS_DIR):
        os.makedirs(LOGS_DIR)

    imsave(LOGS_DIR + 'chelsea_src.tiff', src)
    imsave(LOGS_DIR + 'chelsea_wb.tiff', wb)
