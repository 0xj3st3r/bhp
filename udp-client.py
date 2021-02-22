import socket

target_host =  "127.0.0.1"
target_port = 9997

#create a socket object
#AF_INET stands for IPv4
#SOCK_DGRAM stands for UDP client

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#send some data

client.sendto(b"AAABBBCCC",(target_host,target_port))

#receive some data

data, addr = client.recvfrom(4096)

if __name__ == '__main__':
	print(data.decode())
	client.close()

