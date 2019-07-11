import numpy as np
import math
from skimage import exposure


def dclahe(src, kernel=None, max_clip_limit=0.03):
    """
    Calculates clip limit, used to drive CLAHE.
    Uses simple heuristic based on histogram's mean and variance,
    to determine how strong CLAHE should be applied.
    Aims to lower variance and bias in luminosity, across data.

    Parameters
    ----------
    src : nd.array
        source image
    max_clip_limit : float
        threshold for maximum clip limit

    Returns
    -------
    nd.array
        Source image with applied DCLAHE.
    """

    hist, bins = exposure.histogram(src)
    mean = np.average(bins, weights=hist)

    variance = np.average(
        (bins - mean)**2,
        weights=hist
    )

    std = math.sqrt(variance)

    clip_limit = (1 - mean / bins.max()) * max_clip_limit
    clip_limit += (std / bins.max()) * max_clip_limit
    clip_limit /= 2

    return exposure.equalize_adapthist(src, kernel, clip_limit)
