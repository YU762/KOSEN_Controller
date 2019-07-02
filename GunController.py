#!/usr/biin/env python

import RPI.GPIO as GPIO
import socket
#import time

HOST = "0.0.0.0"
PORT = 22

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

GPIO.setmode(GPIO.BCM)
GPIO.setup()

#GPIO 8ビンと10ピンの初期化
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
	while True:
		if GPIO.input(8) == GPIO.HIGH:
                        result = str(a)
                        print(result)
                        client.sentto(result.encode('utf-8'),(HOST,PORT))
		
		elif GPIO.input(8) == GPIO.HIGH:
                        result = str(b)
                        print(result)
                        client.sentto(result.encode('utf-8'),(HOST,PORT))
		
		time.sleep(0.1)
		
except KeyboardInterrupt:
	pass
	#例外処理
	
GPIO.cleanup()	
