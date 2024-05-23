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
        
        with open(output_path, "w") as file:
            file.write("\n".join(lines))
        
        return output_path
        