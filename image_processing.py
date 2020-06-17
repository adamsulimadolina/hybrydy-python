from cv2 import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image, ImageEnhance

def histograms():
    img = cv2.imread('xd2.jpg')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    histr = cv2.calcHist([img],[0],None,[256],[0,256])
    histg = cv2.calcHist([img],[1],None,[256],[0,256])
    histb = cv2.calcHist([img],[2],None,[256],[0,256])
    r,g,b = cv2.split(img)
    
    lum = 0.2126 * r + 0.7152 * b + 0.0722 * g
    lum = lum.astype(int)
    print(type(lum))
    histl = cv2.calcHist([lum],[0],None,[256],[0,256])

    file_red = open("red.bin", "wb")
    file_green = open("green.bin", "wb")
    file_blue = open("blue.bin", "wb")
    file_lum = open("lum.bin", "wb")

    np.ndarray.tofile(file_red, histr)
    np.ndarray.tofile(file_green, histg)
    np.ndarray.tofile(file_blue, histb)
    np.ndarray.tofile(file_lum, histl)

def contrast(contrast):
    img = cv2.imread('aaa.png')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    tmp_image = Image.fromarray(img)
    cont = ImageEnhance.Contrast(tmp_image)
    img = cont.enhance(contrast)
    img = np.array(img)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    cv2.imwrite('xd2.jpg', img)
    # if contrast != 0:
    #     f = 131*(contrast + 127)/(127*(131-contrast))
    #     alpha_c = f
    #     gamma_c = 127*(1-f)

    # img = cv2.addWeighted(img, alpha_c, img, 0, gamma_c)
    # cv2.imwrite('copy.jpg', img)


def brightness(brightness):
    img = cv2.imread('abc.jpg')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    tmp_image = Image.fromarray(img)
    bright = ImageEnhance.Brightness(tmp_image)
    img = bright.enhance(brightness)
    img = np.array(img)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    cv2.imwrite('xd3.jpg', img)

def saturation(saturation):
    img = cv2.imread('aaa.png')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    tmp_image = Image.fromarray(img)
    sat = ImageEnhance.Color(tmp_image)
    img = sat.enhance(saturation)
    img = np.array(img)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    cv2.imwrite('xd.jpg', img)

if __name__ == "__main__":
    contrast(3)
    brightness(0.7)
    saturation(2)
    histograms()



