from PIL import Image, ImageDraw


def createGif():
    images = []
    width = 200
    center = width // 2
    firstColor = (0, 255, 0)
    secondColor = (255, 0, 0)
    maxRadius = int(center * 1.5)
    step = 8

    for i in range(0, maxRadius, step):
        im = Image.new("RGB", (width, width), secondColor)
        draw = ImageDraw.Draw(im)
        draw.ellipse((center - i, center - i, center + i, center + i), fill=firstColor)
        images.append(im)
        images[0].save('pillow_image_draw.gif',
                       save_all=True, append_images=images[1:],
                       optimize=False, duration=10)
