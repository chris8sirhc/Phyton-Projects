#Christopher Shirley CSCI 379 Networking Project

from socket import *
serverPort = 12000
import socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print "Christopher Shirley CSCI 379 Networking Project 1\n"
print "The server is ready to receive:"

while True:
	combo, clientAddress = serverSocket.recvfrom(2048)
	if '1' in combo:
		modifiedMessage = combo.upper()
		serverSocket.sendto(modifiedMessage, clientAddress) 
	elif '2' in combo:
		modifiedMessage = combo.lower()
		serverSocket.sendto(modifiedMessage, clientAddress) 
	elif '3' in combo:
		modifiedMessage = combo.title()
		serverSocket.sendto(modifiedMessage, clientAddress) 
	else:
		print("INVALID INPUT")
		break
		 