import pyrealsense2 as rs
import numpy as np
import time
# Declare pointcloud object, for calculating pointclouds and texture mappings
pc = rs.pointcloud()
# We want the points object to be persistent so we can display the last cloud when a frame drops
points = rs.points()

# Declare RealSense pipeline, encapsulating the actual device and sensors
# depth=rs.depth_frame()
pipe = rs.pipeline()
config = rs.config()
# Enable depth stream
config.enable_stream(rs.stream.depth)
# Start streaming with chosen configuration
pipe.start(config)

# We'll use the colorizer to generate texture for our PLY
# (alternatively, texture can be obtained from color or infrared stream)
colorizer = rs.colorizer()

while True:
    try:
        # Wait for the next set of frames from the camera
        frames = pipe.wait_for_frames()
        # colorized = colorizer.process(frames)

        # # Create save_to_ply object
        # ply = rs.save_to_ply("cloud.ply")
        depth_frame = frames.get_depth_frame()
        depth_image = np.asanyarray(depth_frame.get_data()).tolist()
        print(depth_image)
        time.sleep(.5)
        break
    except:
        pass
pipe.stop()