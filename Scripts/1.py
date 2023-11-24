#!/usr/bin/env python3 

import subprocess
import time

def load_v4l2loopback_module():
    try:
        subprocess.run(["sudo", "modprobe", "v4l2loopback"], check=True)
        print("v4l2loopback module loaded successfully.")
    except subprocess.CalledProcessError as e:
        print("Error loading v4l2loopback module:", e)

def unload_v4l2loopback_module():
    try:
        subprocess.run(["sudo", "modprobe", "-r", "v4l2loopback"], check=True)
        print("v4l2loopback module unloaded successfully.")
    except subprocess.CalledProcessError as e:
        print("Error unloading v4l2loopback module:", e)

def set_virtual_camera(video_file):
    try:
        subprocess.run(["ffmpeg", "-re", "-i", video_file, "-f", "v4l2", "/dev/video0"], check=True)
        print("Virtual camera set to:", video_file)
    except subprocess.CalledProcessError as e:
        print("Error setting virtual camera:", e)

if __name__ == "__main__":
    video_file_path = "/home/juba/Videos/suit.mp4"

    # Load v4l2loopback module
    load_v4l2loopback_module()

    # Set the virtual camera to the prerecorded video
    set_virtual_camera(video_file_path)

    try:
        # Keep the script running to maintain the virtual camera
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        # Unload v4l2loopback module when script is interrupted
        unload_v4l2loopback_module()


