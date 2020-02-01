import socket 

HOST = '127.0.0.1'
PORT = 5050

def server_prog():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(5)


        while True:
            conn, addr = s.accept()
            with conn: 
                print('Connection established by ', addr)
                conn.sendall("SERVER >> Leave a Congratulatory message here. Your message will be posted.".encode())          

                while True: 
                    data = conn.recv(1024)
                    print(data.decode())
                    if not data: 
                        break
            if data.decode() == 'q':
                break

        
    

if __name__ == '__main__':
    server_prog()