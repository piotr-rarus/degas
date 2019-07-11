import os

import numpy as np
from skimage import img_as_ubyte
from skimage.color import rgb2gray
from skimage.io import imread, imsave

from degas.exposure import dclahe

IMAGE_PATH = './tests/data/chelsea.png'
LOGS_DIR = './logs/test_dclahe/'


def test_dclahe():
    src = imread(IMAGE_PATH)
    gray = rgb2gray(src)
    gray = img_as_ubyte(gray)
    eq = dclahe(gray, max_clip_limit=0.03)
    eq = img_as_ubyte(eq)

    assert src.shape[:-1] == eq.shape
    assert not np.all(eq == 0)

    if not os.path.isdir(LOGS_DIR):
        os.makedirs(LOGS_DIR)

    imsave(LOGS_DIR + 'chelsea_gray.tiff', gray)
    imsave(LOGS_DIR + 'chelsea_dclahe.tiff', eq)
