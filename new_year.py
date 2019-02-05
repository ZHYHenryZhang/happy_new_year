""" Docstring:
Description: Happy new year
Author: Henry Zhang
Date:February 04, 2019
"""

# module
import numpy as np
import cv2
import pptk

# functions
def point_clond_generate(img):
  """ given image, generate point cloud based on black pixels """
  position = np.where(img[1]==[0,0,0])
  point_cloud = np.array(position).T
  return point_cloud

# main
if __name__ == "__main__":
  img = cv2.imread("data/new_year.png")
  # img = cv2.fromarray() np.array([[255, 0],[23, 199]], dtype=np.uint8)
  img_b = cv2.threshold(img,100,255,cv2.THRESH_BINARY)
  # cv2.imshow("binarized",img_b[1])
  # cv2.imshow("original",img)
  # cv2.waitKey(0)

  point_cloud = point_clond_generate(img_b)

  v = pptk.viewer(point_cloud)
  v.attributes(np.sum(point_cloud,axis=1)%255/2550.0)
  poses = []
  theta = np.pi/180
  r = 80
  i = 0
  poses.append([418, 849, 0, i * np.pi/2, theta * 24* i -np.pi/6, r*i**2])
  poses.append([418, 849, 0, i * np.pi/2, theta * 24* i -np.pi/6, r*i**2])
  for i in range(5):
    poses.append([418, 849, 0, i * np.pi/2, theta * 24* i -np.pi/6, r*i**2])
  poses.append([418, 849, r*4**2, 4 * np.pi/2, np.pi/2, 1])
  v.play(poses,2 * np.arange(8), repeat=False, interp='linear')