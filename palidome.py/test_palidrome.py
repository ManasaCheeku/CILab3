import unittest
from palidrome import is_palindrome

class TestPalindrome(unittest.TestCase):
    def test_true_palindromes(self):
        self.assertTrue(is_palindrome("radar"))
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))

    def test_false_palindromes(self):
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("world"))

if __name__ == '__main__':
    unittest.main()
