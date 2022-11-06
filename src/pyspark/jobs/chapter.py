class ChapterParent:
    def __init__(self, chapterName,  spark, StructType):
        self.chapterName = chapterName
        self.spark = spark
        self.StructType = StructType

    def readCSVFile(self, filepath, nbrLine):
        df = self.spark.read.csv(filepath)
        df.printSchema()
        df.show(nbrLine)

    def writeCSVFile(self, folder_path, dataBody, dataHeader, customMode):
        self.spark.createDataFrame(dataBody, dataHeader).write.csv(folder_path,mode=customMode)
