from pyspark.sql import SparkSession

def get_spark_session(app_name="kin") -> SparkSession:
    """
    Spark session that encompasses needs across all computations.
    """
    global spark_session
    spark_session = None
    
    if not spark_session:
        spark_session = (
            SparkSession.builder.appName(app_name).getOrCreate()
        )
    return spark_session