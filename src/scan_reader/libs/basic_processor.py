from pathlib import Path
from typing import List
from libs.constants import MAX_FILE_COUNT_FOR_SINGLE_MACHINE
from pyspark.sql.types import StringType
from utils.logger import Logger
from utils.spark_utils import get_spark_session
from libs.abstract_processor import AbstractProcessor
from libs.number_recognizer import NumberRecognizer


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

        self._logger.info(f"processing file(s).. Path: {self.path}")
        
        files = []
        
        # read all file urls recursively in the path if it is a directory
        path_obj = Path(self.path)
        if path_obj.is_dir():
            file_or_paths = path_obj.rglob("**/*.txt")
            files = [str(f) for f in file_or_paths if f.is_file()]
        elif path_obj.exists():
            files = [self.path]

        recognizer = NumberRecognizer()   
        output_paths = []
        
        # determine whether to use a single machine or Spark cluster to process the files
        if len(files) > 0:    
            if len(files) <= MAX_FILE_COUNT_FOR_SINGLE_MACHINE:
                for f in files:
                    output_paths.append(recognizer.execute(f))
            else:
                spark = get_spark_session()
                # create a DataFrame containing the file paths
                df_files = spark.createDataFrame(files, StringType())
                # process the files using the Spark cluster
                output_paths = df_files.rdd.mapPartitions(lambda partition: [
                    recognizer.execute(row.value)
                    for row in partition
                ]).collect()
                
            self._logger.info(f"Output paths: {output_paths}")
        else:
            self._logger.warning(f"No files found in the path: {self.path}")