from enum import Enum

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