import cv2
import numpy as np

#read in img and turn to gray (thats why theres a zero)
img = cv2.imread('20160606_170352.jpg', 0)
# edges = cv2.Canny(img,50,150)

# lines = cv2.HoughLines(edges,1,np.pi/180,100)
# for rho,theta in lines[0]:
# 	print rho
# 	print theta
# 	a = np.cos(theta)
# 	b = np.sin(theta)
# 	x0 = a*rho
# 	y0 = b*rho
# 	x1 = int(x0 + 1000*(-b))
# 	y1 = int(y0 + 1000*(a))
# 	x2 = int(x0 - 1000*(-b))
# 	y2 = int(y0 - 1000*(a))

# 	cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

cv2.imwrite('20160606_170352_2.jpg',img)