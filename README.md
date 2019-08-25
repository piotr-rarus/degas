# Degas

Fluent interface for `numpy` arrays. Really comfy for chaining methods from
computer vision packages i.e. `skimage`, `opencv`.

## Getting started

```shell
pip install degas
```

## Chaining methods - FluentImage

### Rationale

This pattern enables us to take some load off Python's internal memory
management mechanisms, and make code much more readable.

Let's consider function like this (please keep in mind that images are quite heavy variables):

```py
from skimage.color import rgb2gray
from skimage.exposure import equalize_adapthist
from skimage.feature import canny
from skimage.transform import rescale


def preprocess(src, scale_factor):

    gray = rgb2gray(src)
    downscaled = rescale(gray, scale_factor)
    equalized = equalize_adapthist(downscaled, clip_limit=0.2)
    edges = canny(equalized, sigma=2.0)

    return edges
```

In this function we create 4 objects, each with unique reference label:

- gray
- downscaled
- equalized

While the interpreter enters `preprocess` scope, by the end of the function, all of these 4 objects live in memory, because their reference count is 1. Our memory consumption grows linear with each image operation. Considering images that can be even over 100MP, this is simply an overkill. How to manage that?

We introduce simple wrapper for an image `FluentImage`, that'll help us chain subsequent methods.

<https://martinfowler.com/bliki/FluentInterface.html>

As we can't simply define new operator for python, we are overloading existing `rshift` operator `>>` (who uses it anyway?). I think it looks cool and resembles pipe `|>` operator from `F#`.

### Example

```py
from degas import FluentImage
from skimage.color import rgb2gray
from skimage.exposure import equalize_adapthist
from skimage.feature import canny
from skimage.transform import rescale


def preprocess(src, scale_factor):
    with FluentImage(src) as thresh:
        preprocessed >> (
            rgb2gray
        ) >> (
            rescale,
            {
                'scale_factor': scale_factor
            }
        ) >> (
            equalize_adapthist,
            {
                'clip_limit': 0.2
            }
        ) >> (
            canny,
            {
                'sigma': 2.0
            }
        )

    return preprocessed
```

We simply pass reference to function, and a dictionary that contains all additional parameters.

Code is much more readable now. `numpy` arrays exist only in narrow scopes, meaning they can be marked immediately for memory sweep. It's also much easier now to change pipeline ordering.
