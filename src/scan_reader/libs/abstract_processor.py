from abc import ABC, abstractmethod
from typing import List


class AbstractProcessor(ABC):
    """
    A class defining an abstract method for data processing
    """
    
    @abstractmethod
    def process(self) -> List[str]:
        """
        This method should blah blah blah...

        :return: (List[str]) -- list of paths to the output files
        """
        pass


    def get_path(self) -> str:
        """
        This method blah blah blah...
        :return: path
        :rtype: str
        """
        if getattr(self, "path", None):
            return self.path
        else:
            raise NotImplementedError('get_path()')
