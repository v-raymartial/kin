from typing import List
from utils.logger import Logger
from libs.abstract_processor import AbstractProcessor


class BasicProcessor(AbstractProcessor):
    """
    A class to process the data with fixed format: 9 numbers x 3 chars x 3 rows
    """

    _logger = Logger(__name__ + ".BasicProcessor")

    def __init__(self, path: str) -> None:
        """
        :param: path (str) -- path to the files to be processed
        """
        super().__init__()
        self.path = path

    def process(self) -> List[str]:
        """ref :func:`~libs.AbstractProcessor.process`"""

        self._logger.info(f"TEST!!!!! {self.path}")

        return None