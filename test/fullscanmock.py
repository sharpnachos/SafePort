import unittest
import full 
from full import portscan
from full import thread
from unittest.mock import patch

#the patch decorator creats a mock class
#It pulls the object from the other side and creates a mock object to test
@patch('full.thread')
@patch('full.portscan')

class TestMock4(unittest.TestCase):
	
	def test(self, MockClass1, MockClass2): #Create the mock test class, pass 3 positional arguments. It won't work without self 
		full.portscan() #Import the objects
		full.thread()
		assert MockClass1 is full.portscan #Mock the objects
		assert MockClass2 is full.thread
		self.assertTrue(MockClass1.called) #Make sure the objects are called properly
		self.assertTrue(MockClass2.called)

#This runs the test
if __name__ == '__main__':
	unittest.main()
	
#We don't need to worry about setup and teardown because we are mocking a decorator.
#The mock does not exist outside the function.
