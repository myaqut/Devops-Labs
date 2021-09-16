import unittest
import flaskapp
import time

class TestStringMethods(unittest.TestCase):
    #check if the time is refreshing by taking time and then taking it again after 5 seconds delay
    def check_refresh(self):
        value1 = flaskapp.current_time()
        time.sleep(5)
        value2 = flaskapp.current_time()
        self.assertNotEqual(value1,value2,"not refreshing, time taken after 5 seconds is the same as before the 5 seconds delay")
        print ("time refresh is correct")


if __name__ == '__main__':
    unittest.main()
