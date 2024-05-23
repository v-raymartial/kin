from utils.logger import Logger

POSITIONS = [0xd9, 0xd8, 0xd7, 0xd6, 0xd5, 0xd4, 0xd3, 0xd2, 0xd1]
#           [25,   24,   23,   22,   21,   20,   19,   18,   17  ]

class NumberValidator:
    """
    A class validates the numbers in a given number string
    """
    _logger = Logger(__name__ + ".NumberValidator")

    def __init__(self) -> None:
        pass
    
    def validate(self, number_str: str) -> bool:
        """
        Validate a number from the given string
        :param: number_str (str) -- number string for validation
        :return: boolean value indicating whether the number is valid
        """
        self._logger.info(f"validate number string: {number_str}")
        
        check_sum = 0
        for n in number_str:
            idx = number_str.index(n)
            check_sum += int(n) * POSITIONS[idx]

        check_sum = check_sum % 11
        
        return check_sum == 0             
        
        