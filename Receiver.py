import socket
import threading
from cryptography import fernet

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip = input("Input ip address of host ")
port=223
terminate_flag = threading.Event()
encryption_key = ""

def send(msg):
    obj = fernet.Fernet(encryption_key)
    msg = str(msg)
    s.send(obj.encrypt(msg.encode()))

def recv():
    obj = fernet.Fernet(encryption_key)
    try:
        while not terminate_flag.is_set():
            msg = s.recv(1024)
            if not msg:
                break
            # if decrypt(msg.decode()) == "quit":
            #     return decrypt(msg.decode())
            print("\nReceived message: " + obj.decrypt(msg))
    except ConnectionResetError:
        print("Connection reset by peer")


def connection():
    try:
        encryption_key = s.recv(1024).decode()
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

s.connect((ip,port))
connection()