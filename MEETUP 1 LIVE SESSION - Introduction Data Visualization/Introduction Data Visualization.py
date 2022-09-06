#!/usr/bin/env python
# coding: utf-8

# # Introduction Data Visualization
# 
# 
# In this practice will learn:
# 
# - How to Manipulate data using Python
# - How to Manipulate data using SQL
# - Understanding & Importing Data
# - Selecting Data based on Criteria
# - Grouping & Aggregation
# - Creating new Column based on Criteria

# # A. Library Used

# - pandas is a Python library used for working with data sets. It has functions for analyzing, cleaning, exploring, and manipulating data.
# - pandasql allows you to query pandas DataFrames using SQL syntax. It works similarly to sqldf in R .
# - NumPy which stands for Numerical Python, is a library consisting of multidimensional array objects and a collection of routines for processing those arrays. Using NumPy, mathematical and logical operations on arrays can be performed

# In[8]:


# A.1 installing package
'''
pip install pandas
pip install pandasql
pip install numpy
'''


# In[9]:


# A.2 Importing Package used
import pandas as pd
import pandasql as ps
import numpy as np


# # B. Understanding & Importing Data

# Berikut ini tampilan data transaksi supermarket kita sepanjang tahun 2019, lengkap dengan masing-masing penjelasannya untuk tiap kolom.
# 
# - order_id : ID dari order/transaksi, 1 transaksi bisa terdiri dari beberapa produk, tetapi hanya dilakukan oleh 1 customer
# - order_date : tanggal terjadinya transaksi
# - customer_id : ID dari pembeli, bisa jadi dalam satu hari, 1 customer melakukan transaksi beberapa kali
# - city : kota tempat toko terjadinya transaksi
# - province : provinsi (berdasarkan city)
# - product_id : ID dari suatu product yang dibeli
# - brand : brand/merk dari product. Suatu product yang sama pasti memiliki brand yang sama
# - quantity : Kuantitas/banyaknya product yang dibeli
# - item_price : Harga dari 1 product (dalam Rupiah). Suatu product yang sama, bisa jadi memiliki harga yang berbeda saat dibeli
# 
# location data: https://storage.googleapis.com/dqlab-dataset/retail_raw_reduced.csv

# In[12]:


dataset = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/retail_raw_reduced.csv')


# In[13]:


dataset


# # C. Selecting Data

# C.1 Selecting selected Columns 

# Study Case:
# - Show All data with customer_id column only

# In[14]:


#C.1.1 Using Python
dataset[['customer_id']]


# In[15]:


#C.1.2 Using SQL run on top Python
ps.sqldf("select customer_id from dataset")


# Question:
# - Show All rows of data with columns (customer_id and city)

# In[17]:


# Using Python 
dataset[['customer_id','city']]


# In[19]:


# Using SQL run on top Python
ps.sqldf("select customer_id, city from dataset")


# C.2 Selecting All Columns top n rows 

# Study Case:
# - Show All data based on top 5 rows

# In[20]:


# C.2.1 Using Python
dataset.head(5)


# In[21]:


# C.2.2 Using SQL run on top Python
ps.sqldf("select * from dataset limit 5")


# Question:
# - Show All data based on top 10 rows

# In[22]:


#Using Python
dataset.head(10)


# In[24]:


# Using SQL run on top Python
ps.sqldf("select * from dataset limit 10")


# C.3 See unique value of Column 

# In[25]:


# C.3.1 Using Python
dataset['brand'].unique()


# In[26]:


# C.3.2 Using SQL run on top Python
ps.sqldf("select distinct brand from dataset")


# C.4 Filtering Rows by Criteria of Column 

# Study Case:
# - Show row of data which quantity of transaction is more than 500
# - Show row of data which province of transaction is in Jawa Timur

# In[28]:


# C.4.1 Using Python
dataset[dataset['quantity'] > 500]


# In[29]:


dataset[(dataset['province'] == 'Jawa Timur')]


# In[30]:


# C.4.2 Using SQL run on top Python
ps.sqldf("select * from dataset where quantity > 500")


# In[31]:


ps.sqldf("select * from dataset where province='Jawa Timur'")


# Question:
# - Show row of data where located in Jawa Timur and quantity of transaction is more than 500

# In[32]:


#Using Python 
dataset[(dataset['province'] == 'Jawa Timur') & (dataset['quantity'] > 400)]


# In[35]:


ps.sqldf("select * from dataset where province='Jawa Timur' and quantity > 500")


# # D. Grouping & Agregating Data 

# Function in Python
# - group()-> Grouping columns
# - count()-> Compute count of group
# - mean()-> Compute mean of groups
# - sum()-> Compute sum of group values
# - min()-> Compute min of group values
# - max()-> Compute max of group values
# 
# Function in SQL
# - group by-> Grouping columns
# - count()-> Compute count of group
# - avg()-> Compute mean of groups
# - sum()-> Compute sum of group values
# - min()-> Compute min of group values
# - max()-> Compute max of group values

