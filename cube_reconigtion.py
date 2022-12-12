import cv2 as cv
import numpy as np
import sys
import kociemba
import time
import copy
from cube_window import cube_window
import keyboard


def openwebcam():
    img_counter = 0
    capture = cv.VideoCapture(1)
    while True:
        isTrue, capvar = capture.read()
        cv.rectangle(capvar,(100,100),(450,450),(0,255,0),2)
        '''for i in range (200,350,50):
            for j in range (200,350,50):
                cv.rectangle(capvar, (i,j), (i+50, j+50), (0,255,0),2)'''
        cv.imshow('live',capvar)
        capvar = capvar[100:450, 100:450]
        if cv.waitKey(20)&0xFF == ord('s'):
            # s pressed
            img_name = "opencv_frame_{}.png".format(img_counter)
            cv.imwrite(img_name,capvar)
            print("{} written!".format(img_name))
            img_counter +=1
        if cv.waitKey(20)&0xFF==ord('q'):
            break



def getcontuor(blurimg,img, imgContours):
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
                show_green(blurimg, imgContours, x_, y_, w, h)
                show_red(blurimg, imgContours, x_, y_, w, h)
                show_blue(blurimg, imgContours, x_, y_, w, h)
                show_orange(blurimg, imgContours, x_, y_, w, h)
                show_yellow(blurimg, imgContours, x_, y_, w, h)


def getcontuors(blurimg,img, imgContours):
    global cube_face
    contours, hierarchy = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    cv.drawContours(imgContours, contours, -1, (255,0,0), 4)
    for cvt in contours:
        area = cv.contourArea(cvt)
        if area > 5000:
            cv.drawContours(imgContours, cvt, -1, (255,0,0), 4)
            peri = cv.arcLength(cvt, True)
            approx = cv.approxPolyDP(cvt, 0.02*peri, True)
            #print(len(approx))
            x_, y_, w, h=cv.boundingRect(approx)
            cv.rectangle(imgContours,(x_, y_),(x_+w,y_+h),(0,255,0), 3)
            cv.putText(imgContours, "Rubik's Cube", (x_+w+10,y_+h+10), cv.FONT_HERSHEY_COMPLEX, 0.7, (0,255,0),1)
            match_green(blurimg, imgContours, x_, y_, w, h)
            update_face_state(coordinates, 'G')
            match_blue(blurimg, imgContours, x_, y_, w, h)
            update_face_state(coordinates, 'B')
            match_red(blurimg, imgContours, x_, y_, w, h)
            update_face_state(coordinates, 'R')
            match_yellow(blurimg, imgContours, x_, y_, w, h)
            update_face_state(coordinates, 'Y')
            match_orange(blurimg, imgContours, x_, y_, w, h)
            update_face_state(coordinates, 'O')
            update_face_state(coordinates, 'W')
            cube_win =cube_window(cube_face)
            return cube_win
