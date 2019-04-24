import socket
import time
import threading
from multiprocessing import JoinableQueue

socket.setdefaulttimeout(0.25)
lock = threading.Lock()

# This sets the IP that we are scanning to the IP of the device running this code
target = '127.0.0.1'
# This saves the start time to calculate the speed of tests later on
start = time.time()
# This creates a queue for the Smart Scan feature I want to implement
sq = JoinableQueue()
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
            openPorts.append(port)
        connection.close()
    except:
        pass
    # Notifies the user that the scan is over
    if port == 65535:
        time.sleep(0.5)
        message = '<h4>Open ports on your device:</h4><br/>'
        results = ', '.join(str(x) for x in openPorts)
        print (message + results + '<br/><br/><br/><i class="fas fa-search fa-md"></i>&nbsp; Scan Type: <i>Custom Scan</i>')
        return results


def thread():
    while True:
        worker = sq.get()
        portscan(worker)
        sq.task_done()

# This sets how many threads you want to run and starts them
for x in range(100):
    t = threading.Thread(target = thread)
    t.daemon = True
    t.start()

for worker in range(0, 65535):
    sq.put(worker)

sq.join()
