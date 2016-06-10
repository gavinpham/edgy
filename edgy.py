import cv2
import numpy as np
img = cv2.imread('/Users/Gavin/edgy/20160606_170352.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize = 3)
minLineLength = 5000
maxLineGap = 10
lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)

print len(lines)

#Loop through all found lines in the image
#Yeah it's gonna be insane
for line in lines:
	for x1,y1,x2,y2 in line:
		cv2.line(img,(x1,y1),(x2,y2),(0,0,255),5)

cv2.imwrite('/Users/Gavin/edgy/20160606_170352_2.jpg',img)
