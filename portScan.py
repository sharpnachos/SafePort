import socket
import time
import threading
from queue import Queue

socket.setdefaulttimeout(0.25)
lock = threading.Lock()

target = '127.0.0.1'
start = time.time()
q = Queue()
openPorts = []

def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        connection = s.connect((target, port))
        with lock:
            print('Port', port, 'is open!')
            print('Time taken:', round(((time.time() - start)/60), 2), ' minutes')
            openPorts.add(port)
        connection.close()
    except:
        pass
    if port == 65536:
        print('Done!')
        for x in range(len(openPorts)):
            print (openPorts[x])
    

def thread():
    while True:
        worker = q.get()
        portscan(worker)
        q.task_done()

for x in range(100):
    t = threading.Thread(target = thread)
    t.daemon = True
    t.start()

for worker in range(1, 65536):
    q.put(worker)

q.join()
