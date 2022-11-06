from modules.chapter    import ChapterParent
from pyspark.ml.feature import VectorAssembler, StringIndexer, OneHotEncoder, Binarizer, PCA, Normalizer, StandardScaler, MinMaxScaler, MaxAbsScaler, Bucketizer
from pyspark.ml.stat    import Correlation

class Chapter05(ChapterParent):
    
    def run(self):
        print("\n - chater 5 - \n")        
        # self.readSalarier()

        # appel des fonction de transformation sur les donnees
        self.binarizer()

    def readSalarier(self):
        print("\n ------ Read Salarier ------ \n")

        df = self.spark.read.csv("src/pyspark/resources/input/csv/salarier.csv", header=True, inferSchema=True)
        df.printSchema()
        df.show()

        assembler = VectorAssembler(inputCols=df.columns, outputCol="features")
        df_new    = assembler.transform(df)

        print("\n create the Spark context, in order to use Spark. : \n")
        df_new.show()

        print("\n- Coefficient de Correlation: Pearson\n")
        pearson_corr = Correlation.corr(df_new,'features')
        pearson_corr.show(2,False)

        print("\n- Coefficient de Correlation: Spearman\n")
        spearman_corr=Correlation.corr(df_new,'features',"spearman")
        spearman_corr.show(2,False)

        self.chi_sq()

    def chi_sq(self):
        print("\n-   Chi-Square Totals  -\n")
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

        print("\n VectorAssembler - \n")

        df_assembler = VectorAssembler(inputCols=['marital_vector','housing_vector'], outputCol="features")
        df = df_assembler.transform(df)
        df.show()

    def binarizer(self):
        print("\n ------ TRANSFORMATION: Binarizer ------ \n")
        df= self.spark.read.csv('src/pyspark/resources/input/csv/transformations.csv',inferSchema=True,header=True)
        df.count()
        df.show()

        print(" \n ------ After Binarize  -------- \n")
        binarizer = Binarizer(threshold=0.99, inputCol="label",outputCol="binarized_label")
        new_df=binarizer.transform(df)
        new_df.show()

        self.componentAnalysis(df)

    def componentAnalysis(self, df):
        print("\n ------ Principal Component Analysis ------ \n")
        assembler = VectorAssembler(inputCols=[col for col in df.columns if col !='label'], outputCol="features")
        df_new=assembler.transform(df)
        df_new.show()

        pca = PCA(k=2, inputCol="features", outputCol="pca_features")
        pca_model=pca.fit(df_new)
        pca_comp = pca_model.transform(df_new).select("pca_features")
        pca_comp.show(truncate=False)

        self.normalizer(df_new)

    def normalizer(self, df):
        print("\n ------ Normalizer ------ \n")

        normalizer = Normalizer(inputCol="features",outputCol="norm_features", p=1.0)
        normalised_l1_data = normalizer.transform(df)
        normalised_l1_data.select('norm_features').show(truncate=False)

        self.standardScaling(df)

    def standardScaling(self, df):
        print("\n ------ Standard Scaling ------ \n")

        scaler = StandardScaler(inputCol="features",outputCol="scaled_features",withStd=False, withMean=True)
        scaler_model = scaler.fit(df)
        scaled_data = scaler_model.transform(df)
        scaled_data.select('scaled_features').show(truncate=False)

        self.minMaxScaling(df)

    def minMaxScaling(self, df):
        print("\n ------ Min-Max Scaling ------ \n")

        mm_scaler = MinMaxScaler(inputCol="features",outputCol="mm_scaled_features")
        mm_scaler_model = mm_scaler.fit(df)
        rescaled_df = mm_scaler_model.transform(df)
        rescaled_df.select("features", "mm_scaled_features").show()

        self.maxAbsScaler(df)

    def maxAbsScaler(self, df):
        print("\n ------ MaxAbsScaler ------ \n")

        mxabs_scaler = MaxAbsScaler(inputCol="features",outputCol="mxabs_features")
        mxabs_scaler_model = mxabs_scaler.fit(df)
        rescaled_df = mxabs_scaler_model.transform(df)
        rescaled_df.select("features", "mxabs_features").show()

        self.binning(df)

    def binning(self, df):
        print("\n ------ Binning ------ \n")

        df.show(10,False)
        splits = [0.0,1.0,2.0,3.0,4.0,5.0,float("inf")]
        bucketizer = Bucketizer(splits=splits, inputCol="label",outputCol="label_bins")
        binned_df = bucketizer.transform(df)
        binned_df.select(['label','label_bins']).show(10,False)