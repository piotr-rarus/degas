# Degas

Image processing package.

- pipe operator to chain methods from `skimage`/`opencv`
- algorithms
  - dynamic CLAHE
  - white balance

## Chaining methods - FluentImage

### Rationale

This pattern enables us to take some load off Python's internal memory management mechanisms, and make code much more readable.

Let's consider function like this (please keep in mind that images are quite heavy variables):

```py
import cv2
from degas import white_balance


def preprocess(src, scale_factor):

    resized = cv2.resize(
        crop,
        fx=scale_factor,
        fy=scale_factor,
        interpolation=cv2.INTER_LANCZOS4
    )

    wb = white_balance.simple(resized, f=0.001, cut_off=0.01)
    gray = cv2.cvtColor(wb, code=cv2.COLOR_BGR2GRAY)
    blurred = cv2.bilateralFilter(normalized, d=5, sigmaColor=25, sigmaSpace=25)

    return blurred
```

In this function we create 4 objects, each with unique reference label:

- resized
- wb
- gray
- blurred

While the interpreter enters `preprocess` scope, by the end of the function, all of these 4 objects live in memory, because their reference count is 1. Our memory consumption grows linear with each image operation. Considering images that can be even 100MP, this is simply an overkill. How to manage that?

We introduce simple wrapper for an image `FluentImage`, that'll help us chain subsequent methods.

<https://martinfowler.com/bliki/FluentInterface.html>

As we can't simply define new operator for python, we are overloading existing `rshift` operator `>>` (who uses it anyway?). I think it looks cool.

### Example

```python
import cv2
from degas.color import white_balance


def preprocess(src, scale_factor, logger: Logger):
    with FluentImage(src, logger, 'preprocessing') as preprocessed:
        preprocessed >> (
            cv2.resize,
            {
                'dsize': None,
                'fx': scale_factor,
                'fy': scale_factor,
                'interpolation': cv2.INTER_LANCZOS4
            }
        ) >> (
            white_balance.simple,
            {
                'f': 0.001
            }
        ) >> (
            cv2.cvtColor,
            {
                'code': cv2.COLOR_BGR2GRAY
            }
        ) >> (
            cv2.bilateralFilter,
            {
                'd': 5,
                'sigmaColor': 25,
                'sigmaSpace': 25
            }
        )

        return preprocessed.image
```

We simply pass reference to function, and a dictionary that contains all additional parameters.

Code is much more readable now. Image numpy arrays exist only in narrow scopes, meaning they can be marked immediately for memory sweep. It's also much easier now to change pipeline ordering.

## Getting started

Be sure you have `virtualenv` installed on your machine.

```shell
pip install virtualenv
```

Clone this repository to your disk. Then install this package through `pip`.

```shell
cd [directory]
pip install .
```

## How to use

Check up some scripts in `./tests/` folder

## Tests

```shell
cd [project-path]
python -m pytest .\tests\
```
