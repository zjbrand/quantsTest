from pyspark import SparkConf,SparkContext

#创建SparkConf类对象
conf=SparkConf().setMaster("local[*]").setAppName("test_spark_app")

# 基于SparkConf对象创建SparkContext对象
sc=SparkContext(conf=conf)

print(sc.version)

sc.stop()


