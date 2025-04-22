from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("SampleSparkJob").getOrCreate()
df = spark.read.csv("data/input.csv", header=True)
df.show()
spark.stop() 
