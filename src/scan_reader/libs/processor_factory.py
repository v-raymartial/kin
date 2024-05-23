from utils.logger import Logger
from libs.constants import ProcessorTypes
from libs.basic_processor import BasicProcessor
from libs.advanced_processor import AdvancedProcessor
from libs.intelligent_processor import IntelligentProcessor

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
            case ProcessorTypes.ADVANCED:
                processor = AdvancedProcessor(path)
            case ProcessorTypes.INTELLIGENT:
                processor = IntelligentProcessor(path)
            case _:
                raise NotImplementedError(f'processor type {processor_type}')
        
        return processor