def match_color(imgvar, imgcontours):

    #image = cv.imread(filepath)
    #image = filepath
    masked_img = imgvar.copy()
    red_lower= np.array([0,100,10])
    red_upper= np.array([5,255,255])
    orange_lower= np.array([8,100,10])
    orange_upper= np.array([30,255,255])
    yellow_lower= np.array([30,50,10])
    yellow_upper= np.array([43,255,255])
    blue_lower= np.array([100,100,10])
    blue_upper= np.array([130,255,255])
    white_lower= np.array([0,0,10])
    white_upper= np.array([180,20,255])
    green_lower = np.array([45,100,10])
    green_upper = np.array([85,255,255])
    #blur = cv.GaussianBlur(image, (11,11), 3)
    #cv.imshow("blur", blur)
    frameHSV = cv.cvtColor(imgvar, cv.COLOR_BGR2HSV)
    green_mask = cv.inRange(frameHSV, green_lower, green_upper)
    red_mask = cv.inRange(frameHSV, red_lower, red_upper)
    blue_mask = cv.inRange(frameHSV, blue_lower, blue_upper)
    yellow_mask = cv.inRange(frameHSV, yellow_lower, yellow_upper)
    orange_mask = cv.inRange(frameHSV, orange_lower, orange_upper)
    white_mask = cv.inRange(frameHSV, white_lower, white_upper)
    masks = green_mask  + blue_mask  +orange_mask
    green_masked = cv.bitwise_and(masked_img, masked_img, mask=masks)
    cv.imshow("green mask ", green_masked)
    green_contours, green_hierachy = cv.findContours(green_mask.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    red_contours, red_hierachy = cv.findContours(red_mask.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    blue_contours, blue_hierachy = cv.findContours(blue_mask.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    yellow_contours, yellow_hierachy = cv.findContours(yellow_mask.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    orange_contours, orange_hierachy = cv.findContours(orange_mask.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    white_contours, white_hierachy = cv.findContours(white_mask.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

    for cvt in green_contours:
        area=cv.contourArea(cvt)
        if area > 10000:
            #cv.drawContours(imgcontours, cvt, -1, (0, 255, 0), 3)
            peri = cv.arcLength(cvt, True)
            approx = cv.approxPolyDP(cvt, 0.02*peri, True)
            #print(len(approx))
            x_, y_, w, h=cv.boundingRect(approx)
            cv.putText(imgcontours, "green", (x_+20,y_+20), cv.FONT_HERSHEY_COMPLEX, 0.7, (0,0,0),1)
    for cvt in red_contours:
        area=cv.contourArea(cvt)
        if area > 10000:
            #cv.drawContours(imgcontours, cvt, -1, (0, 0, 255), 3)
            peri = cv.arcLength(cvt, True)
            approx = cv.approxPolyDP(cvt, 0.02*peri, True)
            #print(len(approx))
            x_, y_, w, h=cv.boundingRect(approx)
            cv.putText(imgcontours, "red", (x_+20,y_+20), cv.FONT_HERSHEY_COMPLEX, 0.7, (0,0,0),1)

    for cvt in blue_contours:
        area=cv.contourArea(cvt)
        if area > 10000:
            cv.drawContours(imgcontours, cvt, -1, (255, 0, 0), 3)
            peri = cv.arcLength(cvt, True)
            approx = cv.approxPolyDP(cvt, 0.02*peri, True)
            #print(len(approx))
            x_, y_, w, h=cv.boundingRect(approx)
            cv.putText(imgcontours, "blue", (x_+20,y_+20), cv.FONT_HERSHEY_COMPLEX, 0.7, (0,0,0),1)
    for cvt in yellow_contours:
        area=cv.contourArea(cvt)
        if area > 10000:
            cv.drawContours(imgcontours, cvt, -1, (0, 255, 255), 3)
            peri = cv.arcLength(cvt, True)
            approx = cv.approxPolyDP(cvt, 0.02*peri, True)
            #print(len(approx))
            x_, y_, w, h=cv.boundingRect(approx)
            cv.putText(imgcontours, "yellow", (x_+20,y_+20), cv.FONT_HERSHEY_COMPLEX, 0.7, (0,0,0),1)
    for cvt in orange_contours:
        area=cv.contourArea(cvt)
        if area > 10000:
            cv.drawContours(imgcontours, cvt, -1, (0, 165, 255), 3)
            peri = cv.arcLength(cvt, True)
            approx = cv.approxPolyDP(cvt, 0.02*peri, True)
            #print(len(approx))
            x_, y_, w, h=cv.boundingRect(approx)
            cv.putText(imgcontours, "orange", (x_+20,y_+20), cv.FONT_HERSHEY_COMPLEX, 0.7, (0,0,0),1)
    for cvt in white_contours:
        area=cv.contourArea(cvt)
        if area > 10000:
            cv.drawContours(imgcontours, cvt, -1, (0, 0, 0), 6)
            peri = cv.arcLength(cvt, True)
            approx = cv.approxPolyDP(cvt, 0.02*peri, True)
            #print(len(approx))
            x_, y_, w, h=cv.boundingRect(approx)
            cv.putText(imgcontours, "white", (x_+10,y_+10), cv.FONT_HERSHEY_COMPLEX, 0.7, (0,255,0),1)



def show_green(imgvar, imgcontours, x, y, w, h):

    global coordinates
    coordinates =[]
    masked_img = imgvar.copy()
    green_lower = np.array([45,100,10])
    green_upper = np.array([85,255,255])
    frameHSV = cv.cvtColor(masked_img, cv.COLOR_BGR2HSV)
    green_mask = cv.inRange(frameHSV, green_lower, green_upper)
    sumofpixels = 0
    nonzero_pixel_coor = cv.findNonZero(green_mask)
    #print(nonzero_pixel_coor)
    nonzero_pixel_coor = nonzero_pixel_coor.tolist()
    for coors in nonzero_pixel_coor:
        for i in range(3):
            if x+30+((i)*w)/3< coors[0][0] < x-30+((i+1)*w)/3 :
                for j in range(3):
                    if y+30 + ((j)*h)/3 < coors[0][1] < y -30 + ((j+1)*h)/3 :
                        cv.rectangle(imgcontours,(coors[0][0],coors[0][1]),(coors[0][0]+10, coors[0][1]+10),(0,255,0),1)
                        sumofpixels += 1
                        #print(sumofpixels)
                    if sumofpixels > 1000:

                        sumofpixels = 0
                        break


def show_blue(imgvar, imgcontours, x, y, w, h):

    global coordinates
    coordinates =[]
    masked_img = imgvar.copy()
    blue_lower = np.array([90, 100, 10])
    blue_upper = np.array([130, 255, 255])
    frameHSV = cv.cvtColor(masked_img, cv.COLOR_BGR2HSV)
    blue_mask = cv.inRange(frameHSV, blue_lower, blue_upper)
    sumofpixels = 0
    nonzero_pixel_coor = cv.findNonZero(blue_mask)
    #print(nonzero_pixel_coor)
    nonzero_pixel_coor = nonzero_pixel_coor.tolist()
    for coors in nonzero_pixel_coor:
        for i in range(3):
            if x+30+((i)*w)/3< coors[0][0] < x-30+((i+1)*w)/3 :
                for j in range(3):
                    if y +30+ ((j)*h)/3 < coors[0][1] < y -30+ ((j+1)*h)/3 :
                        cv.rectangle(imgcontours,(coors[0][0],coors[0][1]),(coors[0][0]+10, coors[0][1]+10),(255,0,0),1)
                        sumofpixels += 1
                        #print(sumofpixels)
                    if sumofpixels > 1000:
                        #print(coordinates)
                        sumofpixels = 0
                        break

def show_red(imgvar, imgcontours, x, y, w, h):

    global coordinates
    coordinates =[]
    masked_img = imgvar.copy()
    red_lower = np.array([0, 100, 10])
    red_upper = np.array([9, 255, 255])
    frameHSV = cv.cvtColor(masked_img, cv.COLOR_BGR2HSV)
    red_mask = cv.inRange(frameHSV, red_lower, red_upper)
    sumofpixels = 0
    nonzero_pixel_coor = cv.findNonZero(red_mask)
    #print(nonzero_pixel_coor)
    nonzero_pixel_coor = nonzero_pixel_coor.tolist()
    for coors in nonzero_pixel_coor:
        for i in range(3):
            if x+30+((i)*w)/3< coors[0][0] < x-30+((i+1)*w)/3 :
                for j in range(3):
                    if y +30+ ((j)*h)/3 < coors[0][1] < y -30+ ((j+1)*h)/3 :
                        cv.rectangle(imgcontours,(coors[0][0],coors[0][1]),(coors[0][0]+10, coors[0][1]+10),(0,0,255),1)
                        sumofpixels += 1
                        #print(sumofpixels)
                    if sumofpixels > 800:
                        #print(coordinates)
                        sumofpixels = 0
                        break


def show_orange(imgvar, imgcontours, x, y, w, h):

    global coordinates
    coordinates =[]
    masked_img = imgvar.copy()
    orange_lower = np.array([10, 100, 10])
    orange_upper = np.array([30, 255, 255])
    frameHSV = cv.cvtColor(masked_img, cv.COLOR_BGR2HSV)
    orange_mask = cv.inRange(frameHSV, orange_lower, orange_upper)
    sumofpixels = 0
    nonzero_pixel_coor = cv.findNonZero(orange_mask)
    #print(nonzero_pixel_coor)
    nonzero_pixel_coor = nonzero_pixel_coor.tolist()
    for coors in nonzero_pixel_coor:
        for i in range(3):
            if x+30+((i)*w)/3< coors[0][0] < x-30+((i+1)*w)/3 :
                for j in range(3):
                    if y+30 + ((j)*h)/3 < coors[0][1] < y-30 + ((j+1)*h)/3 :
                        cv.rectangle(imgcontours,(coors[0][0],coors[0][1]),(coors[0][0]+10, coors[0][1]+10),(0,165,255),1)
                        sumofpixels += 1
                        #print(sumofpixels)
                    if sumofpixels > 1000:
                        #print(coordinates)
                        sumofpixels = 0
                        break


def show_yellow(imgvar, imgcontours, x, y, w, h):

    global coordinates
    coordinates =[]
    masked_img = imgvar.copy()
    yellow_lower = np.array([30, 50, 10])
    yellow_upper = np.array([43, 255, 255])
    frameHSV = cv.cvtColor(masked_img, cv.COLOR_BGR2HSV)
    yellow_mask = cv.inRange(frameHSV, yellow_lower, yellow_upper)
    sumofpixels = 0
    nonzero_pixel_coor = cv.findNonZero(yellow_mask)
    #print(nonzero_pixel_coor)
    nonzero_pixel_coor = nonzero_pixel_coor.tolist()
    for coors in nonzero_pixel_coor:
        for i in range(3):
            if x+30+((i)*w)/3< coors[0][0] < x-30+((i+1)*w)/3 :
                for j in range(3):
                    if y +30+ ((j)*h)/3 < coors[0][1] < y -30+ ((j+1)*h)/3 :
                        cv.rectangle(imgcontours,(coors[0][0],coors[0][1]),(coors[0][0]+10, coors[0][1]+10),(0,255,255),1)
                        sumofpixels += 1
                        #print(sumofpixels)
                    if sumofpixels > 1000:
                        #print(coordinates)
                        sumofpixels = 0
                        break


def match_green(imgvar, imgcontours, x, y, w, h):

    global coordinates
    coordinates =[]
    masked_img = imgvar.copy()
    green_lower = np.array([45,100,10])
    green_upper = np.array([85,255,255])
    frameHSV = cv.cvtColor(masked_img, cv.COLOR_BGR2HSV)
    green_mask = cv.inRange(frameHSV, green_lower, green_upper)
    sumofpixels = 0
    nonzero_pixel_coor = cv.findNonZero(green_mask)
    #print(nonzero_pixel_coor)
    nonzero_pixel_coor = nonzero_pixel_coor.tolist()
    for coors in nonzero_pixel_coor:
        for i in range(3):
            if x+30+((i)*w)/3< coors[0][0] < x-30+((i+1)*w)/3 :
                for j in range(3):
                    if y+30 + ((j)*h)/3 < coors[0][1] < y -30 + ((j+1)*h)/3 :
                        cv.rectangle(imgcontours,(coors[0][0],coors[0][1]),(coors[0][0]+10, coors[0][1]+10),(0,255,0),1)
                        sumofpixels += 1
                        #print(sumofpixels)
                    if sumofpixels > 600:
                        coordinates.append([j,i])
                        #print(coordinates)
                        sumofpixels = 0
                        break


def match_blue(imgvar, imgcontours, x, y, w, h):

    global coordinates
    coordinates =[]
    masked_img = imgvar.copy()
    blue_lower = np.array([90, 100, 10])
    blue_upper = np.array([130, 255, 255])
    frameHSV = cv.cvtColor(masked_img, cv.COLOR_BGR2HSV)
    blue_mask = cv.inRange(frameHSV, blue_lower, blue_upper)
    sumofpixels = 0
    nonzero_pixel_coor = cv.findNonZero(blue_mask)
    #print(nonzero_pixel_coor)
    nonzero_pixel_coor = nonzero_pixel_coor.tolist()
    for coors in nonzero_pixel_coor:
        for i in range(3):
            if x+30+((i)*w)/3< coors[0][0] < x-30+((i+1)*w)/3 :
                for j in range(3):
                    if y +30+ ((j)*h)/3 < coors[0][1] < y -30+ ((j+1)*h)/3 :
                        cv.rectangle(imgcontours,(coors[0][0],coors[0][1]),(coors[0][0]+10, coors[0][1]+10),(255,0,0),1)
                        sumofpixels += 1
                        #print(sumofpixels)
                    if sumofpixels > 600:
                        coordinates.append([j,i])
                        #print(coordinates)
                        sumofpixels = 0
                        break

def match_red(imgvar, imgcontours, x, y, w, h):

    global coordinates
    coordinates =[]
    masked_img = imgvar.copy()
    red_lower = np.array([0, 100, 10])
    red_upper = np.array([9, 255, 255])
    frameHSV = cv.cvtColor(masked_img, cv.COLOR_BGR2HSV)
    red_mask = cv.inRange(frameHSV, red_lower, red_upper)
    sumofpixels = 0
    nonzero_pixel_coor = cv.findNonZero(red_mask)
    #print(nonzero_pixel_coor)
    nonzero_pixel_coor = nonzero_pixel_coor.tolist()
    for coors in nonzero_pixel_coor:
        for i in range(3):
            if x+30+((i)*w)/3< coors[0][0] < x-30+((i+1)*w)/3 :
                for j in range(3):
                    if y +30+ ((j)*h)/3 < coors[0][1] < y -30+ ((j+1)*h)/3 :
                        cv.rectangle(imgcontours,(coors[0][0],coors[0][1]),(coors[0][0]+10, coors[0][1]+10),(0,0,255),1)
                        sumofpixels += 1
                        #print(sumofpixels)
                    if sumofpixels > 600:
                        coordinates.append([j,i])
                        #print(coordinates)
                        sumofpixels = 0
                        break


def match_orange(imgvar, imgcontours, x, y, w, h):
#
    global coordinates
    coordinates =[]
    masked_img = imgvar.copy()
    orange_lower = np.array([10, 100, 10])
    orange_upper = np.array([30, 255, 255])
    frameHSV = cv.cvtColor(masked_img, cv.COLOR_BGR2HSV)
    orange_mask = cv.inRange(frameHSV, orange_lower, orange_upper)
    sumofpixels = 0
    nonzero_pixel_coor = cv.findNonZero(orange_mask)
    #print(nonzero_pixel_coor)
    nonzero_pixel_coor = nonzero_pixel_coor.tolist()
    for coors in nonzero_pixel_coor:
        for i in range(3):
            if x+30+((i)*w)/3< coors[0][0] < x-30+((i+1)*w)/3 :
                for j in range(3):
                    if y+30 + ((j)*h)/3 < coors[0][1] < y-30 + ((j+1)*h)/3 :
                        cv.rectangle(imgcontours,(coors[0][0],coors[0][1]),(coors[0][0]+10, coors[0][1]+10),(0,165,255),1)
                        sumofpixels += 1
                        #print(sumofpixels)
                    if sumofpixels > 600:
                        coordinates.append([j,i])
                        #print(coordinates)
                        sumofpixels = 0
                        break


def match_yellow(imgvar, imgcontours, x, y, w, h):

    global coordinates
    coordinates =[]
    masked_img = imgvar.copy()
    yellow_lower = np.array([30, 50, 10])
    yellow_upper = np.array([43, 255, 255])
    frameHSV = cv.cvtColor(masked_img, cv.COLOR_BGR2HSV)
    yellow_mask = cv.inRange(frameHSV, yellow_lower, yellow_upper)
    sumofpixels = 0
    nonzero_pixel_coor = cv.findNonZero(yellow_mask)
    #print(nonzero_pixel_coor)
    nonzero_pixel_coor = nonzero_pixel_coor.tolist()
    for coors in nonzero_pixel_coor:
        for i in range(3):
            if x+30+((i)*w)/3< coors[0][0] < x-30+((i+1)*w)/3 :
                for j in range(3):
                    if y +30+ ((j)*h)/3 < coors[0][1] < y -30+ ((j+1)*h)/3 :
                        cv.rectangle(imgcontours,(coors[0][0],coors[0][1]),(coors[0][0]+10, coors[0][1]+10),(255,255,0),1)
                        sumofpixels += 1
                        #print(sumofpixels)
                    if sumofpixels > 400:
                        coordinates.append([j,i])
                        #print(coordinates)
                        sumofpixels = 0
                        break



'''
def record_color(masked_image,imgcontours):
    global nonzero_pixel_coor
    sumofpixels = 0
    nonzero_pixel_coor = cv.findNonZero(masked_image)
    print(nonzero_pixel_coor)
    nonzero_pixel_coor = nonzero_pixel_coor.tolist()
    for coors in nonzero_pixel_coor:
        cv.rectangle(imgcontours,(coors[0][0],coors[0][1]),(coors[0][0]+10, coors[0][1]+10),(0,0,0),1)
        sumofpixels += 1
    print(sumofpixels)


def record_colors(masked_image,imgcontours,x,y,w,h):
    global nonzero_pixel_coor
    sumofpixels = 0
    nonzero_pixel_coor = cv.findNonZero(masked_image)
    print(nonzero_pixel_coor)
    nonzero_pixel_coor = nonzero_pixel_coor.tolist()
    for coors in nonzero_pixel_coor:
        for i in range(3):
            if (i+1)*x < coors[0][0] < (i+1)*x+w :
                for i in range(3):
                    if (i+1)*y < coors[0][1] < (i+1)*y+h :
                        cv.rectangle(imgcontours,(coors[0][0],coors[0][1]),(coors[0][0]+10, coors[0][1]+10),(0,0,0),1)
                        sumofpixels += 1
                        print(sumofpixels)
'''

def update_face_state(coordinate, color):
    global cube_face
    if color != 'W':
        for coor in coordinate:
            #if cube_face[coor[0]][coor[1]] == 0 :
            cube_face[coor[0]][coor[1]] = color
    else:
        for i in range(3):
            for j in range(3):
                if cube_face[i][j] == 0 :
                    cube_face[i][j] = 'W'




def update_cube_state(cube_face):
    if cube_face[1][1] == "W":
        cube_state[1] = cube_face
        print(cube_state[1])
    if cube_face[1][1] == "B":
        cube_state[0] = cube_face
        print(cube_state[0])
    if cube_face[1][1] == "R":
        cube_state[2] = cube_face
        print(cube_state[2])
    if cube_face[1][1] == "Y":
        cube_state[3] = cube_face
        print(cube_state[3])
    if cube_face[1][1] == "O":
        cube_state[4] = cube_face
        print(cube_state[4])
    if cube_face[1][1] == "G":
        cube_state[5] = cube_face
        print(cube_state[5])


def detect_cube():
    global cube_state
    global cube_face
    global cube_faceshow
    cube_state = []

    for i in range(6):
        cube_state.append(0)

    cube_face = []

    for i in range(3):
        cube_face.append([])
        for j in range(3):
            cube_face[i].append(0)

    capture = cv.VideoCapture(1)
    capture.set(cv.CAP_PROP_EXPOSURE, 80)
    for k in range(6):
        while True:
            try:
                isTrue, capvar = capture.read()
                imgContours = capvar.copy()
                blur = cv.GaussianBlur(capvar, (11,11), 1)
                canny = cv.Canny(blur, 150, 175)
                #cv.imshow("gray", blurgray)
                    #cv.imshow("blur", blur)
                kernel = np.ones((5,5))
                dilimg = cv.dilate(canny, kernel, iterations=1)
                getcontuor(blur, dilimg, imgContours)
                cv.imshow("imgcontour", imgContours)
                cv.imshow("dil", dilimg)
                #match_color(blur,imgContours)
                #match_color(capvar)

                if cv.waitKey(20) & 0xFF == ord('q'):

                    blank = getcontuors(blur, dilimg, imgContours)
                    cv.imshow("imgcontour", imgContours)
                    #update_cube_state(cube_face)
                    print(cube_face)
                if cv.waitKey(20) & 0xFF == ord('s'):
                    #keyboard.wait('s')
                    print(k + 1)
                    cv.putText(imgContours, "Done Recording, next face", (80, 400), cv.FONT_HERSHEY_COMPLEX, 0.7,
                               (0, 255, 0), 1)
                    cv.imshow("imgcontour", imgContours)
                    update_cube_state(cube_face)
                    print(cube_face)
                    cube_face = []
                    for i in range(3):
                        cube_face.append([])
                        for j in range(3):
                            cube_face[i].append(0)

                    break

            except AttributeError:
                continue

    print(cube_state)
    return copy.deepcopy(cube_state)





#match_color("E:\Documents\OneDrive\PYTHON\SCRIPTS\MachineLearning\opencv_frame_0.png")
#openwebcam()

#def mapping():
'''
cube_state = []

for i in range(6):
    cube_state.append(0)

cube_face = []

for i in range(3):
    cube_face.append([])
    for j in range(3):
        cube_face[i].append(0)

cube_faceshow = []

for i in range(3):
    cube_faceshow.append([])
    for j in range(3):
        cube_faceshow[i].append(0)


cubestring = ''
for i in range(6):
    for j in range(3):
        for k in range(3):
            cubestring = cubestring + cube_state[i][j][k]

cubestring = cubestring.replace('B','U')
cubestring = cubestring.replace('W','F')
cubestring = cubestring.replace('G', 'D')
cubestring = cubestring.replace('O','L')
cubestring = cubestring.replace('Y','B')
print(cubestring)'''