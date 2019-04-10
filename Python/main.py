# This class will ask the user for the type of scan they want to perform and then will edit the variables to fit the needs of the user
# NOT READY FOR INTEGRATION

# I'm using JoinableQueue because some computers have a hard time dealing with a regular queue and this seems to fix the problem
from multiprocessing import JoinableQueue
# These imports are for the actual port scanning functions: Socket is how we make connections and threading is the amount of ports that can be tested at a time
import socket
import threading
# This is mostly for developer purposes as to see how fast the scan takes to complete
import time

# This declares the public variables that will be used for the portscan, the variables are instantiated as a full scan default for now, might change the default to smart scan
target = '127.0.0.1'
userQ = JoinableQueue()
threads = 100

def main():
    smartRange = [0, 21, 22, 23, 25, 53, 79, 80, 110, 113, 119, 135, 137, 138, 139, 143, 389, 443, 445, 555, 631, 666, 902, 912, 1001, 1002, 1024, 1025, 1026, 1027, 1028, 1029, 1030, 1243, 1433, 1434, 1720, 1900, 2000, 4380, 4381, 5000, 5040, 5088, 5354, 5432, 6463, 6667, 6670, 6711, 6776, 6969, 7000, 7680, 8080, 8733, 12345, 12346, 13148, 15292, 15393, 21554, 22222, 27015, 27017, 27275 , 27374, 29559, 31337, 31338, 49664, 49665, 49666, 49668, 49684, 49731, 49765, 49774, 50698, 50760, 51229, 54860, 54870, 57621]
    answer = str(input('What kind of scan would you like to do? (full, smart, or custom): '))
    if answer == 'full':
        for worker in range(0, 65536):
            userQ.put(worker)
    elif answer == 'smart':
        for worker in smartRange:
            userQ.put(worker)
    elif answer == 'custom':
        target = input('What target address would you like to scan? (ip or URL): ')
        for worker in range(0, 655365):
            userQ.put(worker)
        threads = str(input('How many threads would you like to use? (The default is 100): '))
    else:
        answer = str(input("I'm sorry, we do not have a response for that command yet. Try typing 'smart', 'full', or 'advanced': "))

main()

socket.setdefaulttimeout(0.25)
lock = threading.Lock()

# This saves the start time to calculate the speed of tests later on
start = time.time()

# This makes a list in which we will store the ports that were found to be open
openPorts = []

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