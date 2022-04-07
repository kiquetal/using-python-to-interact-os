import socket

def check_localhost():
    localhost = socket.gethostbyname('localhost')
    return localhost == '127.0.0.1'
