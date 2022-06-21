import unittest
from SignInTest import*


class TestSignIn(unittest.TestCase):
    
    def test_SignIn(self):
        result = SignInTest("Hello", "Hello_Hello")
        self.assertEqual(result, "Welcome to your account !!")
        
        
if __name__ == '__main__':
    unittest.main()