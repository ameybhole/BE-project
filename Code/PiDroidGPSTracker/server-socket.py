#server script
import socket
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(("192.168.1.7",12345))
sock.listen(2)
(client,(ip,port))=sock.accept()

while True:
	gpsdata = client.recv(1204)
	file = open("file2","w")
	file.write(gpsdata)
	file.close()
