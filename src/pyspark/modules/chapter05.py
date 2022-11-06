from modules.chapter import ChapterParent
from pyspark.ml.feature import VectorAssembler, StringIndexer, OneHotEncoder
from pyspark.ml.stat import Correlation

class Chapter05(ChapterParent):
    
    def run(self):
        print("\n - Hello 5 chater 5 - \n")

        # df = self.spark.read.csv("src/pyspark/resources/input/csv/salarier.csv", header=True, inferSchema=True)
        # df.printSchema()
        # df.show()

        # assembler = VectorAssembler(inputCols=df.columns, outputCol="features")
        # df_new    = assembler.transform(df)

        # print("\n create the Spark context, in order to use Spark. : \n")
        # df_new.show()

        # print("\n- Coefficient de Correlation: Pearson\n")
        # pearson_corr = Correlation.corr(df_new,'features')
        # pearson_corr.show(2,False)

        # print("\n- Coefficient de Correlation: Spearman\n")
        # spearman_corr=Correlation.corr(df_new,'features',"spearman")
        # spearman_corr.show(2,False)

        self.chi_sq()

    def chi_sq(self):
        df= self.spark.read.csv('src/pyspark/resources/input/csv/chi_sq.csv',inferSchema=True,header=True)
        df.count()
        df.show()

        marital_indexer = StringIndexer(inputCol="marital", outputCol="marital_num").fit(df)
        df = marital_indexer.transform(df)
        
        marital_encoder = OneHotEncoder(inputCol="marital_num", outputCol="marital_vector")
        marital_encoder.setDropLast(False)
        marital_model = marital_encoder.fit(df) # indexer is the existing dataframe, see the question
        df = marital_model.transform(df)

        housing_indexer = StringIndexer(inputCol="housing", outputCol="housing_num").fit(df)
        df = housing_indexer.transform(df)
        
        housing_encoder = OneHotEncoder(inputCol="housing_num", outputCol="housing_vector")
        housing_encoder.setDropLast(False)
        housing_model = housing_encoder.fit(df) # indexer is the existing dataframe, see the question
        df = housing_model.transform(df)
        
        df.show()
