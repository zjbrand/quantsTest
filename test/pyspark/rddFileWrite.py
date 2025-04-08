from pyspark import SparkConf,SparkContext
import os

os.environ['PYSPARK_PYTHON']="C:/Users/zj_brand/AppData/Local/Programs/Python/Python311/python.exe"
os.environ['HADOOP_HOME']="C:/baidunetdiskdownload/hadoop-3.0.0"

#创建SparkConf类对象
conf=SparkConf().setMaster("local[*]").setAppName("test_spark_app")

# hadoop会把数据分到各分区中，比如CPU内核为16，则为16个分区，分别放置数据。为便于查看设置全局并行度为1
conf.set("spark.default.parallelism",1)

# 基于SparkConf对象创建SparkContext对象
sc=SparkContext(conf=conf)



# 构建rdd对象
rdd1=sc.parallelize([1,2,3,4,5])

#也可单独设置全局并行度 rdd1=sc.parallelize([1,2,3,4,5],numSlice=1) 或者 rdd1=sc.parallelize([1,2,3,4,5],1)
rdd2=sc.parallelize([("Hello",3),("Spark",5),("Hi",7)])
rdd3=sc.parallelize([[1,3,5],[6,7,9],[11,13,11]])

rdd1.saveAsTextFile("output1")
rdd2.saveAsTextFile("output2")
rdd3.saveAsTextFile("output3")
