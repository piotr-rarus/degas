import numpy as np
from austen import Logger
from skimage.color import rgb2gray
from skimage.io import imread

from degas import FluentImage
from degas.color import white_balance
from degas.exposure import dclahe

IMAGE_PATH = './tests/data/chelsea.png'
LOGS_DIR = './logs/test_fluent/'


def test_fluent():
    src = imread(IMAGE_PATH)

    with Logger(LOGS_DIR) as logger:
        with FluentImage(src, logger) as src_fluent:

            src_fluent >> (
                white_balance.simple,
                {
                    'f': .01,
                    'cut_off': .01
                }
            ) >> (
                rgb2gray
            ) >> (
                dclahe
            )

            assert src_fluent.image.shape == src.shape[:-1]
            assert not np.all(src_fluent.image == 0)


def test_fluent_2():
    src = imread(IMAGE_PATH)

    with Logger(LOGS_DIR) as logger:
        with FluentImage(src, logger, inter_save=False) as src_fluent:

            src_fluent >> (
                white_balance.simple,
                {
                    'f': .01,
                    'cut_off': .01
                }
            ) >> (
                rgb2gray
            ) >> (
                dclahe
            )

            assert src_fluent.image.shape == src.shape[:-1]
            assert not np.all(src_fluent.image == 0)


def test_fluent_3():
    src = imread(IMAGE_PATH)

    with FluentImage(src) as src_fluent:
        src_fluent >> (
            white_balance.simple,
            {
                'f': .01,
                'cut_off': .01
            }
        ) >> (
            rgb2gray
        ) >> (
            dclahe
        )

        assert src_fluent.image.shape == src.shape[:-1]
        assert not np.all(src_fluent.image == 0)
