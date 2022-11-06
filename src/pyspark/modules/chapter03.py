from modules.chapter import ChapterParent

class Chapter03(ChapterParent):

    def writeStreamingToCSVFolder(self):
        print("\n - We actually write custom data to in csv folder using streaming \n")

        self.writeCSVFile(
            "src/pyspark/resources/output/csv/chapter03", 
            [
                ("XN203",'FB',300,30),
                ("XN201",'Twitter',10,19),
                ("XN202",'Insta',500,45)
            ],
            ["user_id","app","time_in_secs","age"], 
            'append')

        print("----- Please check  the folder at: src/pyspark/resources/output/csv/chapter03 to see the resule   ---------\n")


    def readStreamingFromCSVFolder(self):
        print("\n - We actually read custom data from in csv folder using streaming \n")

        schema = self.StructType().add("user_id","string").add("app","string").add("time_in_secs", "integer").add("age","integer")
        datas  = self.spark.readStream.option("sep", ",").schema(schema).csv("src/pyspark/resources/output/csv/chapter03")
        isStreaming =  datas.isStreaming
        print("Is streaming = ", isStreaming)
        datas.printSchema()

        print("\n----- Please check  the folder at: src/pyspark/output/csv/chapter03 to see the resule   ---------\n")



    def run(self):
        # self.writeStreamingToCSVFolder()
        self.readStreamingFromCSVFolder()
