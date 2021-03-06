
# coding: utf-8

# In[1]:


import findspark
findspark.init()


# In[2]:


from __future__ import print_function

import sys
from random import random
from operator import add

from pyspark.sql import SparkSession


# In[3]:


if __name__ == "__main__":
   
    spark = SparkSession        .builder        .appName("PythonPi")        .getOrCreate()

    slices = 1 #int(sys.argv[1]) if len(sys.argv) > 1 else 2
    n = 100000 * slices

    def f(_):
        x = random() * 2 - 1
        y = random() * 2 - 1
        return 1 if x ** 2 + y ** 2 <= 1 else 0

    count = spark.sparkContext.parallelize(range(1, n + 1), slices).map(f).reduce(add)
    print("Pi is roughly %f" % (4.0 * count / n))

    spark.stop()

