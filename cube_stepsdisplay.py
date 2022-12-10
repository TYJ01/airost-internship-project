import cv2 as cv
import numpy as np
import time


def getcontuor(blurimg,img, imgContours,step):
    img1 = img.copy()
    #imggray = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
    #thresh = cv.threshold(imggray, 100,255, cv.THRESH_BINARY)
    contours, hierarchy = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    #cv.drawContours(imgContours, contours, -1, (255,0,0), 4)
    for cvt in contours:
        area = cv.contourArea(cvt)
        if area > 10000:
            cv.drawContours(imgContours, cvt, -1, (255,0,0), 4)
            peri = cv.arcLength(cvt, True)
            approx = cv.approxPolyDP(cvt, 0.02*peri, True)
            if len(approx) == 4:
            #print(len(approx))
                x_, y_, w, h=cv.boundingRect(approx)
                cv.rectangle(imgContours,(x_, y_),(x_+w,y_+h),(0,255,0), 3)
                cv.putText(imgContours, "Rubik's Cube", (x_+w+10,y_+h+10), cv.FONT_HERSHEY_COMPLEX, 0.7, (0,255,0),1)


def getcontuor1(blurimg,img, imgContours,step,i):
    img1 = img.copy()
    #imggray = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
    #thresh = cv.threshold(imggray, 100,255, cv.THRESH_BINARY)
    contours, hierarchy = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    #cv.drawContours(imgContours, contours, -1, (255,0,0), 4)
    for cvt in contours:
        area = cv.contourArea(cvt)
        if area > 10000:
            cv.drawContours(imgContours, cvt, -1, (255,0,0), 4)
            peri = cv.arcLength(cvt, True)
            approx = cv.approxPolyDP(cvt, 0.02*peri, True)
            if len(approx) == 4:
            #print(len(approx))
                x_, y_, w, h=cv.boundingRect(approx)
                cv.rectangle(imgContours,(x_, y_),(x_+w,y_+h),(0,255,0), 3)
                cv.putText(imgContours, "Rubik's Cube", (x_+w+10,y_+h+10), cv.FONT_HERSHEY_COMPLEX, 0.7, (0,255,0),1)
                text = "step : " + str(i)
                cv.putText(imgContours, text, (x_ + w + 10, y_ + h - 20), cv.FONT_HERSHEY_COMPLEX,
                       0.7, (0, 255, 0), 1)
                step_counter(step,imgContours, x_, y_, w, h)

def getcontuor2(blurimg,img, imgContours,step):
    img1 = img.copy()
    #imggray = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
    #thresh = cv.threshold(imggray, 100,255, cv.THRESH_BINARY)
    contours, hierarchy = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    #cv.drawContours(imgContours, contours, -1, (255,0,0), 4)
    for cvt in contours:
        area = cv.contourArea(cvt)
        if area > 10000:
            cv.drawContours(imgContours, cvt, -1, (255,0,0), 4)
            peri = cv.arcLength(cvt, True)
            approx = cv.approxPolyDP(cvt, 0.02*peri, True)
            if len(approx) == 4:
            #print(len(approx))
                x_, y_, w, h=cv.boundingRect(approx)
                cv.rectangle(imgContours,(x_, y_),(x_+w,y_+h),(0,255,0), 3)
                cv.putText(imgContours, "Rubik's Cube", (x_+w+10,y_+h+10), cv.FONT_HERSHEY_COMPLEX, 0.7, (0,255,0),1)
                step_counter(step,imgContours, x_, y_, w, h)





