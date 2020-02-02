import socket 
import sys
import traceback
import threading

HOST = '127.0.0.1'
PORT = 5050

def server_prog():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print("Socket creation is finished")

    try:
        s.bind((HOST,PORT))
    except:
        print("Binding failed. Error: " + str(sys.exc_info()))
        sys.exit()

    s.listen(6)
    print("Socket now listening")

    while True: 
        conn, addr = s.accept()
        ip, port = str(addr[0]), str(addr[1])
        # print("Connected with " + ip + ":" + port)
        conn.sendall("SERVER >> Leave a Congratulatory message here. Your message will be posted.".encode())          
        print("Message Server sent to new Client")

        threading.Thread(target=clientThread, args=(conn, ip, port)).start()

    
    # try:
    #     print("Establishing thread")
    #     Thread(target=client_thread, args=(connection, ip, port)).start()
    # except: 
    #     print("Thread not established.")
    #     traceback.print_exc()  

    # s.close() 

def clientThread(connection, ip, port, max_buffer_size = 5120):
   # print("Entered clientThread")
   is_active = True
   while is_active:
      client_input = receive_input(connection, max_buffer_size)
      if "--QUIT--" in client_input:
         print("Client is requesting to quit")
         connection.close()
         print("Connection " + ip + ":" + port + " closed")
         is_active = False
      else:
         print("{}".format(client_input))
         connection.sendall("-".encode("utf8"))

def receive_input(connection, max_buffer_size):
   client_input = connection.recv(max_buffer_size)
   client_input_size = sys.getsizeof(client_input)
   if client_input_size > max_buffer_size:
      print("The input size is greater than expected {}".format(client_input_size))
   decoded_input = client_input.decode("utf8").rstrip()
   result = process_input(decoded_input)
   return result

def process_input(input_str):
   # print("Processing the input received from client")
   # return "Hello " + str(input_str).upper()
   return "Message received!"
        
# def server_prog():
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#         s.bind((HOST, PORT))
#         s.listen(5)


#         while True:
#             conn, addr = s.accept()
#             with conn: 
#                 print('Connection established by ', addr)
#                 conn.sendall("SERVER >> Leave a Congratulatory message here. Your message will be posted.".encode())          

#                 while True: 
#                     data = conn.recv(1024)
#                     print(data.decode())
#                     if not data: 
#                         break
#             if data.decode() == 'q':
#                 break

        
    

if __name__ == '__main__':
    server_prog()