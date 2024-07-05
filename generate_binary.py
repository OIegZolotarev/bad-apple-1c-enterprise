import os
from PIL import Image


frames = os.listdir("./compressed")

for file in frames:

    fileName = ("./compressed/" + file)
    print("Parsing frame {0} of {1}".format(frames.index(file), len(frames)))

    with Image.open(fileName).convert('L') as im:

        frameNumber = file.split(".")[0]
        outFrame = open("./binary/{0}".format(frameNumber), "wt")

        for x in range(0,im.width):
            for y in range(0,im.height):
                
                pixel = im.getpixel((x,y))
                
                outFrame.write("{0},".format(pixel))

        outFrame.close()                
                
