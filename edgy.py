import cv2
import numpy as np
import os

for filename in os.listdir(os.getcwd()):
	if filename.endswith(".jpg"): 
		print filename
		print "\tPerforming Blob Test"
		 
		# Read image (Blob detection)
		im = cv2.imread('/Users/Gavin/edgy/' + filename, cv2.IMREAD_GRAYSCALE)
		cv2.imwrite('/Users/Gavin/edgy/output/gray_' + filename, im)
		 
		# Set up the detector with default parameters.
		detector = cv2.SimpleBlobDetector_create()
		 
		# Detect blobs.
		keypoints = detector.detect(im)
		 
		# Draw detected blobs as red circles.
		# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
		im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
		 
		# Write out 
		cv2.imwrite('/Users/Gavin/edgy/output/blob_' + filename,im_with_keypoints)

		# Read image (Canny & Hough)
		img = cv2.imread('/Users/Gavin/edgy/' + filename)
		gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
		
		# Find edges
		edges = cv2.Canny(gray,100,200)
		
		# # Find contours
		# ret,thresh = cv2.threshold(gray,127,255,0)
		# print cv2.findContours(thresh,1,2)
		# countours, hierarchy = cv2.findContours(thresh,1,2).iteritems()
		# cv2.drawContours(gray, contours, -1, (0,255,0), 3)
		# cv2.imwrite('/Users/Gavin/edgy/output/contours_' + filename, gray)
		
		# Write out Canny results
		cv2.imwrite('/Users/Gavin/edgy/output/canny_' + filename,edges)

		# Finegle the deets of Hough
		minLineLength = 200
		maxLineGap = 10
		lines = cv2.HoughLinesP(edges,1,np.pi/180,100,0,minLineLength,maxLineGap)

		print "\tNumber of lines found: " + str(len(lines))

		# Loop through all found lines in the image
		# Yeah it's gonna be insane
		for line in lines:
			for x1,y1,x2,y2 in line:
				cv2.line(img,(x1,y1),(x2,y2),(0,0,255),5)

		cv2.imwrite('/Users/Gavin/edgy/output/hough_' + filename,img)
		continue
	else:
		continue
