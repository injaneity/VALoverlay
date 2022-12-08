import cv2 as cv
import numpy as np

def adjust_gamma(image, gamma=1.0):
	# build a lookup table mapping the pixel values [0, 255] to
	# their adjusted gamma values
	invGamma = 1.0 / gamma
	table = np.array([((i / 255.0) ** invGamma) * 255
		for i in np.arange(0, 256)]).astype("uint8")
	# apply gamma correction using the lookup table
	return cv.LUT(image, table)

class ObjVision:

    def __init__(self):
        self = self

    def findObjects(self, needle, haystack, threshold):

        needle = needle[..., :3]
        needle = np.ascontiguousarray(needle)
        #needle[np.where((needle==[0,0,0]).all(axis=2))] = [155,155,155]

        haystack = haystack[..., :3]
        haystack = np.ascontiguousarray(haystack)
        haystack = adjust_gamma(haystack, gamma=1.6)

        #print an array of values
        result = cv.matchTemplate(haystack, needle, cv.TM_SQDIFF_NORMED)

        #np helps to locate relevant results
        locations = np.where(result <= threshold)
        locations = list(zip(*locations[::-1]))
        if locations:
            return True
