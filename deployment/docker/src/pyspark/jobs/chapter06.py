class Chapter06:
    
    def __init__(self, chapterName,  spark, StructType):
        self.chapterName = chapterName
        self.spark = spark
        self.StructType = StructType

    def run(self):
        print("Hello from chater 6")