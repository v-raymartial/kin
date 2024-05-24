import re
from utils.logger import Logger

POSITIONS = [0xd9, 0xd8, 0xd7, 0xd6, 0xd5, 0xd4, 0xd3, 0xd2, 0xd1]
#           [217,   216,  215,  214,  213,  212,  211,  210,  209]

class NumberValidator:
    """
    A class validates the numbers in a given number string
    """
    _logger = Logger(__name__ + ".NumberValidator")

    def __init__(self) -> None:
        pass
    
    def validate(self, number_str: str) -> str:
        """
        Validate a number from the given string
        :param: number_str (str) -- number string for validation
        :return: 
        :   if number_str contains ?, returns ILL
        :   if validation passed, returns PAS
        :   if validation failed, returns ERR
        """

        result = ""        
        check_sum = 0
        if len(number_str.split("?", 1)) > 1:
            result = "ILL"
        else:
            for n in number_str:
                idx = number_str.index(n)
                check_sum += int(n) * POSITIONS[idx]

            check_sum = check_sum % 11
            result = "PAS" if check_sum == 0 else "ERR"
            
        self._logger.info(f"validated number string: {number_str} - {result} - {check_sum}")
        
        return result
        
        