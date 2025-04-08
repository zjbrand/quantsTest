from pyspark import SparkConf,SparkContext
import os
import json

os.environ['PYSPARK_PYTHON']="C:/Users/zj_brand/AppData/Local/Programs/Python/Python311/python.exe"
#创建SparkConf类对象
conf=SparkConf().setMaster("local[*]").setAppName("test_spark_app")
conf.set("spark.default.parallelism","1")
# 基于SparkConf对象创建SparkContext对象
sc=SparkContext(conf=conf)

# 读取文件
file_rdd=sc.textFile("search_log.txt")

# 需求1：热门搜索时间top3
result1=file_rdd.map(lambda x:x.split("\t")).\
    map(lambda x:x[0][:2]).\
    map(lambda x:(x,1)).\
    reduceByKey(lambda a,b:a+b).\
    sortBy(lambda x:x[1],ascending=False,numPartitions=1).\
    take(3)
print("需求1的结果:",result1)

# 需求2：热门搜索词top3
result2=file_rdd.map(lambda x:(x.split("\t")[2],1)).\
    reduceByKey(lambda a,b:a+b).\
    sortBy(lambda x:x[1],ascending=False,numPartitions=1).\
    take(3)
print("需求2的结果:",result2)

# 需求3：统计黑马程序员关键字在什么时段被搜索的最多
result3=file_rdd.map(lambda x:x.split("\t")).\
    filter(lambda x:x[2]=='黑马程序员').\
    map(lambda x:(x[0][:2],1)).\
    reduceByKey(lambda a,b:a+b).\
    sortBy(lambda x:x[1],ascending=False,numPartitions=1).\
    take(1)
print("需求3的结果:",result3)

#需求4：将数据转换为Json格式，写出到文件中
file_rdd.map(lambda x:x.split("\t")).\
    map(lambda x:{"time":x[0],"user_id":x[1],"key_word":x[2],"rank1":x[3],"rank2":x[4],"url":x[5]}).\
    saveAsTextFile("output_json")


