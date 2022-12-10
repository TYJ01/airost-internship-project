import cv2 as cv
import numpy as np


def cube_window(cube_face):
    blank = np.zeros((500, 500, 3), dtype='uint8')
    cv.imshow("cube face", blank)

    for i in range(3):
        for j in range(3):
            cv.rectangle(blank, (100 + 50 * i, 100 + 50 * j), (100 + 50 * (i + 1), 100 + 50 * (j + 1)), (0, 255, 0), 2)

    for i in range(3):
        for j in range(3):
            if cube_face[i][j] == "G":
                cv.rectangle(blank, (100 + 50 * j, 100 + 50 * i), (100 + 50 * (j + 1), 100 + 50 * (i + 1)),
                             (0, 255, 0), -1)
            if cube_face[i][j] == "B":
                cv.rectangle(blank, (100 + 50 * j, 100 + 50 * i), (100 + 50 * (j + 1), 100 + 50 * (i + 1)),
                             (255, 0, 0), -1)
            if cube_face[i][j] == "R":
                cv.rectangle(blank, (100 + 50 * j, 100 + 50 * i), (100 + 50 * (j + 1), 100 + 50 * (i + 1)),
                             (0, 0, 255), -1)
            if cube_face[i][j] == "Y":
                cv.rectangle(blank, (100 + 50 * j, 100 + 50 * i), (100 + 50 * (j + 1), 100 + 50 * (i + 1)),
                             (0, 255, 255), -1)
            if cube_face[i][j] == "O":
                cv.rectangle(blank, (100 + 50 * j, 100 + 50 * i), (100 + 50 * (j + 1), 100 + 50 * (i + 1)),
                             (0, 165, 255), -1)
            if cube_face[i][j] == "W":
                cv.rectangle(blank, (100 + 50 * j, 100 + 50 * i), (100 + 50 * (j + 1), 100 + 50 * (i + 1)),
                             (255, 255, 255), -1)
    cv.imshow("cube face", blank)
