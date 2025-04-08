from pyspark import SparkConf,SparkContext
import os
os.environ['PYSPARK_PYTHON']="C:/Users/zj_brand/AppData/Local/Programs/Python/Python311/python.exe"
#创建SparkConf类对象
conf=SparkConf().setMaster("local[*]").setAppName("test_spark_app")

# 基于SparkConf对象创建SparkContext对象
sc=SparkContext(conf=conf)

# 构建rdd对象
rdd=sc.parallelize([1,1,2,2,2,3,3,4,4,4,4,5,5,6,6,5])
#去除重复内容
rdd1=rdd.distinct()

print(rdd1.collect())