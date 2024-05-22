from typing import List
from utils.logger import Logger
from libs.abstract_processor import AbstractProcessor


class AdvancedProcessor(AbstractProcessor):
    """
    TODO: A class to process the data with variable size of the number shapes
    """

    _logger = Logger(__name__ + ".AdvancedProcessor")

    def __init__(self, path: str) -> None:
        """
        :param: path (str) -- path to the files to be processed
        """
        super().__init__()
        self.path = path

    def process(self) -> List[str]:
        """TODO: ref :func:`~libs.AbstractProcessor.process`"""
        raise NotImplementedError('process()')
            