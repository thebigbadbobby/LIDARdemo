from time import time
# import cv2
import numpy as np
# import open3d as o3d
from PIL import Image
import matplotlib.pyplot as plt
from plyfile import PlyData, PlyElement
import json
import cv2
import os
import sys
import subprocess
# file_name="../../../../Data/Datasets/nuspace/sweeps/LIDAR_TOP/n008-2018-08-01-15-16-36-0400__LIDAR_TOP__1533151603597909.pcd.bin"
# file_ply="C:/Users/EavnJeong/Downloads/archive/ModelNet40_PLY/person/train/person_0011.ply"
file_ply="./cloud.ply"
file_depth="./depth.npy"
file_color="./color.npy"
# file_json="../../../..//Data/Datasets/ARKitScenes/raw/Training/41048190/41048190_3dod_annotation.json"

def load_json(js_path):
    with open(js_path, "r") as f:
        json_data = json.load(f)
    return json_data
def extract_from_pci_bin(file_name):
        scan = np.fromfile(file_name, dtype=np.float32)
        return scan.reshape((-1, 5))[:, :4]
def extract_from_ply_bin(filename):
        scan = PlyData.read(filename)
        x = np.array([list(tup) for tup in scan.elements[0].data])
        return x
        # print(scan)
        # print(scan.reshape((int(len(scan)/4),4)))
        # return scan.reshape((int(len(scan)/4),4))
# print(points)
def remove_close(points,radius: float) -> None:
        """
        Removes point too close within a certain radius from origin.
        :param radius: Radius below which points are removed.
        """

        x_filt = np.abs(points[:, 0]) < radius
        y_filt = np.abs(points[:, 1]) < radius
        not_close = np.logical_not(np.logical_and(x_filt, y_filt))
        return points[not_close, :]
def remove_low_intensity(points,thresh: float) -> None:
        """
        Removes point too close within a certain radius from origin.
        :param radius: Radius below which points are removed.
        """

        x_filt = np.abs(points[:, 3]) < thresh
        low_inten = np.logical_not(x_filt)
        return points[low_inten, :]

cmd=['c:/Python27/python.exe','../l515video.py']
process = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
print("simultaneous")
x=input()
print("terminate started")
process.terminate()
print("terminate ended")
idx=0
while True:
        try:
                # points=extract_from_ply_bin(file_ply)
                # np.save("cloud.npy",points)
                depth=np.load(f"depth{idx}.npy")
                color=np.load(f"depth{idx}.npy")
                # print(depth)
                # print(color)
                cv2.imwrite("./" + sys.argv[1] + f"/color_images/color{idx}.png",color)
                # clrimg=Image.fromarray(color)
                # clrimg.save("./" + sys.argv[1] + f"/color_images/color{idx}.png")
                depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth, alpha=0.03), cv2.COLORMAP_JET)
                print(idx)
                
                cv2.imwrite("./" + sys.argv[1] + f"/depth_images/depthgreyscale{idx}.png",depth)
                cv2.imwrite("./" + sys.argv[1] + f"/depth_images/depth{idx}.png",depth_colormap)
                # os.system('mkdir '+ sys.argv[1])
                # os.system('move cloud.ply '+ sys.argv[1])
                # os.system('move color*.png '+ sys.argv[1] + "/color_images/")
                # os.system('move depth*.png '+ sys.argv[1] + "/depth_images/")
                #        os.system('move *.png '+ sys.argv[1] + "/color_images/")
                # os.system('del *.npy ')
                idx+=1
        except:
                print("ekans")
                os.system("del *.npy /Q")
                break

