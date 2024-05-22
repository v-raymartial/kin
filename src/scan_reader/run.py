import sys
from utils.logger import Logger

class Runner:
    """
    A class for running the scan reader
    """
    logger = Logger(__name__ + f".FeedAPI")
    
    def execute(self, path: str):
        self.logger.info(f"TEST!!!!! {path}")

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "../../data"
    runner = Runner()
    runner.execute(path)