import numpy as np
from austen import Logger
from skimage.color import rgb2gray
from skimage.feature import canny
from skimage import morphology
from skimage.io import imread
from pathlib import Path

from degas import FluentNumpy

IMAGE = Path('./tests/data/chelsea.png')
LOGS = Path('./logs/')


def test_fluent():
    src = imread(str(IMAGE))

    logs_dir = LOGS.joinpath(test_fluent.__name__)

    with Logger(logs_dir) as logger:
        with FluentNumpy(src, logger) as src_fluent:

            src_fluent >> (
                rgb2gray
            ) >> (
                canny,
                {
                    'sigma': 3.0
                }
            ) >> (
                morphology.binary_dilation
            )

            assert src_fluent.image.shape == src.shape[:-1]
            assert not np.all(src_fluent.image == 0)


def test_fluent_2():
    src = imread(str(IMAGE))

    logs_dir = LOGS.joinpath(test_fluent_2.__name__)

    with Logger(logs_dir) as logger:
        with FluentNumpy(src, logger, inter_save=False) as src_fluent:
            src_fluent >> (
                rgb2gray
            ) >> (
                canny,
                {
                    'sigma': 3.0
                }
            ) >> (
                morphology.binary_dilation
            )

            assert src_fluent.image.shape == src.shape[:-1]
            assert not np.all(src_fluent.image == 0)


def test_fluent_3():
    src = imread(str(IMAGE))

    with FluentNumpy(src) as src_fluent:
        src_fluent >> (
                rgb2gray
            ) >> (
                canny,
                {
                    'sigma': 3.0
                }
            ) >> (
                morphology.binary_dilation
            )

        assert src_fluent.image.shape == src.shape[:-1]
        assert not np.all(src_fluent.image == 0)