def step_counter(step,imgContours, x_, y_, w, h):
        if step == 'F' :
            cv.arrowedLine(imgContours, (x_ + 50, y_ + 50),
                           (x_ + int((2 * w) / 3 + 30), y_ + 50), (0, 255, 0), 3)
            cv.arrowedLine(imgContours, (int(x_ + ((2 * w) / 3) + 50), y_ + 50),
                           (int(x_ + ((2 * w) / 3) + 50), int(y_ + ((2 * h) / 3) + 30)), (0, 255, 0), 3)
            cv.arrowedLine(imgContours, (int(x_ + (2 * w) / 3 + 50), int(y_ + (2 * h) / 3 + 50)),
                           (x_ + 80, int(y_ + (2 * h) / 3 + 50)), (0, 255, 0), 3)
            cv.arrowedLine(imgContours, (x_ + 50, int(y_ + (2 * h) / 3 + 50)),
                           (x_ + 50, y_ + 80), (0, 255, 0), 3)
        if step == "F'" :
            cv.arrowedLine(imgContours, (int(x_ + (2 * w) / 3 + 50), y_ + 50),
                           (x_ + 80, y_ + 50), (0, 255, 0), 3)
            cv.arrowedLine(imgContours, (x_ + 50, y_+50), (x_ + 50, int(y_ + (2 * h) / 3 + 30)), (0,255,0), 3)
            cv.arrowedLine(imgContours, (x_ + 50, int(y_ + (2 * h) / 3 + 50)),
                       (int(x_ + (2 * w) / 3 + 30), int(y_ + (2 * h) / 3 + 50)), (0, 255, 0), 3)
            cv.arrowedLine(imgContours, (int(x_ + ((2 * w) / 3) + 50), int(y_ + ((2 * h) / 3) + 50)), (int(x_ + ((2 * w) / 3) + 50), y_+30), (0,255,0), 3)
        if step == 'R' :
            cv.arrowedLine(imgContours, (int(x_ + ((2 * w) / 3) + 50), int(y_ + ((2 * h) / 3) + 50)), (int(x_ + ((2 * w) / 3) + 50), y_+50), (0,255,0), 3)
        if step == "R'" :
            cv.arrowedLine(imgContours, (int(x_ + ((2 * w) / 3) + 50), y_+50), (int(x_ + ((2 * w) / 3) + 50), int(y_ + ((2 * h) / 3) + 50)), (0,255,0), 3)
        if step == 'B' :
            cv.arrowedLine(imgContours, (int(x_ + ((2 * w) / 3) + 50), int(y_ + ((2 * h) / 3) + 50)),
                           (int(x_ + ((2 * w) / 3) + 50), y_ + 50), (0, 255, 0), 3)
        if step == "B'" :
            cv.arrowedLine(imgContours, (int(x_ + ((2 * w) / 3) + 50), y_ + 50),
                           (int(x_ + ((2 * w) / 3) + 50), int(y_ + ((2 * h) / 3) + 50)), (0, 255, 0), 3)
        if step == 'L' :
            cv.arrowedLine(imgContours, (x_ + 50, y_+50), (x_ + 50, int(y_ + (2 * h) / 3 + 50)), (0,255,0), 3)
        if step == "L'" :
            cv.arrowedLine(imgContours, (x_  + 50, int(y_ + (2 * h) / 3 + 50)),
                           (x_ + 50, y_ + 50), (0,255,0), 3)
        if step == 'U' :
            cv.arrowedLine(imgContours, (int(x_ + (2 * w) / 3+ 50), y_  + 50),
                           (x_ + 50, y_ + 50), (0,255,0), 3)
        if step == "U'" :
            cv.arrowedLine(imgContours, (x_ + 50, y_ + 50),
                           (x_ + int((2 * w) / 3+ 50), y_  + 50), (0,255,0), 3)
        if step == 'D' :
            cv.arrowedLine(imgContours, (x_ + 50, int(y_+ (2 * h) / 3 + 50)),
                           (int(x_ + (2 * w) / 3 + 50), int(y_+ (2 * h) / 3 + 50)), (0,255,0), 3)
        if step == "D'" :
            cv.arrowedLine(imgContours, (int(x_ + (2 * w) / 3 + 50), int(y_+ (2 * h) / 3 + 50)),
                           (x_ + 50, int(y_+ (2 * h) / 3 + 50)), (0,255,0), 3)
        if step == "SL":
            cv.arrowedLine(imgContours, (x_ + 50, y_ + 50),
                           (x_ + int((2 * w) / 3 + 50), y_ + 50), (0, 255, 0), 3)
            cv.arrowedLine(imgContours, (x_ + 50, y_+int((h) / 3) + 50),
                           (x_ + int((2 * w) / 3+ 50), y_ +int((h) / 3) + 50), (0,255,0), 3)
            cv.arrowedLine(imgContours, (x_ + 50, y_+ int((2*h)/3) + 50),
                           (x_ + int((2 * w) / 3+ 50), y_+ int((2*h)/3)  + 50), (0,255,0), 3)
        if step == "SR":
            cv.arrowedLine(imgContours, (x_ + int((2 * w) / 3 + 50), y_ + 50),
                           (x_ + 50, y_ + 50), (0, 255, 0), 3)
            cv.arrowedLine(imgContours, (x_ + int((2 * w) / 3+ 50), y_ +int((h) / 3) + 50),
                           (x_ + 50, y_+int((h) / 3) + 50), (0, 255, 0), 3)
            cv.arrowedLine(imgContours, (x_ + int((2 * w) / 3+ 50), y_+ int((2*h)/3)  + 50),
                           (x_ + 50, y_+ int((2*h)/3) + 50), (0, 255, 0), 3)



