#!/usr/bin/env python
# coding: utf-8

# # Isi Modul :
# - Pengolahan dataset (menggunakan library NumPy & Pandas).
# - Membuat grafik dasar menggunakan matplotlib.
# - Melakukan modifikasi komponen visualisasi, seperti axis, labels, - - title, dan legend.
# - Menyimpan plot visualisasi yang sudah dibuat

# # Pengenalan Matplotlib dan Persiapan Dataset

# In[10]:


import pandas as pd
import datetime
import matplotlib.pyplot as plt 

dataset = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/retail_raw_reduced.csv')
print('Ukuran dataset:%d baris dan %d kolom\n' % dataset.shape)
print('Lima data teratas:')
print(dataset.head())


# # Penjelasan Dataset
# - order_id : ID dari order/transaksi, 1 transaksi bisa terdiri dari beberapa produk, tetapi hanya dilakukan oleh 1 customer
# - order_date : tanggal terjadinya transaksi
# - customer_id : ID dari pembeli, bisa jadi dalam satu hari, 1 customer melakukan transaksi beberapa kali
# - city : kota tempat toko terjadinya transaksi
# - province : provinsi (berdasarkan city)
# - product_id : ID dari suatu product yang dibeli
# - brand : brand/merk dari product. Suatu product yang sama pasti memiliki brand yang sama
# - quantity : Kuantitas/banyaknya product yang dibeli
# - item_price : Harga dari 1 product (dalam Rupiah). Suatu product yang sama, bisa jadi memiliki harga yang berbeda saat dibeli

# In[11]:


# Penambahan kolom order month pada dataset
dataset['order_month']=dataset['order_date'].apply(lambda x:datetime.datetime.strptime(x,"%Y-%m-%d").strftime('%Y-%m'))
print(dataset.head())


# In[12]:


#penambahan kolom GMV pada Dataset
dataset['gmv'] = dataset['item_price']*dataset['quantity']
print('Ukuran dataset:%d baris dan %d kolom\n' % dataset.shape)
print('Lima data teratas:')
print(dataset.head())


# In[13]:


#Membuat data agregat
monthly_amount = dataset.groupby('order_month')['gmv'].sum().reset_index()
print(monthly_amount)


# In[14]:


#Membuat line chart trend pertumbuhan GMV
plt.plot(monthly_amount['order_month'],monthly_amount['gmv'])
plt.show


# In[16]:


#Membuat line chart dengan fungsi.plot() pada pandas dataframe
dataset['order_month'] = dataset['order_date'].apply(lambda x: datetime.datetime.strptime(x, "%Y-%m-%d").strftime('%Y-%m'))
dataset['gmv'] = dataset['item_price']*dataset['quantity']

dataset.groupby(['order_month'])['gmv'].sum().plot()
plt.show()


# # Anatomi dari Figure
# Ada beberapa istilah dan komponen di sebuah plot, nanti akan mempermudah mengingat function apa yang digunakan untuk memodifikasinya.
# 
# - Figure adalah keseluruhan visualisasi yang kita plot dalam 1 kali menjalankan code.
# - Sedangkan satu plot (yang dibuat saat memanggil .plot() atau .scatter()) disebut Axes. Sebuah Figure bisa terdiri dari beberapa Axes. 
# - Setiap Axes biasanya memiliki sumbu-X (X-axis) dan sumbu-Y (Y-axis). Masing-masing sumbu memiliki komponen sebagai berikut:
#     - Axis Label: Nama dari sumbu yang ditampilkan.
#     - Tick: Penanda berupa titik/garis kecil yang berjajar di sumbu, sebagai referensi skala nilai.
#     - Tick Label: Tulisan di tiap tick yang menyatakan nilainya.
# - Untuk isi grafiknya sendiri, bisa berupa line (untuk line plot), atau marker (untuk scatter plot), bisa juga bentuk lain seperti bar (untuk bar plot/histogram).
# - Aksesoris lain yang bisa ditambahkan, di antaranya Grid untuk mempermudah melihat tick yang sejajar, dan Text untuk memberikan informasi tambahan berbentuk teks di grafik.
# 
# Memahami komponen-komponen di atas sudah cukup untuk melakukan berbagai visualisasi dengan matplotlib. Untuk anatomi yang lebih lengkap, bisa dilihat di link berikut: https://matplotlib.org/3.1.3/gallery/showcase/anatomy.html.

# In[17]:


# mengubah fitur size 
plt.figure(figsize=(15,5))
dataset.groupby(['order_month'])['gmv'].sum().plot()
plt.show()


