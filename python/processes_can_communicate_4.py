import os
import socket

child_socket, parent_socket = socket.socketpair(socket.AF_UNIX,
                                                socket.SOCK_DGRAM, 0)
maxlen = 1000

if __name__ == "__main__":
    pid = os.fork()
    if pid == 0:
        parent_socket.close()

        for _ in range(4):
            instruction = child_socket.recv(maxlen)
            child_socket.send("%s accomplished!" % instruction)
    else:
        child_socket.close()

        for _ in range(2):
            parent_socket.send("Heavy lifting", 0)

        for _ in range(2):
            parent_socket.send("Feather lifting", 0)

        for _ in range(4):
            print parent_socket.recv(maxlen)
