#imports numpy for arrays and pillow for image reading and writing
import numpy as np
from PIL import Image
#function converts input file to output file in greyscale
def Greyscale(input_file,output_file):
#   opens user_input image with pillow. creates array with numpy
    array = Image.open(input_file)
    array = np.array(array)
#   checks the height and width
    height, width, rbg = np.shape(array)
#    uses nested loop to convert each pixel to rgb one row at a time
    for i in range(0,height):
        for j in range(0,width):
            array[i][j] = 0.21 * array[i][j][0] + 0.72 * array[i][j][1] + 0.07 * array[i][j][2]
#   checks where to send output file to
    greyscale_output_file = output_file
#   saves output file
    img = Image.fromarray(array, 'RGB')
    img.save(greyscale_output_file)