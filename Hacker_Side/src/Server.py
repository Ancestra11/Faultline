import socket
import time
import os

class Server() :

	def __init__(self) :
		IP = '0.0.0.0'
		Port = 1002
		self.Count = 1
		self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server.bind((IP, Port))
		self.server.listen()
		self.client_socket, self.client_address = self.server.accept()

	def receive_image(self) :

		# Receives the size of the file before receiving the image
		FileSize = self.client_socket.recv(7).decode("utf-8")
		print("FileSize : ", FileSize)

		# Verify existing files and modify the name of the incoming one if necessary.
		FilePath = '../data/Screenshots/image' + str(self.Count) + '.bmp'
		while os.path.exists(FilePath) == True :
			self.Count += 1
			FilePath = '../data/Screenshots/image' + str(self.Count) + '.bmp'

		# Write incoming image to 'FilePath' location
		self.file = open(FilePath, 'wb')
		image_chunk = self.client_socket.recv(2048)

		while image_chunk :
			self.file.write(image_chunk)
			image_chunk = self.client_socket.recv(2048)

			# Stops when the size of written image is good enough
			if os.path.getsize(FilePath) >= int(FileSize) :
				self.file.close()
				break

		print("SORTIE DE WHILE")
		print(self.Count)

		# Avoid writting endless files if target crashes
		if os.path.getsize(FilePath) < 2920 :
			self.Count -= 1

	def Thread(self) :
		threading.Thread(target=receive_image)

SRV = Server()
SRV.receive_image()

#receive_image(Count)
#client_socket.close()