import socket
import time
import RPi.GPIO as GPIO

# Setup out TCP/IP socket
s = socket.socket(
	socket.AF_INET, socket.SOCK_STREAM
)
s.connect(("localhost", 13000))

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN)

# Generic button interrupt
def edge_interrupt(socket, button_num):
	def interrupt(channel):
		if not GPIO.input(channel):
			socket.sendall('Button'+ str(button_num) +' 1;')
		else:
			socket.sendall('Button'+ str(button_num) +' 0;')
	return interrupt
	
# Find edges
GPIO.add_event_detect(26, GPIO.BOTH, callback=edge_interrupt(s, 1))

try:
	while True:
		#if not wiringpi.digitalRead(26):
			#message = 'Button1 1;'
			#s.sendall(message)
		#else:
			#message = 'Button1 0;'
			#s.sendall(message)
			
		time.sleep(0.05)
finally:
	s.close()
