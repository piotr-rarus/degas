import numpy as np
from skimage.exposure import rescale_intensity


def simple(src, f, cut_off=0.0):
    """
    Performs white balance on an image.

    Parameters
    ----------
    src : nd.array
        source image
    f : float
        factor of balance intensity
    cut_off : float, optional
        factor of black and white cut off,
        when you have many black/white pixels, this can help to omit them
        during balancing (the default is 0.0, which turns it off)

    Returns
    -------
    nd.array
        Image with color balance applied.
    """

    f /= 2.0
    wb = []
    for channel in np.dsplit(src, src.shape[-1]):
        channel_sorted = np.sort(channel.flatten())

        r = channel_sorted[-1] - channel_sorted[0]
        l_cut_off = int(r * cut_off)
        h_cut_off = channel_sorted[-1] - int(r * cut_off)

        channel_sorted = channel_sorted[np.where(channel_sorted > l_cut_off)]
        channel_sorted = channel_sorted[np.where(channel_sorted < h_cut_off)]

        low = channel_sorted[int(len(channel_sorted) * f)]
        high = channel_sorted[int(len(channel_sorted) * (1 - f))]

        channel[channel < low] = low
        channel[channel > high] = high
        channel = rescale_intensity(channel)
        wb.append(channel)

    return np.dstack(wb).astype(src.dtype)
