#!/usr/bin/env python
# coding: utf-8

# # Data Visualization with Matplotlib

# In this practice you will learn:
# * How to Manipulate data using Python
# * How to Manipulate data using SQL
# * Create Basic Plot with Matplotlib
# * Study Case

# ### <font color='darkred'>A. Library Used</font>

# * `pandas` is a Python library used for working with data sets. It has functions for analyzing, cleaning, exploring, and manipulating data.
# * `pandasql` allows you to query pandas DataFrames using SQL syntax. It works similarly to sqldf in R .
# * `NumPy` which stands for Numerical Python, is a library consisting of multidimensional array objects and a collection of routines for processing those arrays. Using NumPy, mathematical and logical operations on arrays can be performed.
# * `matplotlib` is a low level graph plotting library in python that serves as a visualization utility

# In[7]:


# A.1 installing package
'''
!pip install pandas
!pip install pandasql
!pip install numpy
!pip install matplotlib
'''


# In[6]:


import pandas as pd
import pandasql as ps
import numpy as np
import matplotlib.pyplot as plt


# ### <font color='darkred'>B. Basic Plotting with Matplotlib</font>

# Workflow:
# 1. Import Package
# 2. Prepare the Data
# 3. Creating plot
# 4. Show Plot

# #### <font color='darkgreen'>B.1 Basic Line Chart with Dummy data</font>

# Semisal kita mempunyai data
# * `X1` dengan isi dari datanya adalah (1,3,5,7,9,11)
# * `Y1` dengan isi dari datanya adalah (1,9,25,49,81,121)
# * `X2` dengan isi dari datanya adalah (3,4,16,18,20,22)
# * `Y2` dengan isi dari datanya adalah (2,12,30,56,90,132)

# In[8]:


#1. Import Package nya
import numpy as np
import matplotlib.pyplot as plt

#2. Prepare the data
x1 = np.array([1,2,5,7,9,11])
y1 = np.array([1,9,20,49,81,121])
x2 = np.array([3,4,16,18,20,22])
y2 = np.array([2,12,30,56,90,132])

#3. Creating plot
plt.plot(x1,y1)
plt.plot(x2,y2)

#4. Show plot
plt.show()


# #### <font color='darkgreen'>B.2 Set Color & Marker</font>

# * untuk mengatur langsung marker maupun warna dari suatu plot, bisa langsung menggunakan fungsi yang ada di `plot()`
# * untuk formatnya pengaturan marker, line & color, urutannya adalah `fmt = '[marker][line][color]'`
# 
# more info: [matplotlib plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html)

# In[11]:


#1. Import Package nya
import numpy as np
import matplotlib.pyplot as plt

#2. Prepare the data
x1 = np.array([1,2,5,7,9,11])
y1 = np.array([1,9,20,49,81,121])
x2 = np.array([3,4,16,18,20,22])
y2 = np.array([2,12,30,56,90,132])

#3. Creating plot
plt.plot(x1,y1,'y')
plt.plot(x2,y2,'or:')

#4. Show plot
plt.show()


# #### <font color='darkgreen'>B.3 Set Properties</font>

# Untuk mengatur properties seperti warna, tipe garis, ketebalan garis dll, bisa menggunakan fungsi `setp()`
# more info: [matplotlib setp](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.setp.html)

# In[17]:


# 1. Import Package nya
import numpy as np
import matplotlib.pyplot as plt 

# 2. Prepare the Data
x1 = np.array([1,2,5,7,9,11])
y1 = np.array([1,9,20,49,81,121])
x2 = np.array([3,4,16,18,20,22])
y2 = np.array([2,12,30,56,90,132])

# 3. Creating plot
plot1 = plt.plot(x1,y1)
plot2 = plt.plot(x2,y2)

# setting properties
plt.setp(plot1,color='r', linestyle='-',  linewidth=0.15)
plt.setp(plot2,color='b', linestyle='-.', linewidth=4)

# 4. Show plot
plt.show()


# #### <font color='darkgreen'>B.4 Set Axis</font>

