import os
import sys
from utils.logger import Logger
from libs.constants import ProcessorTypes
from libs.processor_factory import ProcessorFactory

class Runner:
    """
    A class for running the scan reader
    """
    _logger = Logger(__name__ + f".Runner")
    
    def execute(self, path: str, processor_type: ProcessorTypes = ProcessorTypes.BASIC):
        """
        Create a processor based on process_type with a factory pattern to process data
        :param: path (str) -- path to the files to be processed
        :param: processor_type (ProcessorTypes) -- processor type. Default value: ProcessorTypes.BASIC
        """

        factory = ProcessorFactory()
        processor = factory.get_processor(path, processor_type)
        output = processor.process()
        self._logger.info(output)

if __name__ == "__main__":
    
    default_data_path = os.path.join(os.getcwd(), "data")
    path = sys.argv[1] if len(sys.argv) > 1 else default_data_path
    processor_type = sys.argv[2] if len(sys.argv) > 2 else ProcessorTypes.BASIC
    runner = Runner()
    runner.execute(path, processor_type)