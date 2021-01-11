##!/usr/bin/env python3
import time
from rpi_ws281x import *
import argparse
import os.path
import pwd
import psi
import psi.process
import telebot
bot = telebot.TeleBot("telegram bot token here")
 
LED_COUNT	= 1	 # Number of LED pixels.
LED_PIN		= 18	  # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ	= 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA		= 10	  # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255	 # Set to 0 for darkest and 255 for brightest
LED_INVERT	 = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL	= 0	   # set to '1' for GPIOs 13, 19, 41, 45 or 53
 
 
def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)
def colorWipe(strip, color, wait_ms=50):
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, color)
		strip.show()
		time.sleep(wait_ms/1000.0)

def wipe(strip, wait_ms=50):
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, Color(0,0,0))
		strip.show()
def start(strip, wait_ms=20, iterations=4):
	for j in range(256*iterations):
		for i in range(strip.numPixels()):
			strip.setPixelColor(i, wheel((i+j) & 255))
		strip.show()
		time.sleep(wait_ms/1000.0)
def startold(strip, wait_ms=3):
	for i in range(strip.numPixels()):
		for z in range(255):
			strip.setPixelColor(i, Color(z,z,z))
			strip.show()
			time.sleep(wait_ms/1000)
		for z in reversed(range(255)):
			strip.setPixelColor(i, Color(z,z,255))
			strip.show()
			time.sleep(wait_ms/1000)
		for z in range(255):
			strip.setPixelColor(i, Color(z,z,255))
			strip.show()
			time.sleep(wait_ms/1000)
		for z in reversed(range(255)):
			strip.setPixelColor(i, Color(z,z,z))
			strip.show()
			time.sleep(wait_ms/1000)
		for z in range(255):
			strip.setPixelColor(i, Color(z,z,z))
			strip.show()
			time.sleep(wait_ms/1000)
		for z in reversed(range(255)):
			strip.setPixelColor(i, Color(z,z,255))
			strip.show()
			time.sleep(wait_ms/1000)
		for z in range(255):
			strip.setPixelColor(i, Color(z,z,255))
			strip.show()
			time.sleep(wait_ms/1000)
		for z in reversed(range(255)):
			strip.setPixelColor(i, Color(z,z,z))
			strip.show()
			time.sleep(wait_ms/1000)
		for z in range(255):
			strip.setPixelColor(i, Color(z,z,255))
			strip.show()
			time.sleep(wait_ms/1000)
		for z in reversed(range(255)):
			strip.setPixelColor(i, Color(z,z,z))
			strip.show()
			time.sleep(wait_ms/1000)
		for z in range(255):
			strip.setPixelColor(i, Color(z,z,255))
			strip.show()
			time.sleep(wait_ms/1000)
		for z in reversed(range(255)):
			strip.setPixelColor(i, Color(z,z,z))
			strip.show()
			time.sleep(wait_ms/1000)
def discord(strip, wait_ms=3):
	for i in range(strip.numPixels()):
		for z in range(255):
			strip.setPixelColor(i, Color(z,0,z))
			strip.show()
			time.sleep(wait_ms/1000)
		for z in reversed(range(255)):
			strip.setPixelColor(i, Color(z,0,z))
			strip.show()
			time.sleep(wait_ms/1000)
		for z in range(255):
			strip.setPixelColor(i, Color(z,0,0))
			strip.show()
			time.sleep(wait_ms/1000)
		for z in reversed(range(255)):
			strip.setPixelColor(i, Color(z,0,0))
			strip.show()
			time.sleep(wait_ms/1000)			
def drive(strip, wait_ms=3):
	for i in range(strip.numPixels()):
		for z in range(255):
			strip.setPixelColor(i, Color(z,z,z))
			strip.show()
			time.sleep(wait_ms/1000)
		for z in reversed(range(255)):
			strip.setPixelColor(i, Color(z,z,z))
			strip.show()
			time.sleep(wait_ms/1000)
		for z in range(255):
			strip.setPixelColor(i, Color(z,0,0))
			strip.show()
			time.sleep(wait_ms/1000)
		for z in reversed(range(255)):
			strip.setPixelColor(i, Color(z,0,0))
			strip.show()
			time.sleep(wait_ms/1000)
