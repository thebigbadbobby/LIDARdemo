import numpy as np
# import open3d as o3d
from PIL import Image
import matplotlib.pyplot as plt
from plyfile import PlyData, PlyElement
import json
import cv2
import os
import sys
import time
import subprocess
# depth=np.load("../depth_image0.npy")
# print(np.type(depth))
# depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth, alpha=0.03), cv2.COLORMAP_JET)
# cv2.imwrite("./"+"depthgreyscale0.png",depth/30000)
# cv2.imwrite("./"+"depth0.png",depth_colormap)

os.system('c:/Python27/python.exe ../l515picture.py"')
# points=extract_from_ply_bin(file_ply)
# np.save("cloud.npy",points)
depth=np.load("depth.npy")
depth=np.load("../depth_image0.npy")
depth=depth.tolist()
depth=np.array(depth, dtype=np.uint16)
# color=np.load(file_color)
# print(depth)
# print(color)
# clrimg=Image.fromarray(color)
# clrimg.save("./" + sys.argv[1] + f"color{idx}.png")

depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth, alpha=0.03), cv2.COLORMAP_JET)

cv2.imwrite("./" f"depthgreyscale0.png",depth)