# Untuk mengatur ukuran axis, maka bisa menggunakan fungsi `axis()`
# 
# more info: [matplotlib axis](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axis.html)

# In[18]:


#1. Import Package nya
import numpy as np
import matplotlib.pyplot as plt

#2. Prepare the data
x1 = np.array([1,2,5,7,9,11])
y1 = np.array([1,9,20,49,81,121])
x2 = np.array([3,4,16,18,20,22])
y2 = np.array([2,12,30,56,90,132])

#3. Creating plot
plt.plot(x1,y1)
plt.plot(x2,y2)

#set axis, minimum & maximum (X,Y)
plt.axis([0,20,1,100])

#4. Show plot
plt.show()


# #### <font color='darkgreen'>B.5 Set Label</font>

# * Untuk memberi title di Judul, maka bisa menggunakan fungsi `title()`, more info: [matplotlib title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html)
# * Untuk memberi label di sumbu X, maka bisa menggunakan fungsi `xlabel()`, more info: [matplotlib xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html)
# * Untuk memberi label di sumbu Y, maka bisa menggunakan fungsi `ylabel()`, more info: [matplotlib ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html)

# In[19]:


#1. Import Package nya
import numpy as np
import matplotlib.pyplot as plt

#2. Prepare the data
x1 = np.array([1,2,5,7,9,11])
y1 = np.array([1,9,20,49,81,121])
x2 = np.array([3,4,16,18,20,22])
y2 = np.array([2,12,30,56,90,132])

#3. Creating plot
plt.plot(x1,y1)
plt.plot(x2,y2)

#set Label
plt.title('Ini adalah judul dari Plot')
plt.xlabel('Label sumbu X')
plt.ylabel('Label sumbu Y')

#4. Show plot
plt.show()


# #### <font color='darkgreen'>B.6 Add text</font>

# Untuk memberi text tambahan pada plot, maka bisa menggunakan fungsi `text()`, more info: [matplotlib text](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.text.html)

# In[20]:


#1. Import Package nya
import numpy as np
import matplotlib.pyplot as plt

#2. Prepare the data
x1 = np.array([1,2,5,7,9,11])
y1 = np.array([1,9,20,49,81,121])
x2 = np.array([3,4,16,18,20,22])
y2 = np.array([2,12,30,56,90,132])

#3. Creating plot
plt.plot(x1,y1)
plt.plot(x2,y2)

#Add text
plt.text(4,80, 'line plot 1')
plt.text(13,60, 'line plot 2')

#4. Show plot
plt.show()


# #### <font color='darkgreen'>B.7 Add Legend</font>

# Untuk menambahkan legend pada plot, maka bisa menggunakan fungsi `legend()`, more info: [matplotlib legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html)

# In[23]:


#1. Import Package nya
import numpy as np
import matplotlib.pyplot as plt

#2. Prepare the data
x1 = np.array([1,2,5,7,9,11])
y1 = np.array([1,9,20,49,81,121])
x2 = np.array([3,4,16,18,20,22])
y2 = np.array([2,12,30,56,90,132])

#3. Creating plot
plt.plot(x1,y1, label='line 1')
plt.plot(x2,y2, label='line 2')

# Add legend
# plt.legend()
#lokasi legend geser
#plt.legend(loc="lower right")
plt.legend(bbox_to_anchor=(1.3,0.2))

#4. Show plot
plt.show()


# #### <font color='darkgreen'>B.8 Change Ticks</font>

# * Untuk merubah ticks pada sumbu X maka bisa menggunakan fungsi `xticks()`, more info: [matplotlib xticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xticks.html)
# * Untuk merubah ticks pada sumbu Y maka bisa menggunakan fungsi `yticks()`, more info: [matplotlib yticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.yticks.html)

# In[26]:


#1. Import Package nya
import numpy as np
import matplotlib.pyplot as plt

#2. Prepare the data
x1 = np.array([1,2,5,7,9,11])
y1 = np.array([1,9,20,49,81,121])
x2 = np.array([3,4,16,18,20,22])
y2 = np.array([2,12,30,56,90,132])

