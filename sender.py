import socket
import threading

terminate_flag = threading.Event()
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
PORT=223
SERVER = socket.gethostbyname(socket.gethostname())
bind = (SERVER,PORT)


def send(msg):
    msg = str(msg)
    ms = encrypt(msg)
    target.send(ms.encode())

def recv():
    try:
        while not terminate_flag.is_set():
            msg = target.recv(1024)
            if not msg:
                break
            # if decrypt(msg.decode()) == "quit":
            #     a = decrypt(msg.decode())
            print("\nReceived message: " + decrypt(msg.decode()))
    except ConnectionResetError:
        print("Connection reset by peer")
    except ConnectionAbortedError:
        print("Connection aborted, try again")

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
    try:
        rec = threading.Thread(target=recv)
        rec.start()
        while True:
            msg = input("Enter your message: ")
            # if msg == "quit":
            #     send(msg)
            #     print("You exitted the program")
            #     terminate_flag.set()
            #     break
            send(msg)
    except Exception as e:
        print(f"An unexpected error occured: {e}")
    finally:
        s.close()
        target.close()
    

s.bind(bind)
s.listen(5)
target,ip = s.accept()
print("Connected to ",ip)
connection()