import cv2 as cv
import numpy as np
from vision import ObjVision

def adjust_gamma(image, gamma=1.0):
	# build a lookup table mapping the pixel values [0, 255] to
	# their adjusted gamma values
	invGamma = 1.0 / gamma
	table = np.array([((i / 255.0) ** invGamma) * 255
		for i in np.arange(0, 256)]).astype("uint8")
	# apply gamma correction using the lookup table
	return cv.LUT(image, table)

needle = cv.imread(r'C:\Users\zanec\PycharmProjects\customUI\armor_icons\full.png')
needle = needle[...,:3]
needle = np.ascontiguousarray(needle)
needle[np.where((needle==[0,0,0]).all(axis=2))] = [155,155,155]


bar = cv.resize(needle, None, fx=1.226, fy=1.226, interpolation=cv.INTER_CUBIC)

img = cv.imread(r'C:\Users\zanec\PycharmProjects\customUI\test_images\test_feed_4.png')

bar_l = img[30:71, 430:768]
bar_r = img[30:71, 1149:1449]

P1 = img[339:374, 572:1348]
P2 = img[374:407, 572:1348]
P3 = img[407:440, 572:1348]
P4 = img[440:473, 572:1348]
P5 = img[473:507, 572:1348]
P6 = img[570:603, 572:1348]
P7 = img[604:637, 572:1348]
P8 = img[637:670, 572:1348]
P9 = img[672:705, 572:1348]
P10 = img[705:738, 572:1348]

haystack = P5
haystack = haystack[...,:3]
haystack = np.ascontiguousarray(haystack)
haystack = adjust_gamma(haystack, gamma=1.75)
img = haystack[0:375, 0:42]

#haystack[:,:,2] += 0



cv.imshow('huh', haystack)
cv.waitKey(3000)

result = cv.matchTemplate(haystack, needle, cv.TM_SQDIFF_NORMED)

threshold = 0.1

# The np.where() return value will look like this:
# (array([482, 483, 483, 483, 484], dtype=int32), array([514, 513, 514, 515, 514], dtype=int32))
locations = np.where(result <= threshold)
# We can zip those up into a list of (x, y) position tuples
locations = list(zip(*locations[::-1]))
print(locations)

rectangles = []

if locations:
    print('Found needle.')

    needle_w = needle.shape[1]
    needle_h = needle.shape[0]
    line_color = (0, 255, 0)
    line_type = cv.LINE_4

    # Loop over all the locations and draw their rectangle
    for loc in locations:
        # Determine the box positions
        top_left = loc
        bottom_right = (top_left[0] + needle_w, top_left[1] + needle_h)
        # Draw the box
        cv.rectangle(haystack, top_left, bottom_right, line_color, line_type)

    cv.imshow('Matches', haystack)
    cv.waitKey(5000)
    #cv.imwrite('result.jpg', haystack_img)

else:
    print('Needle not found.')


