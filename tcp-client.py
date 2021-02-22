import socket

target_host =  "127.0.0.1"
target_port = 9998

#create a socket object
#AF_INET stands for IPv4
#SOCK_STREAM stands for TCP client

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect the client

client.connect((target_host,target_port))

#send some data

client.send(b"some text")

#receive some data

response = client.recv(4096)

if __name__ == '__main__':
	print(response.decode())
	client.close()

