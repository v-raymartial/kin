from utils.logger import Logger
from libs.constants import ProcessorTypes
from libs.basic_processor import BasicProcessor

class ProcessorFactory:
    """
    A class for running the scan reader
    """
    _logger = Logger(__name__ + f".ProcessorFactory")
    
    def get_processor(self, path: str, processor_type: ProcessorTypes = ProcessorTypes.BASIC):
        """
        Get a processor based on process_type with a factory pattern
        :param: path (str) -- path to the files to be processed
        :param: processor_type (ProcessorTypes) -- processor type. Default value: ProcessorTypes.BASIC
        """

        match processor_type:
            case ProcessorTypes.BASIC:
                processor = BasicProcessor(path)
            case _:
                raise NotImplementedError('get_path()')
        
        return processor