from lightFunctions import readIntensity as ri




from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
sleep(10)
camera.capture('./naKAL_blye.jpg')

camera.stop_preview()
