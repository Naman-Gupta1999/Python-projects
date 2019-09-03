import cv2
import dlib
import os
import sys
import sqlite3

cam = cv2.VideoCapture(1)
detector = dlib.get_frontal_face_detector()
connect = sqlite3.connect("Face-DataBase.db")


if len(sys.argv) is not 1:
	img = cv2.imread(str(sys.argv[1]))
	dets = detector(img, 1)
	if not os.path.exists('D:\\PycharmProjects\\Microsoft_azure\\Cropped_faces'):
		os.makedirs('D:\\PycharmProjects\\Microsoft_azure\\Cropped_faces')
	print("detected = " + str(len(dets)))
	for i, d in enumerate(dets):
   		cv2.imwrite('D:\\PycharmProjects\\Microsoft_azure\\Cropped_faces\\face' + str(i + 1) + '.jpg', img[d.top():d.bottom(), d.left():d.right()])
