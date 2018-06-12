# The pixels in an input image are represented as integers.
# This algorithm distorts the input image in the following way:
# Every pixel x in the output image has a value equal to the average
# value of the pixel values from the 3 × 3 square that has its center at x,
# including x itself. All the pixels on the border of x are then removed.

# Return the blurred image as an integer, with the fractions rounded down.

import math
def boxBlur(image):
    results = []
    for i in range(len(image) - 2):
        results_row = []
        for pixels in range(len(image[0]) - 2):
            # get average of this 3 x 3 square
            sum = 0
            # first row
            for thisPixels in range(3):
                sum += image[i][pixels + thisPixels]
            # middle row
            for thisPixels in range(3):
                sum += image[i+1][pixels + thisPixels]
            # bottom row
            for thisPixels in range(3):
                sum += image[i+2][pixels + thisPixels]
            results_row.append(math.floor(sum/9))
        results.append(results_row)
    return results
