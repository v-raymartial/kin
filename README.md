### Setting Up Local Development/Testing Environment

To prepare a local environment for development and testing on a Windows machine (TODO: iOS, Ubuntu):

1. **Install Python**:

   Download and install Python 3.10.0 from https://www.python.org/downloads/release/python-3100/

   Add C:\Users\{your-login}\AppData\Local\Programs\Python\Python310 to system path env

   Add C:\Users\{your-login}\AppData\Local\Programs\Python\Python310\Scripts to system path env
   
   Add C:\Users\{your-login}\source\repos\kin\src\scan_reader to a file named dev.pth, then place dev.pth in c:\Users\{your-login}\AppData\Roaming\Python\Python310\site-packages
    

2. **Install Spark**:

   Install "Spark 3.3.1 for Hadoop 3.3+" from https://spark.apache.org/downloads.html into C:\Program Files\Spark

   Add SPARK_HOME=C:\Program Files\Spark to system env

   Add PYSPARK_PYTHON=python to system env

   Add C:\Program Files\Spark\bin to system Path

3. **Run Program**:

   ```bash
    cd C:\Users\{your-login}\source\repos\kin\src\scan_reader

    # To run the program with default input
    python ./run.py

    # To specify a path
    python ./run.py ../../data/file01.txt
    python ./run.py ../../data
   ```
   
