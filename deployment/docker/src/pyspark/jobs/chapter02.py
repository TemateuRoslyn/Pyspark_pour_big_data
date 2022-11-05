from jobs.chapter import ChapterParent


class Chapter02(ChapterParent):

    def __str__(self):
        return f"{self.spark}({self.StructType})"

    def completeDataFrame(self):
            schema = self.StructType().add("user_id","string").add("country","string").add("browser", "string").add("OS",'string').add("age", "integer")

            df = self.spark.createDataFrame([("A203",'India',"Chrome","WIN",33),("A201",'China',"Safari","MacOS",35),("A205",'UK',"Mozilla","Linux",25)],schema=schema)
            df.printSchema()
            df.show()

    def dataFrameWithNullValues(self):
        schema = self.StructType().add("user_id","string").add("country","string").add("browser", "string").add("OS",'string').add("age", "integer")

        print("The Initial Data Frame\n")
        df = self.spark.createDataFrame([("A203",None,"Chrome","WIN",33),("A201",'China',None,"MacOS",35),("A205",'UK',"Mozilla","Linux",25)],schema=schema)    
        df.show()

        print("We fill the empty values by 0 instead of null value\n")
        df.fillna('0').show()

        print("We fill the empty values by correctes values\n")
        df.fillna( { 'country':'USA', 'browser':'Safari' } ).show()

        print("After Droping rows with any null values\n")
        df.na.drop().show()

    def run(self):
        # self.completeDataFrame()
        # self.dataFrameWithNullValues()
        print("Read CSV File from: /path/to/container/container-resources/zipcodes.csv")
        self.readCSVFile("container-resources/zipcodes.csv", 10)
