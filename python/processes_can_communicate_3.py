import socket

if __name__ == "__main__":
    sockets = socket.socketpair(socket.AF_UNIX, socket.SOCK_DGRAM, 0)
    print "Paired sockets:", sockets
