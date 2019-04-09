# This class will take information on what scan the user wants to perform and then will make a scan according to those specifications and pass the variable to portScan which will carry out the scan
# NOT READY FOR INTEGRATION
def main():
    ip = '127.0.0.1'
    userQ = JoinableQueue()
    threads = 100
    smartRange = [0, 21, 22, 23, 25, 53, 79, 80, 110, 113, 119, 135, 137, 138, 139, 143, 389, 443, 445, 555, 631, 666, 902, 912, 1001, 1002, 1024, 1025, 1026, 1027, 1028, 1029, 1030, 1243, 1433, 1434, 1720, 1900, 2000, 4380, 4381, 5000, 5040, 5088, 5354, 5432, 6463, 6667, 6670, 6711, 6776, 6969, 7000, 7680, 8080, 8733, 12345, 12346, 13148, 15292, 15393, 21554, 22222, 27015, 27017, 27275 , 27374, 29559, 31337, 31338, 49664, 49665, 49666, 49668, 49684, 49731, 49765, 49774, 50698, 50760, 51229, 54860, 54870, 57621]
    answer = str(input(print('What kind of scan would you like to do? (full, smart, or advanced): ')))
    if answer == 'full':
        for worker in range(0, 65536):
            userQ.put(worker)
        makeScan(ip, userQ, threads)
    elif answer == 'smart':
        for worker in smartRange:
            userQ.put(worker)
        makeScan(ip, userQ, threads)
    elif answer == 'advanced':
        ip = input(print('What IP address woyuld you like to scan?: '))
        for worker in range(0, 655365):
            userQ.put(worker)
        threads = str(input(print('How many threads would you like to use? (The default is 100): ')))
        makeScan(ip, userQ, threads)
    else:
        answer = str(input(print("I'm sorry, we do not have a response for that command yet. Try typing 'smart', 'full', or 'advanced': ")))
    def makeScan(ip, userQ, threads):
        scan = scanOption(ip, userQ, threads)
    portScan(scan)

class scanOption:
    #Sets the default just in case something goes wrong
    ip = "127.0.0.1"
    userQ = JoinableQueue()
    for num in range(0, 655365):
        userQ.put(num)
    threads = 100

    # The class "constructor" - It's actually an initializer 
    def __init__(self, ip, userQ, threads):
        self.ip = ip
        self.userQ = userQ
        self.threads = threads
    
    def getip():
        return ip
    
    def geruserQ():
        return userQ
    
    def getthreads():
        return threads

    def changeip(ip1):
        ip = ip1
        print ('The IP Address was changed to ', ip, '!')

    def changeuserQ(userQ1):
        userQ = userQ1
        print ('The scanning range was changed!')
    
    def changethreads(threads1):
        threads = threads1
        print ('The number of threads has been changed to ', threads, '!')

class portScan(object):
    ip = scanOption.getip()
    userQ = scanOption.getuserQ()
    threads = scanOption.getthreads()

    