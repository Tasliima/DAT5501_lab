import unittest
unittest.main()
from MyFunction import incrementals

# define the unit tests
class test_one(unittest.TestCase):
    def test_incrementals(self):
        
        # test adding integers
        self.assertEqual(my_incrementals(2), 3)

        # test adding negative integers
        self.assertEqual(my_incrementals(-6), -5)

        # test adding floats
        self.assertEqual(my_incrementals(3.1), 4.1)

# run the tests
if __name__ == "__main__":
    unittest.main()