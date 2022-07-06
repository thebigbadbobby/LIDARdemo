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
def stream_process(process):
    go = process.poll() is None
    for line in process.stdout:
        print(line)
    return go
# cmd=['c:/Python27/python.exe','../l515video.py']
# process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
# while stream_process(process):
#     time.sleep(0.1)
idx=0
while True:
    depth=np.load("../depth_image"+str(idx) + ".npy")
    # clrimg=Image.fromarray(color)
    # depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth, alpha=0.03), cv2.COLORMAP_JET)
    # cv2.imwrite("./"+f"depthgreyscale{i}.png",depth)
    # cv2.imwrite("./"+f"depth{i}.png",depth_colormap)
    
    # color=np.load(file_color)
    # print(depth)
    # print(color)
    # clrimg=Image.fromarray(color)
    # clrimg.save("./" + sys.argv[1] + f"color{idx}.png")
    # depth=np.load(file_depth)
    # color=np.load(file_color)
    # print(depth)
    # print(color)
    # clrimg=Image.fromarray(color)
    # clrimg.save("./" + sys.argv[1] + f"color{idx}.png")
    
    # t = time()
    depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth, alpha=0.03), cv2.COLORMAP_JET)
    # print(time() - t)
    depth=depth.tolist()
    depth=np.array(depth, dtype=np.uint16)
    
    cv2.imwrite("./" f"depthgreyscale{idx}.png",depth)
    cv2.imwrite("./" f"depth{idx}.png",depth_colormap)
    idx+=1