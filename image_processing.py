from cv2 import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image, ImageEnhance
from py4j.java_gateway import JavaGateway, CallbackServerParameters

class ImageProcessing():
    # def __init__(self, gateway):
    #     self.gateway = gateway

    # class Java:
    #     implements = ["PACKAGE.INTERFEJS"]

    def histograms(self):
        img = cv2.imread('abc.jpg')
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img_lum = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
        histr = cv2.calcHist([img_rgb],[0],None,[256],[0,256])
        histg = cv2.calcHist([img_rgb],[1],None,[256],[0,256])
        histb = cv2.calcHist([img_rgb],[2],None,[256],[0,256])
        histl = cv2.calcHist([img_lum],[0],None,[256],[0,256])

        plt.xlabel("Pixel value")
        plt.ylabel("Number of pixels")
        plt.plot(histr, color="r", label="Red")
        plt.savefig("swap/red.jpg")
        plt.clf()
        plt.plot(histg, color="g", label="Green")
        plt.savefig("swap/green.jpg")
        plt.clf()
        plt.plot(histb, color="b", label="Blue")
        plt.savefig("swap/blue.jpg")
        plt.clf()
        plt.plot(histl, color="grey", label="Lumi")
        plt.savefig("swap/lum.jpg")
        plt.clf()
    

    def contrast(self, contrast):
        img = Image.open('swap/image.jpg')
        cont = ImageEnhance.Contrast(img)
        img = cont.enhance(contrast)
        img.save('swap/test.jpg')


    def brightness(self, brightness):
        img = Image.open('swap/image.jpg')
        bright = ImageEnhance.Brightness(img)
        img = bright.enhance(brightness)
        img.save('swap/test.jpg')

    def saturation(self, saturation):
        img = Image.open('swap/image.jpg')
        sat = ImageEnhance.Color(img)
        img = sat.enhance(saturation)
        img.save('swap/test.jpg')

if __name__ == "__main__":
    # gateway = JavaGateway(
    #     callback_server_parameters=CallbackServerParameters()
    # )
    processor = ImageProcessing()
    processor.saturation(0.5)
    #gateway.entry_point.setProcessor(processor)



