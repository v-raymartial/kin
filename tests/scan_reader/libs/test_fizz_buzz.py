""" 
Module providing unit tests for NumberRecognizer 

Notes: test
"""

import pytest
from unittest.mock import patch, Mock
from libs.fizz_buzz import FizzBuzz

class TestFizzBuzz:
   
    def test_init(self):
        fizz_buzz = FizzBuzz()
        assert fizz_buzz is not None

    @pytest.mark.parametrize("input_num,outout", [
        (3,  "Fizz"),
        (5,  "Buzz"),
        (15, "FizzBuzz"),
        (1,  "1")
    ])
    def test_fizz_buzz(self, input_num : int, outout : str):
        fizz_buzz = FizzBuzz()
        assert fizz_buzz.get_fizz_buzz_value(input_num) == outout       

    def mock_get_fizz_buzz_value(self, input_num : int) -> str:
        return "FizzBuzz"

    def test_process(self):
        get_fizz_buzz_value_mock = patch.object(FizzBuzz, 'get_fizz_buzz_value', Mock(return_value="test"))
        get_fizz_buzz_value_mock_start = get_fizz_buzz_value_mock.start()
        fizz_buzz = FizzBuzz()
        fizz_buzz.process(range(1,101))
        assert get_fizz_buzz_value_mock_start.call_count == 100
        get_fizz_buzz_value_mock_start.stop()

# if __name__ == "__main__":
#     # pytest.main()
#     pytest.main(["-v", "tests/scan_reader/libs/test_fizz_buzz.py"])

        
        