from PIL import Image #import library

bear = Image.open( "bear.png" ) #open bear image

print(bear.size) #prints size of image

pixel = bear.getpixel( ( 100, 200) ) #gets pixel RGB at loc 100, 200
print(pixel) # prints pixel RGB

bear.putpixel( (100, 200), (0, 0, 0) ) #edits pixel

#edits line of pixels
for i in range(100):
    bear.putpixel( (i, 200) , (0, 0, 0) )

bear.save("tmp_James.png") # create/overwrite tmp_Name.png with current image

#inverts image
def invert( im ):

    ''' Invert the colors in the input image, im '''
    
    # Find the dimensions of the image
    (width, height) = im.size

    # Loop over the entire image
    for x in range( width ):
        for y in range( height ):
            (red, green, blue) = im.getpixel((x, y))
            bear.putpixel( (x, y), (255-red, 255-green, 255-blue) )


#inverts upper left corner of image

#inverts upper right of image
def invert_block( im ):
    # Find the dimensions of the image
    (width, height) = im.size

    # Loop over the entire image
    for x in range( int(width / 2), width):
        for y in range(int(height / 2)):
            (red, green, blue) = im.getpixel((x, y))
            bear.putpixel( (x, y), (255-red, 255-green, 255-blue) )


invert_block(bear)

bear.save("tmp_James.png") # create/overwrite tmp_Name.png with current image