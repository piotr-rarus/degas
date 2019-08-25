import numpy as np
from austen import Logger
from skimage import morphology
from skimage.color import rgb2gray
from skimage.feature import canny

from degas import FluentImage


def test_smoke(coffee: np.ndarray):

    with FluentImage(coffee) as coffee_fluent:

        assert np.array_equal(coffee_fluent.image, coffee)

        coffee_fluent >> (
                rgb2gray
            ) >> (
                canny,
                {
                    'sigma': 3.0
                }
            ) >> (
                morphology.binary_dilation
            )

        assert coffee_fluent.image.shape == coffee.shape[:-1]
        assert not np.all(coffee_fluent.image == 0)


def test_inter_save(coffee: np.ndarray, logger: Logger):

    with FluentImage(coffee, logger) as coffee_fluent:

        coffee_fluent >> (
            rgb2gray
        ) >> (
            canny,
            {
                'sigma': 3.0
            }
        ) >> (
            morphology.binary_dilation
        )

        files = tuple(logger.OUTPUT.iterdir())
        assert len(files) == 4


def test_wo_inter_save(coffee: np.ndarray, logger: Logger):

    with FluentImage(coffee, logger, inter_save=False) as coffee_fluent:

        coffee_fluent >> (
            rgb2gray
        ) >> (
            canny,
            {
                'sigma': 3.0
            }
        ) >> (
            morphology.binary_dilation
        )

        files = tuple(logger.OUTPUT.iterdir())
        assert len(files) == 0
