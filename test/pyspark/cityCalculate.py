from pyspark import SparkConf,SparkContext
import os
import json

os.environ['PYSPARK_PYTHON']="C:/Users/zj_brand/AppData/Local/Programs/Python/Python311/python.exe"
#创建SparkConf类对象
conf=SparkConf().setMaster("local[*]").setAppName("test_spark_app")

# 基于SparkConf对象创建SparkContext对象
sc=SparkContext(conf=conf)

# 读取文件
file_rdd=sc.textFile("orders.txt")

# 取出每个json字符串
json_str_rdd=file_rdd.flatMap(lambda x:x.split("|"))

# 将json字符串变为字典
dict_rdd=json_str_rdd.map(lambda x:json.loads(x))

#获取城市和销售额的元组
city_with_money_rdd=dict_rdd.map(lambda x:(x['areaName'],int(x['money'])))

#按照城市聚合
city_result_rdd=city_with_money_rdd.reduceByKey(lambda a,b:a+b)

#按城市排序统计销售额
result_rdd=city_result_rdd.sortBy(lambda x:x[1],ascending=False,numPartitions=1)
print("sort result:",result_rdd.collect())

# 查询出所有售卖商品
category_rdd=dict_rdd.map(lambda x:x['category']).distinct()
print("All goods:",category_rdd.collect())

# 查询出北京售卖商品
beijing_data_rdd=dict_rdd.filter(lambda x:x['areaName']=='北京')
result3_rdd=beijing_data_rdd.map(lambda x:x['category']).distinct()
print("BeiJing's goods:",result3_rdd.collect())

sc.stop()