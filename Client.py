import socket 
import sys 

HOST = '127.0.0.1'
PORT = 5050

def client_prog():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST, PORT))
        except: 
            print("Connection Error")
            sys.exit()
        
        server_msg = s.recv(1024)
        print(server_msg.decode())

        print("Please enter 'quit' when you are done.")
        msg = input("-> ")
        
        while msg.lower().strip() != 'quit':
            s.sendall(msg.encode("utf8"))
            # if s.recv(5120).decode("utf8") == "-":
                 # pass # null operation
            msg = input("-> ")

        print("Connection about to be halted.")
        s.send(b'--quit--')

        # data = s.recv(1024)
        # print(data.decode())

        # msg = input("-> ")

        # while msg.lower().strip() != 'bye':
        #     s.sendall(msg.encode())
            
        #     msg = input("-> ")

        # print("Connection about to be halted.")
        # s.close()


if __name__ == '__main__':
    client_prog()