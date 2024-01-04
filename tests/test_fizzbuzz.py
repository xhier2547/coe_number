from coe_number.fizzbuzz import FizzBuzzTest

import unittest

class FizzTest(unittest.TestCase ):
    
    def test_give_3_fizz(self):
        fizz_list = 3
        is_fizz = FizzBuzzTest(fizz_list)
        self.assertEqual(is_fizz, 'Fizz')
        
    def test_give_10_buzz(self):
        buzz_list = 10
        is_buzz = FizzBuzzTest(buzz_list)
        self.assertEqual(is_buzz, 'Buzz')
        
    def test_give_45_fizzbuzz(self):
        fizzbuzz_list = 45
        is_fizzbuzz = FizzBuzzTest(fizzbuzz_list)
        self.assertEqual(is_fizzbuzz, 'FizzBuzz')
        
