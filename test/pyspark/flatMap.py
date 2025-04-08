from pyspark import SparkConf,SparkContext
import os
os.environ['PYSPARK_PYTHON']="C:/Users/zj_brand/AppData/Local/Programs/Python/Python311/python.exe"
#创建SparkConf类对象
conf=SparkConf().setMaster("local[*]").setAppName("test_spark_app")

# 基于SparkConf对象创建SparkContext对象
sc=SparkContext(conf=conf)

# 构建rdd对象
rdd=sc.parallelize(["要 抄 底","必 须","有 耐 心"])

# rdd2=rdd.map(lambda x : x.split(" ")) #[['要', '抄', '底'], ['必', '须'], ['有', '耐', '心']]
rdd2=rdd.flatMap(lambda x : x.split(" "))

print(rdd2.collect())

# reduceByKey聚合
rdd1=sc.parallelize([('男',99),('男',88),('女',99),('女',66)])

rdd3=rdd1.reduceByKey(lambda a,b:a+b)

print(rdd3.collect())