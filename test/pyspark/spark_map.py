from pyspark import SparkConf,SparkContext
import os
os.environ['PYSPARK_PYTHON']="C:/Users/zj_brand/AppData/Local/Programs/Python/Python311/python.exe"
#创建SparkConf类对象
conf=SparkConf().setMaster("local[*]").setAppName("test_spark_app")

# 基于SparkConf对象创建SparkContext对象
sc=SparkContext(conf=conf)

# 构建rdd对象
rdd=sc.parallelize([1,2,3,4,5])

# def func(data):
#     return data*10
# 对每个成员计算
rdd2=rdd.map(lambda x:x*10).map(lambda x:x+5)

print(rdd2.collect())