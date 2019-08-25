from pathlib import Path
from shutil import rmtree
from typing import Generator

from austen import Logger
from numpy import ndarray
from pytest import fixture
from skimage.io import imread

__LOGS_DIR = Path('logs')
__COFFEE_PNG_PATH = Path('degas/test/coffee.png')


def __reset_dir(path: Path):
    if path.is_dir:
        rmtree(str(path), ignore_errors=True)


@fixture()
def logger() -> Generator[Logger, None, None]:
    yield Logger(__LOGS_DIR, clear_dir=True)

    __reset_dir(__LOGS_DIR)


@fixture(scope='session')
def coffee() -> ndarray:
    coffee = imread(__COFFEE_PNG_PATH)
    return coffee