# Study Case:
# - Show how many data available based on brand
# - Show average quantity transaction based on brand

# In[38]:


# D.4.1 Using Python
dataset.groupby(['brand'])['brand'].count()


# In[39]:


dataset.groupby(['brand'] ,as_index=False)['quantity'].mean()


# In[40]:


# D.4.2 Using SQL run on top Python
ps.sqldf("select brand, count(brand) from dataset group by brand")


# In[41]:


ps.sqldf("select brand, avg(quantity) from dataset group by brand")


# #### Question:
# - Show total quantity of transaction based on Brand & province

# In[42]:


# Using Python
dataset.groupby(['brand','province'] ,as_index=False)['quantity'].sum()


# In[43]:


#Using SQL run on top Python
ps.sqldf("select brand, province, sum(quantity) from dataset group by brand,province")


# # E. Creating New Column based on Condition 

# #### Study Case:
# * Add new column called desc_brand, based on column brand, here are the condition:

# |brand|desc_brand|
# |---|---|
# |BRAND_A|Marimas|
# |BRAND_B|Finto|
# |BRAND_C|Indomilk|
# |BRAND_H|Jas Jus|
# |BRAND_J|Taro|
# |BRAND_L|Chiki|
# |BRAND_P|Hot Hot Pop|
# |BRAND_R|Jagoan Neon|
# |BRAND_S|Sakura|
# |BRAND_W|Yosan|

# In[50]:


# E.1 Using Python
# Define Condition
conditions = [
    (dataset['brand'] == 'BRAND_A'),
    (dataset['brand'] == 'BRAND_B'),
    (dataset['brand'] == 'BRAND_C'),
    (dataset['brand'] == 'BRAND_H'),
    (dataset['brand'] == 'BRAND_J'),
    (dataset['brand'] == 'BRAND_L'),
    (dataset['brand'] == 'BRAND_P'),
    (dataset['brand'] == 'BRAND_R'),
    (dataset['brand'] == 'BRAND_S'),
    (dataset['brand'] == 'BRAND_W')
    ]
# create a list of the values we want to assign for each condition
values = [
    'Marimas'
    ,'Finto'
    ,'Indomilk'
    ,'Jas Jus'
    ,'Taro'
    ,'Chiki'
    ,'Hot Hot Pop'
    ,'Jagoan Neon'
    ,'Sakura'
    ,'Yosan']
# create a new column and use np.select to assign values to it using our lists as arguments
dataset['desc_brand'] = np.select(conditions, values)
dataset


# In[48]:


# E.2 Using SQL run on top Python
ps.sqldf("""
select *
    ,case when brand='BRAND_A' then 'Marimas'
        when brand='BRAND_B' then 'Finto'
        when brand='BRAND_C' then 'Indomilk'
        when brand='BRAND_H' then 'Jas Jus'
        when brand='BRAND_J' then 'Taro'
        when brand='BRAND_L' then 'Chiki'
        when brand='BRAND_P' then 'Hot Hot Pop'
        when brand='BRAND_R' then 'Jagoan Neon'
        when brand='BRAND_S' then 'Sakura'
        when brand='BRAND_W' then 'Yosan'
    end as desc_brand_sql
from dataset
""")


# #### Question:
# * Add new column called `cat_brand` & `cat_brand_sql` for categoring desc_brand of product with criteria below:

# |desc_brand|cat_brand|
# |---|---|
# |Marimas, Finto, Indomilk, Jasjus|Minuman|
# |Taro, Chiki, Sakura|Makanan Ringan|
# |Hot Hot Pop, Jagoan Neon, Yosan|Permen|
# 

# In[49]:


#  Using Python
# Define Condition
conditions = [
    (dataset['desc_brand'] == 'Marimas') | (dataset['desc_brand'] == 'Finto') | (dataset['desc_brand'] == 'Indomilk') | (dataset['desc_brand'] == 'Jasjus'),
    (dataset['desc_brand'] == 'Taro') | (dataset['desc_brand'] == 'Chiki') | (dataset['desc_brand'] == 'Sakura'),
    (dataset['desc_brand'] == 'Hot Hot Pop') | (dataset['desc_brand'] == 'Jagoan Neon') | (dataset['desc_brand'] == 'Yosan')
    ]
# create a list of the values we want to assign for each condition
values = [
    'Minuman'
    ,'Makanan Ringan'
    ,'Permen']
# create a new column and use np.select to assign values to it using our lists as arguments
dataset['cat_brand'] = np.select(conditions, values)
dataset


# In[51]:


# E.2 Using SQL run on top Python
ps.sqldf("""
select *
    ,case when desc_brand in ('Marimas','Finto','Indomilk','Jas Jus') then 'Minuman'
        when desc_brand in ('Taro','Chiki') then 'Makanan Ringan'
        when desc_brand in ('Hot Hot Pop','Jagoan Neon','Sakura','Yosan') then 'Permen'
    end as desc_brand_sql
from dataset
""")

