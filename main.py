#print("Running lab05Warmup_Arjun.py")
#import lab05Warmup_Arjun

#print("Running lab05Warmup_James.py")
#import lab05Warmup_James

#Turn image to grayscale

from PIL import Image  # imports image manipulation library

bear = Image.open("bear.png")  # opens the bear image

def grayscale(im):
    ''' grayscale the colors in the input image, im '''

    # Find the dimensions of the image

    (width, height) = im.size

    # Loop over the entire image
    for x in range(width):
        for y in range(height):
            (red, green, blue) = im.getpixel((x, y))

            grayscale_value = int(.21*red + .72*green + .07*blue)
            
            im.putpixel((x, y), (grayscale_value, grayscale_value, grayscale_value))



def binarize(im, thresh, startx, starty, endx, endy):
    
    ''' binarize the colors in the input image, im '''

    # Find the dimensions of the image

    (width, height) = im.size

    # Loop over the entire image
    for x in range(startx, endx):
        for y in range(starty, endy):
            (red, green, blue) = im.getpixel((x, y))

            luminance = int(.21*red + .72*green + .07*blue)

            if luminance > thresh:        
                im.putpixel((x, y), (255, 255, 255))
            else:
                im.putpixel((x, y), (0, 0, 0))


def mirrorVert(im):
    ''' mirror the vertical dimension of the image '''

    # Find the dimensions of the image
    (width, height) = im.size

    # Loop over the entire image
    for x in range(width):
        for y in range(height//2):
            (red, green, blue) = im.getpixel((x, y))

            im.putpixel((x, height-y-1), (red, green, blue))

def mirrorHoriz(im):
    ''' mirror the horizontal dimension of the image '''

    # Find the dimensions of the image
    (width, height) = im.size

    # Loop over the entire image
    for x in range(width//2):
        for y in range(height):
            (red, green, blue) = im.getpixel((x, y))
        
            im.putpixel((width-x-1, y), (red, green, blue))


def flipVert(im):
    ''' flip the image vertically'''

    # Find the dimensions of the image
    (width, height) = im.size

    # Loop over the entire image
    for x in range(width):
        for y in range(height//2):
            (red, green, blue) = im.getpixel((x, y))
            (red2, green2, blue2) = im.getpixel((x, height-y-1))
        
            im.putpixel((x, y), (red2, green2, blue2))
            im.putpixel((x, height-y-1), (red, green, blue))
    
            
            
flipVert(bear)           
#mirrorHoriz(bear)
#mirrorVert(bear)    
#binarize(bear, 100, 0, 0, 600, 800)
#grayscale(bear)
bear.save("tmp_Lab.png") # create/overwrite tmp_Lab.png with current image

