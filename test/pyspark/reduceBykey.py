from pyspark import SparkConf,SparkContext
import os
os.environ['PYSPARK_PYTHON']="C:/Users/zj_brand/AppData/Local/Programs/Python/Python311/python.exe"
#创建SparkConf类对象
conf=SparkConf().setMaster("local[*]").setAppName("test_spark_app")

# 基于SparkConf对象创建SparkContext对象
sc=SparkContext(conf=conf)
#指定读取文本路径
rdd=sc.textFile("C:/Users/zj_brand/PycharmProjects/test/test1.txt")
#把每个字符放入list中
word_rdd=rdd.flatMap(lambda x:x.split(" "))

#print(word_rdd.collect())
#把每个成员变成元组
word_with_one_rdd=word_rdd.map(lambda word:(word,1))
#对每个元组按键值统计数量
result_rdd=word_with_one_rdd.reduceByKey(lambda a,b:a+b)
#对每个元素排序
#final_rdd=result_rdd.sortBy(lambda x:x[1],ascending=False,numPartitions=1)
final_rdd=result_rdd.sortBy(lambda x:x[1],ascending=True,numPartitions=1)
print(final_rdd.collect())