def cube_window1(cube_face):
    blank = np.zeros((500,500,3), dtype='uint8')
    cv.imshow("blank", blank)

    for i in range(3):
        for j in range(3):
            cv.rectangle(blank,(200 + 20*i,100+ 20*j),(200 + 20*(i+1),100 + 20*(j+1)),(0,255,0),2)

    for k in range(4):
        for i in range(3):
            for j in range(3):
                cv.rectangle(blank,(140+(60*k) + 20*i,160+ 20*j),(140+(60*k) + 20*(i+1),160+ 20*(j+1)),(0,255,0),2)
    for i in range(3):
        for j in range(3):
            cv.rectangle(blank,(200 + 20*i,220+ 20*j),(200 + 20*(i+1),220 + 20*(j+1)),(0,255,0),2)
    if cube_face[1][1] == "W":
        for i in range(3):
            for j in range(3):
                if cube_face[i][j] == "G":
                    cv.rectangle(blank, (200 + 20 * j, 100 + 20 * i), (200 + 20 * (j + 1), 100 + 20 * (i + 1)),
                                 (0, 255, 0), -1)
                if cube_face[i][j] == "B":
                    cv.rectangle(blank, (200 + 20 * j, 100 + 20 * i), (200 + 20 * (j + 1), 100 + 20 * (i + 1)),
                                 (255, 0, 0), -1)
                if cube_face[i][j] == "R":
                    cv.rectangle(blank, (200 + 20 * j, 100 + 20 * i), (200 + 20 * (j + 1), 100 + 20 * (i + 1)),
                                 (0, 0, 255), -1)
                if cube_face[i][j] == "Y":
                    cv.rectangle(blank, (200 + 20 * j, 100 + 20 * i), (200 + 20 * (j + 1), 100 + 20 * (i + 1)),
                                 (0, 255, 255), -1)
                if cube_face[i][j] == "O":
                    cv.rectangle(blank, (200 + 20 * j, 100 + 20 * i), (200 + 20 * (j + 1), 100 + 20 * (i + 1)),
                                 (0, 165, 255), -1)
                if cube_face[i][j] == "W":
                    cv.rectangle(blank, (200 + 20 * j, 100 + 20 * i), (200 + 20 * (j + 1), 100 + 20 * (i + 1)),
                                 (255, 255, 255), -1)
    if cube_face[1][1] == "B":
        for i in range(3):
            for j in range(3):
                if cube_face[i][j] == "G":
                    cv.rectangle(blank, (200 + 20 * j, 100 + 20 * i), (200 + 20 * (j + 1), 100 + 20 * (i + 1)),
                                     (0, 255, 0), -1)
                if cube_face[i][j] == "B":
                    cv.rectangle(blank, (200 + 20 * j, 100 + 20 * i), (200 + 20 * (j + 1), 100 + 20 * (i + 1)),
                                     (255, 0, 0), -1)
                if cube_face[i][j] == "R":
                    cv.rectangle(blank, (200 + 20 * j, 100 + 20 * i), (200 + 20 * (j + 1), 100 + 20 * (i + 1)),
                                     (0, 0, 255), -1)
                if cube_face[i][j] == "Y":
                    cv.rectangle(blank, (200 + 20 * j, 100 + 20 * i), (200 + 20 * (j + 1), 100 + 20 * (i + 1)),
                                     (0, 255, 255), -1)
                if cube_face[i][j] == "O":
                    cv.rectangle(blank, (200 + 20 * j, 100 + 20 * i), (200 + 20 * (j + 1), 100 + 20 * (i + 1)),
                                     (0, 165, 255), -1)
                if cube_face[i][j] == "W":
                    cv.rectangle(blank, (200 + 20 * j, 100 + 20 * i), (200 + 20 * (j + 1), 100 + 20 * (i + 1)),
                                     (255, 255, 255), -1)
    if cube_face[1][1] == "R":
        for i in range(3):
            for j in range(3):
                if cube_face[i][j] == "G":
                    cv.rectangle(blank, (200 + 20 * j, 100 + 20 * i), (200 + 20 * (j + 1), 100 + 20 * (i + 1)),
                                 (0, 255, 0), -1)
                if cube_face[i][j] == "B":
                    cv.rectangle(blank, (200 + 20 * j, 100 + 20 * i), (200 + 20 * (j + 1), 100 + 20 * (i + 1)),
                                 (255, 0, 0), -1)
                if cube_face[i][j] == "R":
                    cv.rectangle(blank, (200 + 20 * j, 100 + 20 * i), (200 + 20 * (j + 1), 100 + 20 * (i + 1)),
                                 (0, 0, 255), -1)
                if cube_face[i][j] == "Y":
                    cv.rectangle(blank, (200 + 20 * j, 100 + 20 * i), (200 + 20 * (j + 1), 100 + 20 * (i + 1)),
                                 (0, 255, 255), -1)
                if cube_face[i][j] == "O":
                    cv.rectangle(blank, (200 + 20 * j, 100 + 20 * i), (200 + 20 * (j + 1), 100 + 20 * (i + 1)),
                                 (0, 165, 255), -1)
                if cube_face[i][j] == "W":
                    cv.rectangle(blank, (200 + 20 * j, 100 + 20 * i), (200 + 20 * (j + 1), 100 + 20 * (i + 1)),
                                 (255, 255, 255), -1)
    if cube_face[1][1] == "Y":
        for i in range(3):
            for j in range(3):
                if cube_face[i][j] == "G":
                    cv.rectangle(blank, (200 + 20 * j, 100 + 20 * i), (200 + 20 * (j + 1), 100 + 20 * (i + 1)),
                                 (0, 255, 0), -1)
                if cube_face[i][j] == "B":
                    cv.rectangle(blank, (200 + 20 * j, 100 + 20 * i), (200 + 20 * (j + 1), 100 + 20 * (i + 1)),
                                 (255, 0, 0), -1)
                if cube_face[i][j] == "R":
                    cv.rectangle(blank, (200 + 20 * j, 100 + 20 * i), (200 + 20 * (j + 1), 100 + 20 * (i + 1)),
                                 (0, 0, 255), -1)
                if cube_face[i][j] == "Y":
                    cv.rectangle(blank, (200 + 20 * j, 100 + 20 * i), (200 + 20 * (j + 1), 100 + 20 * (i + 1)),
                                 (0, 255, 255), -1)
                if cube_face[i][j] == "O":
                    cv.rectangle(blank, (200 + 20 * j, 100 + 20 * i), (200 + 20 * (j + 1), 100 + 20 * (i + 1)),
                                 (0, 165, 255), -1)
                if cube_face[i][j] == "W":
                    cv.rectangle(blank, (200 + 20 * j, 100 + 20 * i), (200 + 20 * (j + 1), 100 + 20 * (i + 1)),
                                 (255, 255, 255), -1)
    if cube_face[1][1] == "O":
        for i in range(3):
            for j in range(3):
                if cube_face[i][j] == "G":
                    cv.rectangle(blank, (200 + 20 * j, 100 + 20 * i), (200 + 20 * (j + 1), 100 + 20 * (i + 1)),
                                 (0, 255, 0), -1)
                if cube_face[i][j] == "B":
                    cv.rectangle(blank, (200 + 20 * j, 100 + 20 * i), (200 + 20 * (j + 1), 100 + 20 * (i + 1)),
                                 (255, 0, 0), -1)
                if cube_face[i][j] == "R":
                    cv.rectangle(blank, (200 + 20 * j, 100 + 20 * i), (200 + 20 * (j + 1), 100 + 20 * (i + 1)),
                                 (0, 0, 255), -1)
                if cube_face[i][j] == "Y":
                    cv.rectangle(blank, (200 + 20 * j, 100 + 20 * i), (200 + 20 * (j + 1), 100 + 20 * (i + 1)),
                                 (0, 255, 255), -1)
                if cube_face[i][j] == "O":
                    cv.rectangle(blank, (200 + 20 * j, 100 + 20 * i), (200 + 20 * (j + 1), 100 + 20 * (i + 1)),
                                 (0, 165, 255), -1)
                if cube_face[i][j] == "W":
                    cv.rectangle(blank, (200 + 20 * j, 100 + 20 * i), (200 + 20 * (j + 1), 100 + 20 * (i + 1)),
                                 (255, 255, 255), -1)
    if cube_face[1][1] == "G":
        for i in range(3):
            for j in range(3):
                if cube_face[i][j] == "G":
                    cv.rectangle(blank, (200 + 20 * j, 100 + 20 * i), (200 + 20 * (j + 1), 100 + 20 * (i + 1)),
                                 (0, 255, 0), -1)
                if cube_face[i][j] == "B":
                    cv.rectangle(blank, (200 + 20 * j, 100 + 20 * i), (200 + 20 * (j + 1), 100 + 20 * (i + 1)),
                                 (255, 0, 0), -1)
                if cube_face[i][j] == "R":
                    cv.rectangle(blank, (200 + 20 * j, 100 + 20 * i), (200 + 20 * (j + 1), 100 + 20 * (i + 1)),
                                 (0, 0, 255), -1)
                if cube_face[i][j] == "Y":
                    cv.rectangle(blank, (200 + 20 * j, 100 + 20 * i), (200 + 20 * (j + 1), 100 + 20 * (i + 1)),
                                 (0, 255, 255), -1)
                if cube_face[i][j] == "O":
                    cv.rectangle(blank, (200 + 20 * j, 100 + 20 * i), (200 + 20 * (j + 1), 100 + 20 * (i + 1)),
                                 (0, 165, 255), -1)
                if cube_face[i][j] == "W":
                    cv.rectangle(blank, (200 + 20 * j, 100 + 20 * i), (200 + 20 * (j + 1), 100 + 20 * (i + 1)),
                                 (255, 255, 255), -1)
    cv.imshow("blank", blank)
    cv.waitKey(0)