def vkbot(strip, wait_ms=3):
	for i in range(strip.numPixels()):
		for z in range(255):
			strip.setPixelColor(i, Color(0,z,z))
			strip.show()
			time.sleep(wait_ms/1000)
		for z in reversed(range(255)):
			strip.setPixelColor(i, Color(0,z,z))
			strip.show()
			time.sleep(wait_ms/1000)
		for z in range(255):
			strip.setPixelColor(i, Color(z,0,0))
			strip.show()
			time.sleep(wait_ms/1000)
		for z in reversed(range(255)):
			strip.setPixelColor(i, Color(z,0,0))
			strip.show()
			time.sleep(wait_ms/1000)
def telegram(strip, wait_ms=3):
	for i in range(strip.numPixels()):
		for z in range(255):
			strip.setPixelColor(i, Color(0,0,z))
			strip.show()
			time.sleep(wait_ms/1000)
		for z in reversed(range(255)):
			strip.setPixelColor(i, Color(0,0,z))
			strip.show()
			time.sleep(wait_ms/1000)
		for z in range(255):
			strip.setPixelColor(i, Color(z,0,0))
			strip.show()
			time.sleep(wait_ms/1000)
		for z in reversed(range(255)):
			strip.setPixelColor(i, Color(z,0,0))
			strip.show()
			time.sleep(wait_ms/1000)
def driveone(strip, wait_ms=3):
	for i in range(strip.numPixels()):
		for z in range(255):
			strip.setPixelColor(i, Color(z,z,z))
			strip.show()
			time.sleep(wait_ms/1000)
		for z in reversed(range(255)):
			strip.setPixelColor(i, Color(z,z,z))
			strip.show()
			time.sleep(wait_ms/1000)
		for z in range(255):
			strip.setPixelColor(i, Color(0,z,z))
			strip.show()
			time.sleep(1/1000)
		for z in reversed(range(255)):
			strip.setPixelColor(i, Color(0,z,z))
			strip.show()
			time.sleep(1/1000)
		for z in range(255):
			strip.setPixelColor(i, Color(z,0,0))
			strip.show()
			time.sleep(wait_ms/1000)
		for z in reversed(range(255)):
			strip.setPixelColor(i, Color(z,0,0))
			strip.show()
			time.sleep(wait_ms/1000)


def ok(strip,wait_ms=1):
	for i in range(strip.numPixels()):
		for z in range(155):
			strip.setPixelColor(i, Color(z,z,z))
			strip.show()
			time.sleep(wait_ms/1000)
		for z in reversed(range(155)):
			strip.setPixelColor(i, Color(z,z,z))
			strip.show()
			time.sleep(wait_ms/1000)

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
	args = parser.parse_args()
 
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
	strip.begin()
	try:
		re = 0
		start(strip)
		bot.send_message(895942747,"Сервер запущен!")
		wipe(strip)
		time.sleep(3)
		while True:

			if os.path.isfile("/drive/checkfile") is True:
				re = re+1
				drive = "ok"
			if os.path.isfile("/driveone/checkfile") is True:
				re = re+1
				driveone = "ok"
			myProcessName="besed.py" 
			for p in psi.process.ProcessTable().values():
				if myProcessName in p.command:
					re = re+1
					vkbot = "ok"
	
			myProcessName="run.py" 
			for p in psi.process.ProcessTable().values():
				if myProcessName in p.command:
					re = re+1
					discord = "ok"
	
			myProcessName="tel.py" 
			for p in psi.process.ProcessTable().values():
				if myProcessName in p.command:
					re = re+1
					telegram = "ok"
	
			if vkbot != "ok":
				vkbot(strip)
				bot.send_message(895942747,"Не работает вк бот")
				time.sleep(300)
			if telegram != "ok":
				telegram(strip)
				bot.send_message(895942747,"Не работает TG бот")
				time.sleep(300)
			if discord != "ok":
				discord(strip)
				bot.send_message(895942747,"Не работает дискорд бот")
				time.sleep(300)
			if drive != "ok":
				drive(strip)
				bot.send_message(895942747,"Не работает запасной диск (/drive)")
				time.sleep(300)
			if driveone != "ok":
				drive(strip)
				bot.send_message(895942747,"Не работает главный диск (/driveone)")
				time.sleep(300)

			if re == 5:
				ok(strip)
			re = 0
			time.sleep(180)
	
	except KeyboardInterrupt:
		if args.clear:
			colorWipe(strip, Color(0,0,0), 10)
