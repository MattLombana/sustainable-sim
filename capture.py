#! /usr/bin/env python

from utils.conf import sustainable_sim as ss
import os
import pygame
import pygame.camera

username = ss['server']['username']
ip_address = ss['server']['ip_address']
path = "{}/{}".format(ss['server']['photo_path'], filename)




def start_camera():
    """Creates, starts, and returns a camera object"""
    pygame.camera.init()
    camera_list = pygame.camera.list_cameras()
    camera_name = camera_list[0]
    cam = pygame.camera.Camera(camera_name, (2048, 1620))
    cam.start()
    return cam

def take_photo(camera, filename):
    """Takes a photo, and uploads it to a remote server
    Parameters:
        camera: a camera object
    """
    img = camera.get_image()
    pygame.image.save(img, filename)
    os.system("scp {} {}@{}:{}".format(filename, username, ip_address, path))
    os.remove(filename)


def stop_camera(camera):
    """ Stops the camera.
    Parameters:
        camera: a camera object
    """
    camera.stop()
