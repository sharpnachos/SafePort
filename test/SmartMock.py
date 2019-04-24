import unittest
import smart
from smart import portscan
from smart import thread
from unittest.mock import patch

#the patch decorator creats a mock class
#It pulls the object from the other side and creates a mock object to test

@patch('smart.thread')
@patch('smart.portscan')

class TestMock5(unittest.TestCase):
	
	def test(self, MockClass1, MockClass2): #Create the mock test class, pass 3 positional arguments. It won't work without self
		smart.portscan() #Import the objects
		smart.thread()
		assert MockClass1 is smart.portscan #Mock the objects
		assert MockClass2 is smart.thread
		self.assertTrue(MockClass1.called) #Make sure the objects are called properly
		self.assertTrue(MockClass2.called)
		
#Runs the test 
if __name__ == '__main__':
	unittest.main()

#We don't need to worry about setup and teardown because we are mocking a decorator.
#The mock does not exist outside the function.
