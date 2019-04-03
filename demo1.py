import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

target = '127.0.0.1'

def scan(port):
    try:
        connect = socket.connect((target, port))
        return True
    except:
        return False

customRange = [130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140]

for x in customRange:
    if scan(x):
        print('Port', x, 'is open')
    else:
        print('Port', x, 'is closed')