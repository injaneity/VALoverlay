# Import required packages
import cv2 as cv
import numpy as np
import pytesseract as pyt

# Mention the installed location of Tesseract-OCR in your system
full_img = cv.imread(r'C:\Users\zanec\PycharmProjects\customUI\test_images\test_feed_3.png')
#must be individually changed for each scoreboard chunk
bar1 = full_img[30:71, 431:768]
bar2 = full_img[30:71, 1149:1449]
P1 = full_img[339:374, 572:1348]
P2 = full_img[374:407, 572:1348]
P3 = full_img[407:440, 572:1348]
P4 = full_img[440:473, 572:1348]
P5 = full_img[473:507, 572:1348]
P6 = full_img[570:603, 572:1348]
P7 = full_img[604:637, 572:1348]
P8 = full_img[637:670, 572:1348]
P9 = full_img[672:705, 572:1348]
P10 = full_img[705:738, 572:1348]

list = [P1,P2]

for x in list:
#can stay the same
#username
    agent1 = x[0:375, 0:72]
    user1 = x[0:375, 72:241]
    ultimate1 = x[0:375, 241:362]
    KDA1 = x[0:375, 362:482]
    gun1 = x[0:375, 482:600]
    armor1 = x[0:375, 600:636]
    creds1 = x[0:375, 636:726]
    #cv.imshow('SOURCE', user1)
   # cv.waitKey(5000)

KDA1 = P1[0:375, 362:482]

pyt.pytesseract.tesseract_cmd = r'C:\Users\zanec\AppData\Local\Tesseract-OCR\tesseract.exe'

def textr(input):
    #img = cv.imread(r'C:\Users\zanec\PycharmProjects\customUI\test_images\test_scoreboard_cut13.png')
    img = np.ascontiguousarray(input)
    img = cv.resize(img, None, fx=1.5, fy=1.5, interpolation=cv.INTER_CUBIC)
    gry = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    text = pyt.image_to_string(gry, config="--psm 6")
    return text