# In[18]:


# menambahkan title and axis labels
plt.figure(figsize=(15,5))
dataset.groupby(['order_month'])['gmv'].sum().plot()

plt.title('Monthly GMV Year 2019')
plt.xlabel('Order Month')
plt.ylabel('Total GMV')
plt.show()


# # Kustomisasi Title and Axis Labels
# untuk judul/title, parameter yang bisa ditambahkan:
# 
# - loc: digunakan untuk menentukan posisi title, misalnya ‘left’ untuk membuat rata kiri, ‘right’ untuk rata kanan, dan ‘center’ untuk meletakkannya di tengah. Jika tidak didefinisikan, maka default-nya title ada di tengah.
# - pad: digunakan untuk menambahkan jarak antara judul ke grafik (dalam satuan px), misalnya kita tidak ingin judulnya terlalu menempel dengan grafiknya, jadi kita beri jarak.
# - fontsize: digunakan untuk mengganti ukuran font/huruf (dalam satuan px).
# - color: digunakan untuk mengganti warna huruf judul. Kita bisa menggunakan warna dasar dengan kata seperti ‘blue’, ‘red’, ‘orange’, dsb. Bisa juga dengan hex string, misalnya '#42DDF5' untuk warna biru muda.
# 
# Untuk xlabel dan ylabel, kita bisa mengganti fontsize dan color, tetapi tidak bisa mengganti loc. 

# In[19]:


plt.figure(figsize=(15, 5))
dataset.groupby(['order_month'])['gmv'].sum().plot()
plt.title('Monthly GMV Year 2019', loc='center', pad=20, fontsize=20, color='blue')
plt.xlabel('Order Month', fontsize=15)
plt.ylabel('Total Amount', fontsize=15)
plt.show()


# # Kustomisasi Line dan Point
# Beberapa parameter yang bisa dikustomisasi:
# 
# - color: mengubah warnanya (sama seperti di title)
# - linewidth: mengubah ketebalan line/garisnya (dalam satuan px)
# - linestyle: mengubah jenis dari garis. Misalnya '-' atau 'solid' untuk garis tak terputus (seperti pada default), '--' atau 'dashed' untuk garis putus-putus, ':' atau 'dotted' untuk garis berupa titik-titik, bisa juga '-.' atau ‘dashdot’ untuk garis dan titik bergantian.
# - marker: mengubah tipe points/titik data di chart. Ada banyak sekali kemungkinan nilai untuk marker ini, yang biasanya digunakan yaitu ‘.’ untuk bulatan kecil/titik, ‘o’ untuk bulatan agak besar, ‘s’ untuk persegi, ‘D’ untuk diamond/wajik, dan bentuk-bentuk lain seperti ‘+’, ‘x’, ‘|’, ‘*’.
#  

# In[20]:


plt.figure(figsize=(15, 5))
dataset.groupby(['order_month'])['gmv'].sum().plot(color='green', marker='o', linestyle='-.', linewidth=2)
plt.title('Monthly GMV Year 2019', loc='center', pad=20, fontsize=20, color='blue')
plt.xlabel('Order Month', fontsize=15)
plt.ylabel('Total Amount', fontsize=15)
plt.show()


# # Kustomisasi Grid

# In[22]:


plt.figure(figsize=(15, 5))
dataset.groupby(['order_month'])['gmv'].sum().plot(color='green', marker='o', linestyle='-.', linewidth=2)
plt.title('Monthly GMV Year 2019', loc='center', pad=20, fontsize=20, color='blue')
plt.xlabel('Order Month', fontsize=15)
plt.ylabel('Total Amount', fontsize=15)
plt.grid(color='darkred', linestyle=':', linewidth=0.5)
plt.show()


# # Kustomisasi Axis Ticks

# In[23]:


plt.figure(figsize=(15, 5))
dataset.groupby(['order_month'])['gmv'].sum().plot(color='green', marker='o', linestyle='-.', linewidth=2)
plt.title('Monthly GMV Year 2019', loc='center', pad=20, fontsize=20, color='blue')
plt.xlabel('Order Month', fontsize=15)
plt.ylabel('Total Amount (in Billions)', fontsize=15)
plt.grid(color='darkgray', linestyle=':', linewidth=0.5)
labels, locations = plt.yticks()
plt.yticks(labels, (labels/1000000000).astype(int))
plt.show()


# In[24]:


