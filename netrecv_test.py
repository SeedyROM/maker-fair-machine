import socket
import time

s = socket.socket(
	socket.AF_INET, socket.SOCK_STREAM
)

s.connect(("localhost", 13000))

try:
	while True:
		message = 'Button1 1;'
		s.sendall(message)
		time.sleep(0.5)
finally:
	s.close()
