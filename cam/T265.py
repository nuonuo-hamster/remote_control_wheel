import pyrealsense2 as rs
import numpy as np
import transformations as tf
import math as m
import os 

H_aeroRef_T265Ref = np.array([[0,0,-1,0],[1,0,0,0],[0,-1,0,0],[0,0,0,1]])
H_T265body_aeroBody = np.linalg.inv(H_aeroRef_T265Ref)


def cam_init():
    # Declare RealSense pipeline, encapsulating the actual device and sensors
    pipe = rs.pipeline()

    # Build config object and request pose data
    cfg = rs.config()
    cfg.enable_stream(rs.stream.pose)

    # Start streaming with requested config
    pipe.start(cfg)

    return pipe

def get_degree(pipe):
    try:
        # Wait for the next set of frames from the camera
        frames = pipe.wait_for_frames()

        # Fetch pose frame
        pose = frames.get_pose_frame()
        if pose:
            # Print some of the pose data to the terminal
            data = pose.get_pose_data()

            H_T265Ref_T265body = tf.quaternion_matrix([data.rotation.w, data.rotation.x,data.rotation.y,data.rotation.z]) # in transformations, Quaternions w+ix+jy+kz are represented as [w, x, y, z]!

            # transform to aeronautic coordinates (body AND reference frame!)
            H_aeroRef_aeroBody = H_aeroRef_T265Ref.dot( H_T265Ref_T265body.dot( H_T265body_aeroBody ))

            rpy_rad = np.array( tf.euler_from_matrix(H_aeroRef_aeroBody, 'sxyz') ) # Rz(yaw)*Ry(pitch)*Rx(roll) body w.r.t. reference frame

            # os.system("cls")
            print("Frame #{}".format(pose.frame_number))
            degree = rpy_rad[2]*180/m.pi
            print("RPY [deg]: {}".format(rpy_rad*180/m.pi))
            
            return degree

    except Exception as e:
        print(f"cam err: {e}")

    finally:
        print("now is on degree")

def main():
    pipe = cam_init()
    for _ in range(5000):
        degree = get_degree(pipe)
        print(degree)
    pipe.stop()

if __name__ == '__main__':

    main()

