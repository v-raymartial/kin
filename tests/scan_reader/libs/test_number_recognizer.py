""" 
Module providing unit tests for NumberRecognizer 

Notes: For demonstration purpose, this is the only a few unit test files in the project given the limited time
"""

import os
from libs.number_recognizer import NumberRecognizer


class TestNumberRecognizer:
    
    def test_init(self):
        number_recognizer = NumberRecognizer()
        assert number_recognizer is not None
        
    def test_recognize_number(self):
        number_recognizer = NumberRecognizer()
        assert number_recognizer._NumberRecognizer__recognize_number(" _ | ||_|") == "0"
        assert number_recognizer._NumberRecognizer__recognize_number("     |  |") == "1"
        assert number_recognizer._NumberRecognizer__recognize_number(" _  _||_ ") == "2"
        assert number_recognizer._NumberRecognizer__recognize_number(" _  _| _|") == "3"
        
    def test_recognize(self):
        number_recognizer = NumberRecognizer()
        lines = [
            "    _  _     _  _  _  _  _ ",
            "  | _| _||_||_ |_   ||_||_|",
            "  ||_  _|  | _||_|  ||_| _|",
            "                           "
        ]
        assert number_recognizer._NumberRecognizer__recognize(lines) == ["123456789 ERR"]
        
    def test_execute(self):
        number_recognizer = NumberRecognizer()
        path = os.path.join(os.getcwd(), "data", "file02.txt")
        output_path = number_recognizer.execute(path)
        assert output_path == f"{path}.output"
        assert open(output_path, "r").read() == "123456789 ERR\n223403789\n223403?89 ILL"       
        
        