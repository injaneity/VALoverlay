import numpy as np
import os
import json
import pytesseract as pyt
import cv2 as cv
from vision import ObjVision

pyt.pytesseract.tesseract_cmd = r'C:\Users\zanec\AppData\Local\Tesseract-OCR\tesseract.exe'

def text_read(text_input):
    img = np.ascontiguousarray(text_input)
    img = cv.resize(img, None, fx=1.75, fy=1.75, interpolation=cv.INTER_CUBIC)
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    text = pyt.image_to_string(img, config="--psm 6")
    return text

class valCapture:

    def __init__(self):
        self.agent = ''
        self.is_alive = True
        self.username = ''

class valAnalysis:

    def valread(img):

        vision = ObjVision()
        agent_directory = r'C:\Users\zanec\PycharmProjects\customUI\agent_icons'

        #\\\1\\\ opens json to write objects
        with open('C:\\Users\\zanec\\PycharmProjects\\customUI\\data.json', 'w') as file:

            #\\\2\\\ iterating through scoreboard
            #where list contains cropped images
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

            list = [P1, P2, P3, P4, P5, P6, P7, P8, P9, P10]

            j = 0

            for i in list:

                x = 0
                j += 1
                print(j)

                ValObject = valCapture()
                while ValObject.agent == '':
                    print(x)
                    x += 0.05
                    for filename in os.listdir(agent_directory):

                        f = os.path.join(agent_directory, filename)
                        # checking if it is a file
                        if os.path.isfile(f):

                            # turn image into readable input
                            agent = i[0:375, 0:42]
                            agent_input = cv.imread(f, cv.IMREAD_UNCHANGED)
                            agent_input = agent_input[..., :3]
                            agent_input[np.where((agent_input == [0, 0, 0]).all(axis=2))] = [175, 175, 175]

                            # run matchtemplate
                            # if display returns true
                            if vision.findObjects(agent_input, agent, x):

                                print('found the gamer')
                                # need to rename files to viper.png etc.
                                # assigns filename to agent attribute
                                agent_name = filename.split(".")[0]
                                ValObject.agent = str(agent_name)
                                print(ValObject.agent)

                                # \\\5\\\ check for is_alive
                                # resizes original agent image to fit top bar
                                bar = cv.resize(agent_input, None, fx=1.21875, fy=1.21875, interpolation=cv.INTER_CUBIC)

                                # figuring out which side to choose
                                if j <= 5:
                                    bar_side = bar_l
                                    print('left side')
                                elif j >= 6:
                                    bar_side = bar_r
                                    bar = cv.flip(bar, 1)

                                else:
                                    print('error weird number')

                                if vision.findObjects(bar, bar_side, 0.35):
                                    ValObject.is_alive = True
                                    print("alive")
                                else:
                                    ValObject.is_alive = False
                                    print("dead")

                                # \\\6\\\ text detection part 1: username
                                username = i[0:375, 72:241]
                                ValObject.username = text_read(username)
                                json_export = json.dumps(ValObject.__dict__)

                if ValObject.agent == '':
                    print('missing')

                else:
                    file.write(json_export)




image = cv.imread(r'C:\Users\zanec\PycharmProjects\customUI\test_images\test_feed_4.png')
valAnalysis.valread(image)

