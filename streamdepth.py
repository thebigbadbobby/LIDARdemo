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
cmd=['c:/Python27/python.exe','../l515video.py']
process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
while stream_process(process):
    time.sleep(0.1)