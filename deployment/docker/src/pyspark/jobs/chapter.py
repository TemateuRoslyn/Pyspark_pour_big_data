class ChapterParent:
    def __init__(self, chapterName,  spark, StructType):
        self.chapterName = chapterName
        self.spark = spark
        self.StructType = StructType

    def readCSVFile(self, filepath, nbrLine):
        df = self.spark.read.csv(filepath)
        df.printSchema()
        df.show(nbrLine)
