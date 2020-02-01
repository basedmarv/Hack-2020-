import struct

def recv_msg(socket):
    raw_msglen = recv_all(socket,4)
    if not raw_msglen:
        return None
    msglen = struct.unpack('>I', raw_msglen)[0]
    return recv_all(socket, msglen)

def recv_all(socket, n):
    data = bytearray()
    while len(data) < n:
        packet =  socket.recv(n - len(data))
        if not packet:
            return None
        data.extend(packet)
    return data

def send_msg(socket,msg):
    print('len of message is: ' + str(len(msg)))
    msg = struct.pack('>I', len(msg)) + msg
    socket.sendall(msg)