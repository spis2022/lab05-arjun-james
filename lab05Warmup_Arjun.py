from PIL import Image  # imports image manipulation library

bear = Image.open("bear.png")  # opens the bear image

print(bear.size)  # prints size of the bear image

pixel = bear.getpixel((100, 200))
print(pixel)  # prints the pixel values at 100, 200

bear.putpixel((100, 200), (0, 0, 0))  # edits the pixel at 100, 200

# modify a horizontal line of pixels
for i in range(100):
    bear.putpixel((i, 200), (0, 0, 0))


def invert(im):
    ''' Invert the colors in the input image, im '''

    # Find the dimensions of the image

    (width, height) = im.size

    # Loop over the entire image
    for x in range(width):
        for y in range(height):
            (red, green, blue) = im.getpixel((x, y))

            im.putpixel((x, y), (255 - red, 255 - green, 255 - blue))
            # Complete this function by adding your lines of code here.

            # You need to calculate the new pixel values and then to change them

            # in the image using putpixel()


def invert_block(im):
    ''' Invert the colors in the top right 25% of the input image, im '''

    # Find the dimensions of the image

    (width, height) = im.size

    # Loop over the entire image
    for x in range(int(width/2), width):
        for y in range(int(height/2)):
            (red, green, blue) = im.getpixel((x, y))

            im.putpixel((x, y), (255 - red, 255 - green, 255 - blue))
            


invert(bear)
invert_block(bear)
bear.save("tmp_Arjun.png")  # create/overwrite tmp_Arjun.png with current image
