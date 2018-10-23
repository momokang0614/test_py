#!/usr/bin/env python
#coding:utf-8 
import serial
import cv2
import numpy as np
#这是第一个改动，测试push
bins = np.arange(256).reshape(256,1)


if __name__ == '__main__':
	size = 500
	step = 20
	axis = (255,255,255)
	grid = (64,64,64)
	cv2.namedWindow("im_in", 0)
	cv2.resizeWindow("im_in", 500, 500)
	im_origin = np.zeros((size, size, 3), np.uint8)
	cv2.line(im_origin, (0,size/2), (size, size/2),axis,1)
	i = size/2
	while i < size:
		i += step
		cv2.line(im_origin, (0,i), (size, i),grid,1)
		
	i = size/2
	while i > 0:
		i -= step
		cv2.line(im_origin, (0,i), (size, i),grid,1)
		
	cv2.line(im_origin, (size/2,0), (size/2,size),axis,1)

	i = size/2
	while i < size:
		i += step
		cv2.line(im_origin, (i,0), (i,size),grid,1)
		
	i = size/2
	while i > 0:
		i -= step
		cv2.line(im_origin, (i,0), (i,size),grid,1)
		
	serial = serial.Serial("COM8", 115200, timeout=0.5)
	cv2.imshow('im_in',im_origin)
	print "hello!"
	while cv2.waitKey(1):
		data = ''
		while serial.inWaiting() > 0:
		  data += serial.read(1)
		if data != '':
		  x = int(float(data.split()[0]))
		  y = int(float(data.split()[1]))
		  im = im_origin.copy()
		  im = cv2.circle(im,(x + size/2, y + size/2), 5, (0,0,255), -1)#目标点
		  cv2.imshow('im_in',im)
		
	cv2.destroyAllWindows()
