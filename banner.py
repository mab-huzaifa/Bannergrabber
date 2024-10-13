#!/bin/python3


import socket
import sys

if len(sys.argv) <= 2:
	print(f"USAGE: {sys.argv[0]} <ipaddr> <port>")
	exit(0)

TCPIP = sys.argv[1]
TCPPORT = int(sys.argv[2])
BUFF = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	sock.connect((TCPIP, TCPPORT))
	banner = sock.recv(BUFF)
	print(f"{TCPIP}:{TCPPORT} --> ", banner)
except ConnectionRefusedError:
	pass
finally:
	sock.close()
