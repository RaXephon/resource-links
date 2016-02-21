


[How to Install PySpark and Integrate with IPython Notebook](https://www.dataquest.io/blog/installing-pyspark/)  

### Running Interactive Spark

* Folder to run interactive Spark:    
```
$ pwd
/Users/reshamashaikh/_ds/metis/spark-1.5.2-bin-hadoop2.6
```

* To start up the interactive PySpark shell:  (This is the interactive PySpark shell, similar to IPython)    
```
$ bin/pyspark
```

* if you run `sc` in the shell, you’ll see the SparkContext object already initialized. You can write and run commands interactively in this shell just like you can with IPython.  
```
>>> sc
```
86 with 530.0 MB RAM, BlockManagerId(driver, localhost, 50886)
16/02/20 22:59:57 INFO BlockManagerMaster: Registered BlockManager
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /__ / .__/\_,_/_/ /_/\_\   version 1.5.2
      /_/

Using Python version 2.7.11 (default, Dec  6 2015 18:57:58)
SparkContext available as sc, HiveContext available as sqlContext.
>>> sc
<pyspark.context.SparkContext object at 0x10396d910>
>>> 
```

---

### Running Spark Using Jupyter Notebook

To start IPython Notebook with the pyspark profile, run:  
`$ ipython notebook --profile=pyspark`  

To test that PySpark was loaded properly, create a new notebook and run `sc` in one of the code cells to make sure the SparkContext object was initialized properly.  
`$ sc `





