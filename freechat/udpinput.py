import socket

class UDPInput(object):
	def __init__(self, port:int):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.sock.bind(("0.0.0.0", port))
	
	def getMsg(self):
		data, addr = self.sock.recvfrom(1024)
		user_id = str('{0:x}'.format(int(addr[0].replace(".", ""))))
		
		return [user_id,data.strip().decode()]