#3. Creating plot
plt.plot(x1,y1)
plt.plot(x2,y2)

#Change ticks
#plt.xticks([3,6,10,15])
#plt.yticks([0,25,50,75,100],['dikit banget','dikit','sedang','banyak','banyak banget'])

plt.xticks([3,7,9,17],['dikit lah','mayan','mayan lah','mayan banget'],rotation=40)
plt.yticks([0,25,50,75,100],['dikit banget','dikit','sedang','banyak','banyak banget'])


#4. Show plot
plt.show()


# #### <font color='darkgreen'>B.9 Add Grid</font>

# Untuk memenambahkan grid pada grafik maka bisa menggunakan fungsi `grid()`, more info: [matplotlib grid](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.grid.html)

# In[1]:


#1. Import Package nya
import numpy as np
import matplotlib.pyplot as plt

#2. Prepare the data
x1 = np.array([1,2,5,7,9,11])
y1 = np.array([1,9,20,49,81,121])
x2 = np.array([3,4,16,18,20,22])
y2 = np.array([2,12,30,56,90,132])

#3. Creating plot
plt.plot(x1,y1)
plt.plot(x2,y2)
#Add grid
#plt.grid()
plt.grid(color='grey', linestyle=':', linewidth=0.5)

#4. Show plot
plt.show()


# #### <font color='darkgreen'>B.10 Custome spine</font>

# Untuk merubah spine (garis tepi) pada grafik maka bisa menggunakan fungsi `spines()`, more info: [matplotlib spines](https://matplotlib.org/stable/api/spines_api.html)

# In[2]:


# 1. Import Package
import numpy as np
import matplotlib.pyplot as plt 

# 2. Prepare the Data
x1 = np.array([1,2,5,7,9,11])
y1 = np.array([1,9,20,49,81,121])
x2 = np.array([3,4,16,18,20,22])
y2 = np.array([2,12,30,56,90,132])

# 3. Creating plot
plt.plot(x1,y1)
plt.plot(x2,y2)
# Custome spines
#plt.spines()

ax = plt.gca()
'''
ax.spines['left'].set_color('green')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_color('green')
ax.spines['top'].set_color('none')
'''
'''
ax.spines['left'].set_position(('data',180))
ax.spines['bottom'].set_position(('data',0))
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
'''
ax.spines['left'].set_position(('data',5))
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position(('data',30))
ax.spines['top'].set_color('none')

# 4. Show plot
plt.show()


# #### <font color='darkgreen'>B.11 Save Plot</font>

# Untuk menyimpan maka bisa menggunakan fungsi `savefig()`, more info: [matplotlib savefig](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html)

# In[3]:


# 1. Import Package
import numpy as np
import matplotlib.pyplot as plt 

# 2. Prepare the Data
x1 = np.array([1,2,5,7,9,11])
y1 = np.array([1,9,20,49,81,121])
x2 = np.array([3,4,16,18,20,22])
y2 = np.array([2,12,30,56,90,132])

# 3. Creating plot
plt.plot(x1,y1)
plt.plot(x2,y2)
plt.savefig('trial_save1.png')

# 4. Show plot
plt.show()


# ### <font color='darkred'>C. Working & plotting with Data</font>

# Berikut ini tampilan data transaksi supermarket kita sepanjang tahun 2019, lengkap dengan masing-masing penjelasannya untuk tiap kolom.
# * `order_id` : ID dari order/transaksi, 1 transaksi bisa terdiri dari beberapa produk, tetapi hanya dilakukan oleh 1 customer
# * `order_date` : tanggal terjadinya transaksi
# * `customer_id` : ID dari pembeli, bisa jadi dalam satu hari, 1 customer melakukan transaksi beberapa kali
# * `city` : kota tempat toko terjadinya transaksi
# * `province` : provinsi (berdasarkan city)
# * `product_id` : ID dari suatu product yang dibeli
# * `brand` : brand/merk dari product. Suatu product yang sama pasti memiliki brand yang sama
# * `quantity` : Kuantitas/banyaknya product yang dibeli
# * `item_price` : Harga dari 1 product (dalam Rupiah). Suatu product yang sama, bisa jadi memiliki harga yang berbeda saat dibeli
# ​
# ​
# location data:
# https://storage.googleapis.com/dqlab-dataset/retail_raw_reduced.csv

