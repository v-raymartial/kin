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
	#  0      0     1     3     1     0     0     0     0
	# [217,   216,  215,  214,  213,  212,  211,  210,  209]
	@pytest.mark.parametrize("input, expected", [
		( "123?56789", "ILL" ),
        ( "223403789", "PAS" ),
        ( "001310000", "ERR" )
    ])
	def test_validate_number(self, input: str, expected: str):
		assert self.validator.validate(input) == expected