# Menentukan Batas Minimum dan Maksimum Axis Ticks
plt.figure(figsize=(15, 5))
dataset.groupby(['order_month'])['gmv'].sum().plot(color='green', marker='o', linestyle='-.', linewidth=2)
plt.title('Monthly GMV Year 2019', loc='center', pad=20, fontsize=20, color='blue')
plt.xlabel('Order Month', fontsize=15)
plt.ylabel('Total Amount (in Billions)', fontsize=15)
plt.grid(color='darkgray', linestyle=':', linewidth=0.5)
plt.ylim(ymin=0)
labels, locations = plt.yticks()
plt.yticks(labels, (labels/1000000000).astype(int))
plt.show()


# # Menambahkan Informasi Pada Plot

# In[25]:


fig = plt.figure(figsize=(15, 5))
dataset.groupby(['order_month'])['gmv'].sum().plot(color='green', marker='o', linestyle='-.', linewidth=2)
plt.title('Monthly GMV Year 2019', loc='center', pad=20, fontsize=20, color='blue')
plt.xlabel('Order Month', fontsize=15)
plt.ylabel('Total Amount (in Billions)', fontsize=15)
plt.grid(color='darkgray', linestyle=':', linewidth=0.5)
plt.ylim(ymin=0)
labels, locations = plt.yticks()
plt.yticks(labels, (labels/1000000000).astype(int))
plt.text(0.45, 0.72, 'The GMV increased significantly on October 2019', transform=fig.transFigure, color='red')
plt.show()


# # Menyimpan Hasil Plot Menjadi File Image

# In[26]:


plt.gcf().canvas.get_supported_filetypes()


# In[27]:


plt.savefig('monthly_gmv.png')


# # Pengaturan Parameter untuk Menyimpan Gambar
# Ada berbagai parameter yang bisa diatur saat menyimpan gambar, antara lain:
# 
# - dpi: Resolusi gambar (dots per inch). 
# - quality: Kualitas gambar (hanya berlaku jika formatnya jpg atau jpeg), bisa diisi nilai 1 (paling buruk) hingga 95 (paling bagus).
# - facecolor: Memberikan warna bagian depan figure, di luar area plot 
# - edgecolor: Memberikan warna pinggiran gambar
# - transparent: Jika nilainya True, maka gambarnya jadi transparan (jika file-nya png)
#  
# Tapi biasanya, parameter-parameter ini tidak digunakan karena grafik di file gambar bisa jadi berbeda dengan yang muncul saat menjalankan code di python.
# 

# In[ ]:


plt.savefig('monthly_gmv.png', quality=95)


# # Mini Project

# Studi Kasus dari Senja: Daily number of customers on Desember
# Dengan menggunakan dataset yang sama ('https://storage.googleapis.com/dqlab-dataset/retail_raw_reduced.csv'), buatlah sebuah line chart dengan Matplotlib, yang menunjukkan jumlah pembeli harian (daily number of customers) selama bulan Desember.
# 
# Beberapa spesifikasi yang harus diperhatikan:
# 
# - Ukuran figure adalah 10x5
# - Sumbu-x adalah tanggal pembelian, dari tanggal 1 - 31 Desember 2019
# - Sumbu-y adalah jumlah unique customers di tiap tanggal
# - Title dan axis label harus ada, tulisan dan style-nya silakan disesuaikan sendiri

# In[1]:


# Import library yang dibutuhkan
import datetime
import pandas as pd
import matplotlib.pyplot as plt
# Baca dataset https://storage.googleapis.com/dqlab-dataset/retail_raw_reduced.csv
dataset = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/retail_raw_reduced.csv')
# Buat kolom order_month
dataset['order_month'] = dataset['order_date'].apply(lambda x: datetime.datetime.strptime(x, "%Y-%m-%d").strftime('%Y-%m'))
# Buat kolom gmv
dataset['gmv'] = dataset['item_price'] * dataset['quantity']
# Plot grafik sesuai dengan instruksi
plt.figure(figsize=(10, 5))
dataset[dataset['order_month']=='2019-12'].groupby(['order_date'])['customer_id'].nunique().plot(color='red', marker='.', linewidth=2)
plt.title('Daily Number of Customers - December 2019', loc='left', pad=20, fontsize=20, color='orange')
plt.xlabel('Order Date', fontsize=15, color='blue')
plt.ylabel('Number of Customers', fontsize=15, color='blue')
plt.grid(color='darkgray', linestyle=':', linewidth=0.5)
plt.ylim(ymin=0)
plt.show()

