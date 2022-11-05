def completeDataFrame(SparkSession, StructType):
    spark = SparkSession.builder.appName('data_processing').getOrCreate()

    schema = StructType().add("user_id","string").add("country","string").add("browser", "string").add("OS",'string').add("age", "integer")

    df=spark.createDataFrame([("A203",'India',"Chrome","WIN",33),("A201",'China',"Safari","MacOS",35),("A205",'UK',"Mozilla","Linux",25)],schema=schema)
    df.printSchema()
    df.show()

def dataFrameWithNullValues(SparkSession, StructType):
    spark = SparkSession.builder.appName('data_processing').getOrCreate()

    schema = StructType().add("user_id","string").add("country","string").add("browser", "string").add("OS",'string').add("age", "integer")

    df=spark.createDataFrame([("A203",'India',"Chrome","WIN",33),("A201",'China',"Safari","MacOS",35),("A205",'UK',"Mozilla","Linux",25)],schema=schema)
    df.printSchema()
    df.show()
