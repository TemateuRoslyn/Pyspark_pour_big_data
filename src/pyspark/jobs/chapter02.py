from jobs.chapter import ChapterParent


class Chapter02(ChapterParent):

    def __str__(self):
        return f"{self.spark}({self.StructType})"

    def completeDataFrame(self):
            print(" - Show a complete dataframe \n")
            schema = self.StructType().add("user_id","string").add("country","string").add("browser", "string").add("OS",'string').add("age", "integer")

            df = self.spark.createDataFrame([("A203",'India',"Chrome","WIN",33),("A201",'China',"Safari","MacOS",35),("A205",'UK',"Mozilla","Linux",25)],schema=schema)
            df.printSchema()
            df.show()

    def dataFrameWithNullValues(self):
        print(" - Show a dataframe with NULL values \n")
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


    def selectFromDataFrame(self):
        print(" - SELECT operation from a dataframe \n")
        schema = self.StructType().add("user_id","string").add("country","string").add("browser", "string").add("OS",'string').add("age", "integer")
        df = self.spark.createDataFrame([("A203",None,"Chrome","WIN",33),("A201",'China',None,"MacOS",35),("A205",'UK',"Mozilla","Linux",25)],schema=schema)    
        print("\nThe dataframe shame\n")
        df.printSchema()
        print("\nThe complete dataframe\n")
        df.show()
        print("\nSelect Operation on `user_id` and `country` columns\n")
        df.select(['user_id','country']).show()

    def filterDataFrame(self):
        print(" - FILTER operation from a dataframe \n")
        schema = self.StructType().add("user_id","string").add("country","string").add("browser", "string").add("OS",'string').add("age", "integer")
        df = self.spark.createDataFrame([("A203",None,"Chrome","WIN",33),("A201",'China',None,"MacOS",35),("A205",'UK',"Mozilla","Linux",25)],schema=schema)    
        print("\nThe dataframe shame\n")
        df.printSchema()
        print("\nThe complete dataframe\n")
        df.show()
        print("\n Filter Operation on 30 < `age` < 50\n")
        df.filter(df['age'] > 30).filter(df['age'] <50).show()

    def whereDataFrame(self):
        print(" - WHERE operation from a dataframe \n")
        schema = self.StructType().add("user_id","string").add("country","string").add("browser", "string").add("OS",'string').add("age", "integer")
        df = self.spark.createDataFrame([("A203",None,"Chrome","WIN",33),("A201",'China',None,"MacOS",35),("A205",'UK',"Mozilla","Linux",25)],schema=schema)    
        print("\nThe dataframe shame\n")
        df.printSchema()
        print("\nThe complete dataframe\n")
        df.show()
        print("\n Filter Operation:  where 30 < `age` &  < 40\n")
        df.where((df['age'] > 30) & (df['age'] <40)).show()


    def run(self):
        self.completeDataFrame()
        self.dataFrameWithNullValues()
        print("\n -----  Read CSV File from: src/pyspark/resources/zipcodes.csv ----- \n")
        self.readCSVFile("src/pyspark/resources/zipcodes.csv", 10)
        self.selectFromDataFrame()
        self.filterDataFrame()
        self.whereDataFrame()
