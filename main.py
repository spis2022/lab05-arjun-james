#print("Running lab05Warmup_Arjun.py")
#import lab05Warmup_Arjun

#print("Running lab05Warmup_James.py")
#import lab05Warmup_James

#Turn image to grayscale

from PIL import Image  # imports image manipulation library
import random # imports random library for list manipulation

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
    
def scale(im):
    ''' flip the image vertically'''

    # Find the dimensions of the image
    (width, height) = im.size
    im2 = Image.new('RGB', (width//2, height//2))
    # Loop over the entire image
    for x in range(0, width, 2):
        for y in range(0, height, 2):
            (red, green, blue) = im.getpixel((x, y))
        
            im2.putpixel((x//2, y//2), (red, green, blue))
    return im2
    
def blur(im):
    (width, height) = im.size
    im2 = Image.new('RGB', (width - 2, height - 2))
    # Loop over the entire image
    for x in range(1, width - 1):
        for y in range(1, height - 1):
            colors = [0, 0, 0]
            for i in range(x - 1, x + 2):
                for j in range(y - 1, y + 2):
                    (red, green, blue) = im.getpixel((i, j))
                    colors[0] += red
                    colors[1] += green
                    colors[2] += blue
            colors = tuple([i//9 for i in colors])
            im2.putpixel((x - 1, y - 1), colors)
    return im2

def randomGrid(im):
    (width, height) = im.size
    im2 = Image.new('RGB', (width, height))
    rand_list = [[(i, j) for i in range(0, width, width//4)] for j in range(0, height, height//4)]
    temp_list = []
    for i in rand_list:
        temp_list.extend(i)
    rand_list = temp_list.copy()
    random.shuffle(rand_list)
    print(temp_list)
    print(rand_list)
    for i in range(len(temp_list)):
        new_list = [[(i, j) for i in range(temp_list[i][0], temp_list[i][0] + width//4)] for j in range(temp_list[i][1], temp_list[i][1] + height//4)]
        old_list = [[(i, j) for i in range(rand_list[i][0], rand_list[i][0] + width//4)] for j in range(rand_list[i][1], rand_list[i][1] + height//4)]
        for k in range(len(new_list)):
            for l in range(len(new_list[k])):
                im2.putpixel(new_list[k][l], im.getpixel(old_list[k][l]))
    return im2
#flipVert(bear)           
#mirrorHoriz(bear)
#mirrorVert(bear)    
#binarize(bear, 100, 0, 0, 600, 800)
#grayscale(bear)

randomGrid(bear).save("tmp_Lab.png")
#blur(bear).save("tmp_Lab.png")
#scale(bear).save("tmp_Lab.png")

#bear.save("tmp_Lab.png") # create/overwrite tmp_Lab.png with current image

