import socket
import threading
from cryptography import fernet

obj = fernet.Fernet(fernet.Fernet.generate_key())
terminate_flag = threading.Event()
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
PORT=223
SERVER = socket.gethostbyname(socket.gethostname())
bind = (SERVER,PORT)


def send(msg):
    msg = str(msg)
    target.send(obj.encrypt(msg.encode()))

def recv():
    try:
        while not terminate_flag.is_set():
            msg = target.recv(1024)
            if not msg:
                break
            # if decrypt(msg.decode()) == "quit":
            #     a = decrypt(msg.decode())
            print("\nReceived message: " + obj.decrypt(msg).decode())
    except ConnectionResetError:
        print("Connection reset by peer")
    except ConnectionAbortedError:
        print("Connection aborted, try again")


def connection():
    try:
        send(obj.generate_key())
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