# This is the class that will receive the variables and then run the port scan
# NOT READY FOR INTEGRATION
import socket
import time
import threading
from multiprocessing import JoinableQueue

socket.setdefaulttimeout(0.25)
lock = threading.Lock()

# This saves the start time to calculate the speed of tests later on
start = time.time()

def portscan(port):
    sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # This sends the connection request to each port in the queue
    try:
        connection = sckt.connect((target, port))
        with lock:
            print('Port', port, 'is open!')
            print('Time taken:', round(((time.time() - start)/60), 2), ' minutes')
            openPorts.append(port)
        connection.close()
    except:
        pass
    # Notifies the user that the scan is over
    if port == 65500:
        print('Done!')
        print (*openPorts, sep = ", ")
    

def thread():
    while True:
        worker = userQ.get()
        portscan(worker)
        userQ.task_done()

# This sets how many threads you want to run and starts them
for x in range(100):
    t = threading.Thread(target = thread)
    t.daemon = True
    t.start()

# This adds every single port to the Queue
for worker in range(1, 65536):
    userQ.put(worker)

userQ.join()