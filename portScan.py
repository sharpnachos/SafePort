import socket
import time
import threading
from queue import Queue

socket.setdefaulttimeout(0.25)
lock = threading.Lock()

# This sets the IP that we are scanning to the IP of the device running this code
target = '127.0.0.1'
# This saves the start time to calculate the speed of tests later on
start = time.time()
# Creates a queue to be used for the complete scan
q = Queue()
# TODO: This creates a queue for the Smart Scan feature I want to implement
sq = Queue()
# This makes a list for which we are going to use to keep track of the open ports
openPorts = []

def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # This sends the connection request to each port in the queue
    try:
        connection = s.connect((target, port))
        with lock:
            print('Port', port, 'is open!')
            print('Time taken:', round(((time.time() - start)/60), 2), ' minutes')
            openPorts.add(port)
        connection.close()
    except:
        pass
    # Notifies the user that the scan is over
    if port == 65536:
        print('Done!')
        for x in range(len(openPorts)):
            print (openPorts[x])
    

def thread():
    while True:
        worker = q.get()
        portscan(worker)
        q.task_done()

# This sets how many threads you want to run and starts them
for x in range(100):
    t = threading.Thread(target = thread)
    t.daemon = True
    t.start()

# This adds every single port to the Queue
for worker in range(1, 65536):
    q.put(worker)

q.join()