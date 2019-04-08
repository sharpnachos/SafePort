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

# Creates a queue to be used for the complete scan
fullQ = JoinableQueue()
# This creates a queue for the Smart Scan feature I want to implement
smartQ = JoinableQueue()
# This makes a queue that can be changed to smart or full depending on the users needs
userQ = JoinableQueue()
# This makes a list for which we are going to use to keep track of the open ports
openPorts = []
# This adds every single port to the Queue
for worker in range(1, 65536):
    fullQ.put(worker)
# This creates the smartQ range
# TODO: Change this so it reads from a text file
smartQrange = [0, 21, 22, 23, 25, 53, 79, 80, 110, 113, 119, 135, 137, 138, 139, 143, 389, 443, 445, 555, 631, 666, 902, 912, 1001, 1002, 1024, 1025, 1026, 1027, 1028, 1029, 1030, 1243, 1433, 1434, 1720, 1900, 2000, 4380, 4381, 5000, 5040, 5088, 5354, 5432, 6463, 6667, 6670, 6711, 6776, 6969, 7000, 7680, 8080, 8733, 12345, 12346, 13148, 15292, 15393, 21554, 22222, 27015, 27017, 27275 , 27374, 29559, 31337, 31338, 49664, 49665, 49666, 49668, 49684, 49731, 49765, 49774, 50698, 50760, 51229, 54860, 54870, 57621]
for worker in smartQrange:
    smartQ.put(worker)

def main():

    answer = str(input(print("Would you like a 'full' scan or a 'smart' scan? ")))
    if answer == 'full':
        userQ = fullQ
    elif answer == 'smart':
        userQ = smartQ
    else:
        input = input(print("I'm sorry, I don't understand that answer, try typing 'full' or 'smart': "))
    
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
    fullQ.put(worker)

userQ.join()