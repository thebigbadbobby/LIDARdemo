# LIDARdemo
live feed and picture capabilities
1. download Intel Realsense SDK (800 MB)
2. git clone this repo in Intel Realsense SDK 2.0/bin/x64
3. move l515video.py and l515picture.py back one directory
4. fix paths for your machine. Python2 or python3 paths may not work). Files moved back one directory use python 2.
5. 
a. run "expandpicture.py directory" to take a single picture with all data going to directory - includes .ply, depth, and color.
b. run "streamvideo.py"to bring up the live color video feed."
c. run "streamdepth.py" to process depth data in real time (in development).
