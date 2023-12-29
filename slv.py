import socket
#import asyncio

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port=223

def send(msg):
    msg = str(msg)
    ms = encrypt(msg)
    target.send(ms.encode())

def recv():
    while True:
        try:
            msg = target.recv(1024)
            print(decrypt(msg.decode()))
        except:
            continue

def encrypt(data):
    data = str(data)
    enc = ""
    for i in data:
        if i.isspace():
            enc += i
        if ord(i) < 14:
            new = ord(i) + 13
            enc += chr(new)
        else:
            new = ord(i) - 13
            enc += chr(new)
    return enc

def decrypt(data):
    data = str(data)
    enc = ""
    for i in data:
        if i.isspace():
            enc += i
        elif ord(i) < 14:
            new = ord(i) - 13
            enc += chr(new)
        else:
            new = ord(i) + 13
            enc += chr(new)
    return enc


def connection():
    while True:
        msg = input("")
        if msg == "quit":
            break
        else:
            send(encrypt(msg))
            recv()

s.bind(("192.168.0.160",223))
s.listen(5)
target,ip = s.accept()
print("Connected to ",target)
connection()