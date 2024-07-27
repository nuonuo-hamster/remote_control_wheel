# pip install pyrealsense2
import pyrealsense2 as rs
import numpy as np
import cv2

def realsense_init(width, height):

    pipe = rs.pipeline()
    cfg  = rs.config()

    cfg.enable_stream(rs.stream.color, width,height, rs.format.bgr8, 30)
    cfg.enable_stream(rs.stream.depth, width,height, rs.format.z16, 30)

    pipe.start(cfg)

    return pipe

def realsense_run(pipe):

    frame = pipe.wait_for_frames()
    depth_frame = frame.get_depth_frame()
    color_frame = frame.get_color_frame()

    depth_image = np.asanyarray(depth_frame.get_data())
    color_image = np.asanyarray(color_frame.get_data())
    depth_cm = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, 
                                alpha = 0.5), cv2.COLORMAP_JET)

    return depth_frame, color_image, depth_cm

def main():
    pipe = realsense_init(width=640, height=480)
    
    while(True):
        depth_frame, color_image, depth_cm = realsense_run(pipe)
        cv2.imshow('RGB Frame', color_image)
        if cv2.waitKey(1) == 27: # esc
            break
    
    cv2.destroyAllWindows()
    pipe.stop()

if __name__ == '__main__':
    main()