# In[9]:


import pandas as pd


# In[18]:


dataset = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/retail_raw_reduced.csv')


# #### <font color='darkgreen'>C.1 Case Study 1</font>

# Tampilkan GMV dari bulan ke bulannya. Dimana GMV didapat dari perkalian antara `item_price` & `quantity`

# <details><summary>Click here for the Clue</summary>
# 
# * Buat kolom baru format bulan saja
# * Buat kolom baru GMV
# * Totalkan GMV berdasarkan bulan, buat dataframe baru
# * Plot menggunakan line chart
# 
# </details>

# In[19]:


# Penambahan variable GMV
dataset['gmv'] = dataset['item_price']*dataset['quantity']


# In[20]:


# penambahan variable month
dataset['order_month'] = dataset['order_date'].str.slice(0, 7)


# In[17]:


# buat dataframe baru untuk line chart
monthly_agg_df = dataset.groupby('order_month')['gmv'].sum().reset_index()
monthly_agg_df


# In[21]:


# perbesar figsize
plt.figure(figsize=(20,10))

# membuat line plot
plt.plot(monthly_agg_df['order_month'], monthly_agg_df['gmv'])

# set title & label
plt.title('GMV Value in 2019',color='darkblue', fontsize=17)
plt.xlabel('Order Month',fontsize=13,color='darkred')
plt.ylabel('Total GMV (million)',fontsize=13,color='darkred')

# set xticks & yticks
ytick_label,location = plt.yticks()
plt.yticks(ytick_label, (ytick_label/1000000000).astype(int))
plt.xticks(rotation=20,fontsize=9)

# custom line
plot_line = plt.plot(monthly_agg_df['order_month'], monthly_agg_df['gmv'])
plt.setp(plot_line, color='blue', linestyle='-',  linewidth=2, marker='o')

# set start 0 y axis
plt.ylim(ymin=0)

# set grid
plt.grid(color='darkgray', linestyle=':', linewidth=0.5)

# add text
plt.text(2.7,4000000000, 'Peningkatan GMV ada \n di bulan 09 ke 10', color='darkred')

# save pict
plt.savefig('case_study1.png')

plt.show()


# #### <font color='darkgreen'>C.2 Case Study 2</font>

# Tampilkan komposisi dari kota penyumbang GMV terbesar di provinsi jawa tengah & Jawa Timur. (pilih 5 kota terbesar saja) more info: [matplotlib savefig](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pie.html)

# <details><summary>Click here for the Clue</summary>
# 
# * Filter dulu yang daerah jawa tengah
# * Total GMV berdasakan kota, cari yang 5 kota terbesar
# * Buat Dataframe nya
# * Plot menggunakan pie chart, funsgi pie()
# 
# </details>

# In[25]:


import pandasql as ps


# In[26]:


# create data
pie_df = ps.sqldf("""select city, sum(gmv) as total_gmv
            from dataset 
            where province='Jawa Tengah' or province='Jawa Timur'
            group by city
            order by total_gmv desc
        """)


# In[27]:


#perbesar figsize
plt.figure(figsize=(7,7))

# slicing bagian
myexplode = [0.1, 0, 0, 0,0]

#Plotting
plt.pie(pie_df['total_gmv'],labels = pie_df['city'] ,autopct='%1.1f%%', explode=myexplode ,startangle=90, textprops={'fontsize': 14}, labeldistance=None)

# set title & label
plt.title('GMV Contribution Per City - Jawa Tengah & Jawa Timur in Q4 2019',loc='center', pad=20, fontsize=12, color='blue')

#legend
plt.legend(bbox_to_anchor=(1.3,0.2))

#add text
plt.text(-1,1, 'Semarang', color='darkred', fontsize=12)

# save pict
plt.savefig('case_study2.png')

# tampilkan plot
plt.show()


# #### <font color='darkgreen'>C.3 Case Study 3</font>

