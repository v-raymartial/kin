from utils.logger import Logger

class NumberRecognizer:
    
    _logger = Logger(__name__ + ".NumberRecognizer")

    def __init__(self) -> None:
        pass
    
    def execute(self, path: str) -> None:
        """
        Execute the number recognition process
        :param: path (str) -- path to the file to be processed
        """
        self._logger.info(f"Recognizing numbers in the file: {path}")