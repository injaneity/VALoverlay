import cv2 as cv
import numpy as np
import os
from time import time
from wincap import screenCapture
from valobject import valAnalysis

# initialize the WindowCapture class
wincap = screenCapture()
vision = valAnalysis()

loop_time = time()
while(True):

    # get an updated image of the game
    screenshot = wincap.get_screenshot()
    vision.valread(screenshot)

    agent_directory = r'C:\Users\zanec\PycharmProjects\customUI\agent_icons'

    # debug the loop rate
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('Done.')