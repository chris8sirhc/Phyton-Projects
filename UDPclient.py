#Christopher Shirley CSCI 379 Networking Project

from socket import *
serverName = "localhost"
serverPort = 12000
import socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print "Christopher Shirley CSCI 379 Networking Project 1\n"
number = raw_input("Input:\n 1 - to Uppercase\n 2 - to Lowercase\n 3 - to Uppercase first letter\n")

while True: 
	if '1' in number:
		message = raw_input("Input lowercase sentence:\n")
		combo = number + message
		clientSocket.sendto(combo, (serverName, serverPort)) 
		modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
		print modifiedMessage.strip('1')
	elif '2' in number: 
		message = raw_input("Input uppercase sentence:\n")
		combo = number + message
		clientSocket.sendto(combo, (serverName, serverPort)) 
		modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
		print modifiedMessage.strip('2')
	elif '3' in number:
		message = raw_input("Input sentence:\n")
		combo = number + message
		clientSocket.sendto(combo, (serverName, serverPort)) 
		modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
		print modifiedMessage.strip('3')
	else:
		print("INVALID INPUT")
		break
		
clientSocket.close()
	