from utils.logger import Logger

class FizzBuzz():
    """
    A class to process the data with fixed format: 9 numbers x 3 chars x 3 rows
    """

    _logger = Logger(__name__ + ".BasicProcessor")

    def __init__(self) -> None:
        pass
                

    def get_fizz_buzz_value(self, input_num : int) -> str:
        """ref :func:`~libs.AbstractProcessor.process`"""

        self._logger.info(f"processing .. {input_num}")
        
        if input_num % 3 == 0 and input_num % 5 == 0:
            return "FizzBuzz"
        
        if input_num % 3 == 0:
            return "Fizz"

        if input_num % 5 == 0:
            return "Buzz"
        
        return str(input_num)

    def process(self, nums):
        
        for num in nums:
            self._logger.info(self.get_fizz_buzz_value(num)) # 100 times
    
        
# if __name__ == "__main__":
#     test = FizzBuzz()
#     test.process()
        