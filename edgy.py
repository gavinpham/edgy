import cv2
import numpy as np
import os

for i in os.listdir(os.getcwd()):
	if i.endswith(".jpg"): 
		print i
		img = cv2.imread('/Users/Gavin/edgy/' + i)
		gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
		edges = cv2.Canny(gray,50,150,apertureSize = 3)
		minLineLength = 200
		maxLineGap = 10
		lines = cv2.HoughLinesP(edges,1,np.pi/180,100,0,minLineLength,maxLineGap)

		print len(lines)

		#Loop through all found lines in the image
		#Yeah it's gonna be insane
		for line in lines:
			for x1,y1,x2,y2 in line:
				cv2.line(img,(x1,y1),(x2,y2),(0,0,255),5)

		cv2.imwrite('/Users/Gavin/edgy/output/' + i,img)
		continue
	else:
		continue
