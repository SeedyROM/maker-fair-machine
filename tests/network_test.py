import socket
import time
import RPi.GPIO as GPIO

# Generic button interrupt
def edge_interrupt(socket, button_num):
	def interrupt(channel):
		if not GPIO.input(channel):
			print 'Button%d pressed' % button_num
			socket.sendall('Button'+ str(button_num) +' 1;')
		else:
			print 'Button%d released' % button_num
			socket.sendall('Button'+ str(button_num) +' 0;')
	return interrupt

# Machine class to store socket and button states
class ButtonMachine:
	def __init__(self, port):
		self.pins = [(21, 1)]
		
		# Initialize our interface
		self.setup_socket(port)
		self.setup_gpio()
		self.setup_interrupts()
		
	def setup_socket(self, port):
		self.socket = socket.socket(
			socket.AF_INET, socket.SOCK_STREAM
		)
		self.socket.connect(("localhost", port))
		
	def setup_gpio(self):
		GPIO.setmode(GPIO.BCM)

		for pin, _ in self.pins:
			GPIO.setup(pin, GPIO.IN)
		
	def setup_interrupts(self):
		for pin, num in self.pins:
			GPIO.add_event_detect(
				pin,
				GPIO.BOTH,
				callback=edge_interrupt(self.socket, num),
			)
	
	def clean_up(self):
		self.socket.close()

button_machine = ButtonMachine(13000)
try:
	while True:			
		time.sleep(0.005)
finally:
	button_machine.clean_up()