# Diasumsikan quantity dari transaksi per customer sangat mempengaruhi dengan besarnya GMV yang dihasilkan. Aapakah benar ?

# <details><summary>Click here for the Clue</summary>
# 
# * Grup kan berdasarkan customer_id, hitung total gmv nya & total quantitynya
# * Buat Dataframe nya
# * Plot menggunakan scatter plot dan line plot untuk bantu polanya gunakan fungsi plot()
# 
# </details>

# In[28]:


# persiapan data
dataset_customer = dataset.groupby('customer_id').agg({'quantity':'sum','gmv':'sum'}).reset_index()
dataset_customer


# In[29]:


plt.figure(figsize=(10,10))

#create Plot 1 (Scatter plot)
plt.plot(dataset_customer['quantity'], dataset_customer['gmv'], 'o', markersize=6)

# set title & label
plt.title('Quantity vs GMV of Customer',color='darkblue', fontsize=17)
plt.xlabel('Total Quantity',fontsize=13,color='darkred')
plt.ylabel('Total GMV (billion)',fontsize=13,color='darkred')

# set xticks & yticks
ytick_label,location = plt.yticks()
plt.yticks(ytick_label, (ytick_label/1000000).astype(int))
plt.xticks(rotation=20,fontsize=9)

# set start 0 y axis
plt.ylim(ymin=0,ymax=200000000)
plt.xlim(xmin=0,xmax=300)

#Create Plot 2 (line Plot) Equation line
#obtain m (slope) and b(intercept) of linear regression line
x = dataset_customer['quantity']
y = dataset_customer['gmv']
m, b = np.polyfit(x, y, 1)
plt.plot(x, m*x+b)

# set grid
plt.grid(color='darkgray', linestyle=':', linewidth=0.5)

# Hilangkan garis tepi
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# save pict
plt.savefig('case_study3.png')

plt.show()


# #### <font color='darkgreen'>C.4 Case Study 4</font>

# Setelah melihat scatter plot tadi, terlihat seperti adanya outlier di GMV customer. Pastikan apakah benar ada outlier ? dan tangani outliernya tanpa menghapus data tersebut

# <details><summary>Click here for the Clue</summary>
# 
# * Buat box plot menggunakan GMV
# * Misal ada outlier, maka handle pakai cap dengan nilai maximal dan minimalnya. Asumsikan saja min nya 0, max nya= 36000000
# * Cek kembali plot nya
# </details>

# In[30]:


plt.figure(figsize=(25,10))

# Creating plot
plt.boxplot(dataset_customer['gmv'], vert=0)

# set xticks & yticks
xtick_label,location = plt.xticks()
plt.xticks(xtick_label, (xtick_label/1000000).astype(int), fontsize=12)

# set title & label
plt.title('Box Plot of GMV (Before)',color='darkblue', fontsize=17)
plt.xlabel('Total GMV (billion)',fontsize=13,color='darkred')
 
# rescale
plt.xlim(xmin=0,xmax=500000000)
    
# show plot
plt.show()


# In[31]:


# Handling Outlier
# Asumsikan nilai maks nya adalah 36000000, sedangkan nilai min nya adalah 0
dataset_customer = ps.sqldf("""select customer_id
                ,quantity
                ,case when gmv > 36000000 then 36000000
                    when gmv < 0 then 0
                    else gmv
                end as gmv
            from dataset_customer limit 100

""")


# In[32]:


plt.figure(figsize=(25,10))

# Creating plot
plt.boxplot(dataset_customer['gmv'], vert=0)

# set xticks & yticks
xtick_label,location = plt.xticks()
plt.xticks(xtick_label, (xtick_label/1000000).astype(int), fontsize=12)

# set title & label
plt.title('Box Plot of GMV (After)',color='darkblue', fontsize=17)
plt.xlabel('Total GMV (billion)',fontsize=13,color='darkred')
 
# rescale
plt.xlim(xmin=0,xmax=38000000)

# save pict
plt.savefig('case_study4.png')

# show plot
plt.show()


# In[ ]:




