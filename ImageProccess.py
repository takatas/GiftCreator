from PIL import Image

def openImage():
    im = Image.open("image.png ")
    im.show()
    print(im.format, im.size, im.mode)

def rotateImage():
    im = Image.open("image.png ")
    im.rotate(90).show()
    print(im.format, im.size, im.mode)