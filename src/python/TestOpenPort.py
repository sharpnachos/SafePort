#TestOpenPort

import unittest
import tempFull
import threading


class OpenPort(unittest.TestCase):
#Test for open ports. We need to make the test name as descriptive as possible
#self tells us that known values are going to be running the test
	

	def test_for_open_port_verification(self):
		
		#Make sure that if the port is open, it returns the correct value
		self.assertTrue(tempFull,('is open!'))
		
	def test2_for_open_port_verification(self):
		self.assertNotEqual(tempFull,('is closed'))
		
  #This tests threading, but I don't know if it works properly. It passes, but I can't verify if it is correct.
  
	#def test_threading(self):
  		#t = threading.Thread(target=lambda: self.assertTrue(True))
  		#t.start()
  		#t.join()	
		
if __name__ == '__main__':
	unittest.main()

