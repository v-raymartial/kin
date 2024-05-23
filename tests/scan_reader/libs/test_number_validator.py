""" 
Module providing unit tests for NumberValidator

Notes: For demonstration purpose, this is the only a few unit test files in the project given the limited time
"""

import pytest
from libs.number_validator import NumberValidator

class TestNumberValidator:
	
	@classmethod
	def setup_class(cls):
		cls.validator = NumberValidator()
	
	@classmethod
	def setup_method(self):
		pass
		
	@classmethod
	def teardown_method(self):
		pass	
	
	# cal table
	#  0     0     1     3     1
	# [25,   24,   23,   22,   21,   20,   19,   18,   17  ]
	@pytest.mark.parametrize("input, expected", [
        ("123456789", False),
        ("001310000", True )
    ])
	def test_validate_number(self, input: str, expected: bool):
		self.validator.validate(input) == expected	
