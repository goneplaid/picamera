import picamera
from time import sleep

camera = picamera.PiCamera()
camera.capture('image.jpg')

camera.start_preview()
camera.hflip = True
camera.brightness = 60

camera.start_recording('video.h264')
sleep(120)
camera.stop_recording()
