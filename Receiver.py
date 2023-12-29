import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip = input("Input ip address ")
port=223

def recv():
    while True:
        try:
            msg = s.recv(1024)
            print(decrypt(msg.decode()))
            snd = input("")
            if snd == "quit":
                break
            else:
                send(snd)
        except:
            continue

def encrypt(data):
    data = str(data)
    enc = ""
    for i in data:
        if i.isspace():
            enc += i
        elif ord(i) < 14:
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
    


def send(msg):
    msg = str(msg)
    ms = encrypt(msg)
    s.send(ms.encode())

def connect():
    while True:
        recv()

s.connect((ip,port))
connect()