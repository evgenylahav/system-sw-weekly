"""
this module provides 3 functions for loading an image, calculating its
magnitude of Fourier Transform and present an image
"""
import os
from PIL import Image
import numpy as np
from numpy.fft import fft2, fftshift
import matplotlib.pyplot as plt


def load_image_as_array(filename: str) -> np.ndarray:
    """ load an image an return the array representing it """
    img = Image.open(filename)
    img.load()
    return np.asarray(img, dtype="int32")


def calc_image_fft_magnitude(image_array: np.ndarray) -> np.ndarray:
    """ calc magnitude of Fourier Transform of an input image array """
    return np.abs(fftshift(fft2(image_array)))


def show_image(image: np.ndarray) -> None:
    """ show image on plot """
    plt.imshow(image)
    plt.show()


def main():
    """ main """
    image_name = os.path.abspath(r"../resources/sine_im.jpg")

    image_array = load_image_as_array(image_name)

    image_ft = calc_image_fft_magnitude(image_array)

    show_image(image_ft)


if __name__ == '__main__':
    main()