def steps_converter(raw_solution):
    set = str.split(raw_solution)
    for step in set:
        if step == "F2":
            i =set.index(step)
            set = set[:i] + ["F", "F"] + set[i+1:]
        if step == "U2":
            i =set.index(step)
            set = set[:i] + ["U", "U"] + set[i+1:]
        if step == "R2":
            i =set.index(step)
            set = set[:i] + ["R", "R"] + set[i+1:]
        if step == "L2":
            i =set.index(step)
            set = set[:i] + ["L", "L"] + set[i+1:]
        if step == "D2":
            i = set.index(step)
            set = set[:i] + ["D", "D"] + set[i + 1:]
        if step == "B2":
            i = set.index(step)
            set = set[:i] + ["B", "B"] + set[i + 1:]
        if step == "F'2":
            i =set.index(step)
            set = set[:i] + ["F'", "F'"] + set[i+1:]
        if step == "U'2":
            i =set.index(step)
            set = set[:i] + ["U'", "U'"] + set[i+1:]
        if step == "R'2":
            i =set.index(step)
            set = set[:i] + ["R'", "R'"] + set[i+1:]
        if step == "L'2":
            i =set.index(step)
            set = set[:i] + ["L'", "L'"] + set[i+1:]
        if step == "D'2":
            i = set.index(step)
            set = set[:i] + ["D'", "D'"] + set[i + 1:]
        if step == "B'2":
            i = set.index(step)
            set = set[:i] + ["B'", "B'"] + set[i + 1:]
        print(set)
    return set










def display(solution):
    capture = cv.VideoCapture(1)
    i =1
    for step in solution:
        if step == "B" or step == "B'":
            extra_steps = ["SR", step, "SL"]
            for extra_step in extra_steps:
                while True:
                    try:
                        isTrue, capvar = capture.read()
                        imgContours = capvar.copy()
                        blur = cv.GaussianBlur(capvar, (11, 11), 1)
                        canny = cv.Canny(blur, 150, 175)
                        # cv.imshow("gray", blurgray)
                        # cv.imshow("blur", blur)
                        kernel = np.ones((5, 5))
                        dilimg = cv.dilate(canny, kernel, iterations=1)
                        getcontuor1(blur, dilimg, imgContours, extra_step, i)
                        cv.imshow("imgcontour", imgContours)
                        cv.imshow("dil", dilimg)
                        # match_color(blur,imgContours)
                        # match_color(capvar)
                        if cv.waitKey(20) & 0xFF == ord('n'):
                            time.sleep(0.2)
                            i += 1
                            break
                    except AttributeError:
                        continue
                    except ValueError:
                        break
            continue
        while True:
            try:
                isTrue, capvar = capture.read()
                imgContours = capvar.copy()
                blur = cv.GaussianBlur(capvar, (11, 11), 1)
                canny = cv.Canny(blur, 150, 175)
                # cv.imshow("gray", blurgray)
                # cv.imshow("blur", blur)
                kernel = np.ones((5, 5))
                dilimg = cv.dilate(canny, kernel, iterations=1)
                getcontuor1(blur, dilimg, imgContours, step, i)
                cv.imshow("imgcontour", imgContours)
                cv.imshow("dil", dilimg)
                # match_color(blur,imgContours)
                # match_color(capvar)
                if cv.waitKey(20) & 0xFF == ord('n'):
                    time.sleep(0.2)
                    i += 1
                    break
            except AttributeError:
                continue
#B' L F' U D' F B U2 R2 F2 U' D B2 U2 B2 R2 B2
#solution = ['L',"F'",'U',"D'",'F','U','U','R','R','F','F',"U'",'D','U','U','R','R']
#display(solution)

#solution = ["B","B'"]
#display(solution)