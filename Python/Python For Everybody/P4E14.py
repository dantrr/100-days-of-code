# TCP Sockets and Networking with Python

#free book @ www.net-intro.com
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(("data.pr4e.org", 80))