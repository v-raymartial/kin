from enum import Enum

MAX_FILE_COUNT_FOR_SINGLE_MACHINE = 500 # maximum number of files that can be processed by a single machine

class ProcessorTypes(str, Enum):
    """
    A class containing various static parameters enumerating supported processor types
    """

    BASIC = "basic" # to support basic fixed data format (3x9)
    ADVANCED = "advanced" # TODO: to support non-fixed data format (not 3x9)
    INTELLIGENT = "intelligent" # TODO: to adopt AI or ML approach 

    def __str__(self):
        """
        Method returning a string representation of the class

        :return: a string containing one of the static parameters defined in the class

        """
        return str(self.value)