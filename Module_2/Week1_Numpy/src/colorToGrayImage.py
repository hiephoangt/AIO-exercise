import matplotlib.image as mping
import numpy as np


def lightness(vector):
    return vector.max()*0.5 + vector.min()*0.5


def compute_avarage(vector):
    return vector.mean()


def luminosity(vector):
    return vector[0]*0.21 + vector[1]*0.72 + vector[2]*0.07


if __name__ == '__main__':
    # Question 12
    img = mping.imread('D:\Github\AIO-exercise\Module_2\Week1_Numpy\data\dog.jpeg')
    gray_img_01 = np.apply_along_axis(lightness, 2, img)
    print(gray_img_01[0][0])

    # Question 13
    gray_img_02 = np.apply_along_axis(compute_avarage, 2, img)
    print(gray_img_02[0][0])

    # Question 14
    gray_img_03 = np.apply_along_axis(luminosity, 2, img)
    print(gray_img_03[0][0])
