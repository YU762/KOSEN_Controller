#!/usr/biin/env python

import RPI.GPIO as GPIO
#import time

GPIO.setmode(GPIO.BCM)
GPIO.setup()

GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
	while True:
		if GPIO.input(8) == GPIO.HIGH:
		
			#Nodeに渡す処理
		
		elif GPIO.input(8) == GPIO.HIGH:
		
			##Nodeに渡す処理
		
		#time.sleepp(0.1)
		
except KeyboardInterrupt:
	pass
	#例外処理
	
GPIO.cleanup()	