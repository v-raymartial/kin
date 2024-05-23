from sqlite3 import Row
from typing import List
from utils.logger import Logger

class NumberRecognizer:
    
    _logger = Logger(__name__ + ".NumberRecognizer")

    def __init__(self) -> None:
        pass
    
    def execute(self, path: str) -> str:
        """
        Execute the number recognition on given file and outputs the recognized numbers in a separate file
        :param: path (str) -- path to the file to be processed
        :return: path to the output file
        """
        self._logger.info(f"Recognizing numbers in the file: {path}")
        
        output_path = f"{path}.output"
        lines = open(path, "r").readlines()
        number_lines = self.__recognize(lines)

        with open(output_path, "w") as file:
            file.write("\n".join(number_lines))
        
        return output_path

    def __recognize(self, lines: List[str]) -> List[str]:
        """
        Recognize numbers in the given lines
        :param: lines (List[str]) -- list of lines to be processed
        :return: list of recognized numbers
        """
        number_lines = []
        for row_idx in range(0, len(lines), 4): # read 4 lines at a time
            line = ""
            for col_idx in range(0, 26, 3): # read 3 chars at a time
                # combine first 3 lines into a single line by concatenating each character from each lines
                number_str = \
                     lines[row_idx][col_idx : col_idx+3] + \
                     lines[row_idx+1][col_idx : col_idx+3] + \
                     lines[row_idx+2][col_idx : col_idx+3]
                    
                line += self.__recognize_number(number_str)
            number_lines.append(line)
            
        return number_lines

    def __recognize_number(self, number_str: str) -> str:
        """
        Recognize a number from the given string
        :param: number_str (str) -- string containing a number
        :return: recognized number
        """
        match number_str:
            case " _ | ||_|":
                return "0"
            case "     |  |":
                return "1"
            case " _  _||_ ":
                return "2"
            case " _  _| _|":
                return "3"
            case "   |_|  |":
                return "4"
            case " _ |_  _|":
                return "5"
            case " _ |_ |_|":
                return "6"
            case " _   |  |":
                return "7"
            case " _ |_||_|":
                return "8"
            case " _ |_| _|":
                return "9"
            case _:
                return "?"
        