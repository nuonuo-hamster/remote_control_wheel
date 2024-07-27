import pyrealsense2 as rs
import numpy as np
import transformations as tf
import math as m
import os 

H_aeroRef_T265Ref = np.array([[0,0,-1,0],[1,0,0,0],[0,-1,0,0],[0,0,0,1]])
H_T265body_aeroBody = np.linalg.inv(H_aeroRef_T265Ref)

def cam_init():
   
    pipe = rs.pipeline()
    cfg = rs.config()
    cfg.enable_stream(rs.stream.pose)
    pipe.start(cfg)

    return pipe

def cam_close(pipe):
   
    pipe.stop()

def get_degree(pipe):
      
    frames = pipe.wait_for_frames()
    pose = frames.get_pose_frame()
    
    if pose:
        data = pose.get_pose_data()

        H_T265Ref_T265body = tf.quaternion_matrix([data.rotation.w, data.rotation.x,data.rotation.y,data.rotation.z]) # in transformations, Quaternions w+ix+jy+kz are represented as [w, x, y, z]!
        H_aeroRef_aeroBody = H_aeroRef_T265Ref.dot( H_T265Ref_T265body.dot(H_T265body_aeroBody))
        rpy_rad = np.array( tf.euler_from_matrix(H_aeroRef_aeroBody, 'sxyz') ) # Rz(yaw)*Ry(pitch)*Rx(roll) body w.r.t. reference frame

        print("Frame #{}".format(pose.frame_number))
        print("Axis [xyz]: {}".format(H_T265Ref_T265body))
        print("RPY [deg]: {}".format(rpy_rad*180/m.pi))

        degree = rpy_rad[2]*180/m.pi
        return degree

def main():
    pipe = cam_init()

    for _ in range(5000):

        try:
            degree = get_degree(pipe)
        except Exception as e:
             print(f"cam err: {e}")

        # print(degree)

    cam_close(pipe)

if __name__ == '__main__':

    main()