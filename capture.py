#! /usr/bin/env python

from utils.conf import sustainable_sim as ss
import os
import pygame
import pygame.camera

filename = ss['filename']
username = ss['server']['username']
ip_address = ss['server']['ip_address']
path = "{}/{}".format(ss['server']['photo_path'], filename)

pygame.camera.init()
camera_list = pygame.camera.list_cameras()
camera_name = camera_list[0]
cam = pygame.camera.Camera(camera_name, (2048, 1620))
cam.start()
img = cam.get_image()
pygame.image.save(img, filename)
cam.stop()

os.system("scp {} {}@{}:{}".format(filename, username, ip_address, path))
