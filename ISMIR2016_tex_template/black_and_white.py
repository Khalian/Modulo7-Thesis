from PIL import Image
import sys

if (len(sys.argv) < 3):
    print "Usage : python black_and_white.py inputFile outputFile"
    sys.exit(0)
 
image_file = Image.open(sys.argv[1]) # open colour image
image_file = image_file.convert('1') # convert image to black and white
image_file.save(sys.argv[2])

