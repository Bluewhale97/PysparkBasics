df.createOrReplaceTempView("PERSON_DATA")
df2 = spark.sql("SELECT * from PERSON_DATA")
df2.printSchema()
df2.show()

groupDF = spark.sql("SELECT gender, count(*) from PERSON_DATA group by gender")
groupDF.show()

df = spark.readStream
      .format("socket")
      .option("host","localhost")
      .option("port","9090")
      .load()
      
query = count.writeStream
      .format("console")
      .outputMode("complete")
      .start()
      .awaitTermination()      
      
df.selectExpr("CAST(id AS STRING) AS key", "to_json(struct(*)) AS value")
   .writeStream
   .format("kafka")
   .outputMode("append")
   .option("kafka.bootstrap.servers", "192.168.1.100:9092")
   .option("topic", "josn_data_topic")
   .start()
   .awaitTermination()


import pyspark
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()
sparkContext=spark.sparkContext

rdd=sparkContext.parallelize([1,2,3,4,5])
rddCollect = rdd.collect()
print("Number of Partitions: "+str(rdd.getNumPartitions()))
print("Action: First element: "+str(rdd.first()))
print(rddCollect)

Number of Partitions: 4
Action: First element: 1
[1, 2, 3, 4, 5]

#Replace part of string with another string
from pyspark.sql.functions import regexp_replace
df.withColumn('address', regexp_replace('address', 'Rd', 'Road')) \
  .show(truncate=False)


from pyspark.sql import SparkSession
spark = SparkSession.builder \
         .appName('SparkByExamples.com') \
         .getOrCreate()

data = [("James, A, Smith","2018","M",3000),
            ("Michael, Rose, Jones","2010","M",4000),
            ("Robert,K,Williams","2010","M",4000),
            ("Maria,Anne,Jones","2005","F",4000),
            ("Jen,Mary,Brown","2010","",-1)
            ]

columns=["name","dob_year","gender","salary"]
df=spark.createDataFrame(data,columns)
df.printSchema()

      
    
