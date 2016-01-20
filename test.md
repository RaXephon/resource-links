#### Big Data Processing with Hadoop & Spark
#### Winter 2016
#### Syllabus

--

#### Week 1/Class 1:
*Lecture:*
 * introduction to myself & course
 * motivation for why use distributed computing 
 * pitfalls of classical thread-lock distributed computing models
(deadlock, race conditions, hardware provisioning, software debug)
 * enter HDFS (to solve above problems)
 * bit of HDFS history  
*Labs:*
 * Setting up Cloudera Virtual Machine
 * HDFS commands, navigating HDFS file system, copying files
 * Setting up AWS EC2 instance

#### Week 1/Class 2:
*Lecture:*  
 * review of previous class
 * HDFS architecture (NameNodes, DataNodes etc)
- HDFS performance & tuning (control block size, # map tasks etc)
- HDFS read/write process
- Hadoop distributed cache
*Lecture:*
- computational model of MapReduce (map, shuffle, reduce steps)
- requirements to model problem in terms of MR: (monoid, commutative reducers, key-value pairs)
*Lab:* 
- word count application in local
- word count application on AWS

--

#### Week 2/Class 1:
*Lecture:*  
- review of previous class
- common Hadoop errors
- MapReduce using Java API
- MapReduce using REST API
- Hadoop streaming (using Python)
*Lab:*  
- formulating image processing application (smoothing filter) in terms of MapReduce
- run output in local then on AWS  

*Lecture:*
- MapReduce design patterns: summary functions, filtering, joins
- improvements on Hadoop: Tez
- more about the Hadoop ecosystem
- Hortonworks vs Cloudera
*Lab:* 
- navigating Hadoop ecosystem in Hortonworks (screenshots)

#### Week 2/Class 2:
*Lecture:*
- review of previous lecture
- MapReduce vs relational database
- HBase, Hadoop’s key-value store
- HBase data model
- HBase rows and columns
- Bloom Filter
*Lab:*
- creating tables & running basic operations in Hbase (screenshots)

--

#### Week 3/Class 1:
*Lecture:*
- review of previous lecture
- Hive: Hadoop’s data warehouse
- HiveQL, a query language similar to mySQL
- Hive schemas
- Hive User Defined Functions (UDFs)
*Lab:*
- creating tables, working with HiveQL
- writing Hive UDF

#### Week 3/Class 2:
*Lecture:*
- Pig scripting language
- Pig loading & storing data
- Pig schemas
- Pig UDFs
*Lab:*
- Pig loading, storing, combing and splitting data

--

#### Week 4/Class 1:
*Lecture:*
- review of previous lecture
- introduction & history of Spark
- Resilient Distributed Datasets (RDDs)
- Spark programming model
- Spark Transformations and Actions
- the Spark ecosystem (MLlib, SparkSQL, Spark Streaming, GraphX)
*Lab:* 
- set up pySpark
- word count application in local
- word count application on AWS

#### Week 4/Class 2:
*Lecture:*
- review of previous lecture
- Spark SQL basics
- Spark data frames
- Spark and Hive
*Lab:*
- loading data into Spark SQL
- using Spark SQL

--

#### Week 5/Class 1:
*Lecture:*
- review of previous lecture
- what is machine learning?
- how is Spark useful for machine learning?
- basic linear algebra
*Lab:*
- a tour of MLlib
*Lecture:*
- supervised learning: linear & logistic regression
*Lab:*
- implement linear regression on data set with Spark
- run on local
- run on AWS

#### Week 5/Class 2:
##### *Lecture:*
- review of previous lecture
- unsupervised learning: Principal Component Analysis
##### *Lab:*
- implement PCA on dataset with Spark
- run on local
- run on AWS

--

#### Week 6/Class 1:
*Lecture:*
- review of previous lecture
- introduction to Scala
- streaming concepts, including some Kafka?
- Spark streaming
*Lab:*
- working with streaming

#### Week 6/Class 2:
*Lecture:*
- class wrap-up
*Lab:*
- project day! 
- work on something relevant to your job
