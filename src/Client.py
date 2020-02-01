import socket 

HOST = '127.0.0.1'
PORT = 5050

def client_prog():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        
        data = s.recv(1024)
        print(data.decode())

        msg = input("-> ")

        while msg.lower().strip() != 'bye':
            s.sendall(msg.encode())
            
            msg = input("-> ")

        print("Connection about to be halted.")
        s.close()


if __name__ == '__main__':
    client_prog()