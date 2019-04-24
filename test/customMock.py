#This is the mock that we are using to test the socket object

import unittest
import custom
from custom import portscan
from custom import thread
from unittest.mock import patch

#the patch decorator creats a mock class
#It pulls the object from the other side and creates a mock object to test

@patch('custom.thread')
@patch('custom.portscan')

class TestUM(unittest.TestCase):
	
	def test(self, MockClass1, MockClass2): #Create the mock test class, pass 3 positional arguments. It won't work without self
		custom.portscan() #Import the objects
		custom.thread()
		assert MockClass1 is custom.portscan #Mock the objects
		assert MockClass2 is custom.thread
		self.assertTrue(MockClass1.called) #Make sure the objects are called properly
		self.assertTrue(MockClass2.called)
		
#This runs the test		
if __name__ == '__main__':
	unittest.main()
	
#We don't need to worry about setup and teardown because we are mocking a decorator.
#The mock does not exist outside the function.
