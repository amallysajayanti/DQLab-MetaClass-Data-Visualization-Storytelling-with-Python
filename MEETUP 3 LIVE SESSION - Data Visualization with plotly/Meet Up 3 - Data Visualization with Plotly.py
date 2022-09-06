#!/usr/bin/env python
# coding: utf-8

# # Meet Up 3 - Data Visualization with Plotly

# In this practice you will learn:
# * Plotting with Plotly
# * Basic Dash
# * Dash Callback

# ### <font color='darkred'>A. Library Used</font>

# * `pandas` is a Python library used for working with data sets. It has functions for analyzing, cleaning, exploring, and manipulating data.
# * `pandasql` allows you to query pandas DataFrames using SQL syntax. It works similarly to sqldf in R .
# * `plotly` is an interactive, open-source plotting library that supports over 40 unique chart types covering a wide range of statistical visualization
# * `dash` is an open source framework for building data visualization interfaces

# In[ ]:


# A.1 installing package
'''
!pip install pandas
!pip install pandasql
!pip install plotly
!pip install dash
'''


# In[4]:


# Library data manipulation
import pandas as pd
import pandasql as ps

# Library Data Visualization
import plotly.express as px
import plotly.graph_objects as go

# Library Dashboarding
import dash
#import dash_html_components as html
from dash import html
#import dash_core_components as dcc
from dash import dcc

from dash import Input
from dash import Output


# ### <font color='darkred'>B. Dataset</font>

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
# 
# 
# location data:
# https://storage.googleapis.com/dqlab-dataset/retail_raw_reduced.csv

# In[ ]:


dataset = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/retail_raw_reduced.csv')


# In[7]:


dataset.head()


# ### <font color='darkred'>C. Plotting with Plotly</font>

# Workflow:
# 1. Import Package
# 2. Prepare the Data
# 3. Creating plot
# 4. Show Plot

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

# In[8]:


# penambahahan variable GMV
dataset['gmv'] = dataset['item_price']*dataset['quantity']
dataset.head()


# In[10]:


#penambahan variable month
dataset['order_month'] = dataset['order_date'].str.slice(0,7)
dataset.head()


# In[11]:


# buat dataframe baru untuk line chart
monthly_agg_df = dataset.groupby('order_month')['gmv'].sum().reset_index()
monthly_agg_df


# #### C.1.1 Using Object Go

# In[12]:


#create plot
fig = go.Figure(go.Scatter(x=monthly_agg_df['order_month'] , y= monthly_agg_df['gmv']))
fig.update_layout(title='GMV Value in 2019')

#show plot
fig.show()


# #### C.1.2 Using Express

# In[14]:


#create plot 
fig = px.line(monthly_agg_df, x="order_month", y="gmv", title="GMV Value in 2019", markers=True)

#show plot
fig.show()


# ##### C.1.2.1 Update X & Y label

# In[18]:


#create plot 
fig = px.line(monthly_agg_df, x="order_month", y="gmv", title="GMV Value in 2019", markers=True)

# Update X & Y label
fig.update_yaxes(title_font=dict(size=20, family='arial', color='green'))
fig.update_xaxes(title_font=dict(size=20, family='arial', color='green'))

#show plot
fig.show()


# ##### C.1.2.2 Custom X & Y Ticks

# In[22]:


#create plot 
fig = px.line(monthly_agg_df, x="order_month", y="gmv", title="GMV Value in 2019", markers=True)

#custom X & Y Ticks
fig.update_yaxes(tickvals=[5000000000, 6000000000, 8000000000])
fig.update_xaxes(tickangle=45, tickfont=dict(family='courier', color='brown', size=10))

#show plot
fig.show()


# ##### C.1.2.3 Styling grid lines

# In[27]:


#create plot 
fig = px.line(monthly_agg_df, x="order_month", y="gmv", title="GMV Value in 2019", markers=True)

#styling grid
fig.update_yaxes(showgrid=True)
fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='red')

#show plot
fig.show()


# ##### C.1.2.4 Custom Line & Marker

# In[33]:


# create plot
fig = px.line(monthly_agg_df, x="order_month", y="gmv", title='GMV Value in 2019', markers=True)

# Custom Line
fig.update_traces(line=dict(color="Black", width=0.5),marker=dict(color="Red", size=12))

# Show Plot
fig.show()


# ##### C.1.2.5 Custom Title

# In[38]:


# create plot
fig = px.line(monthly_agg_df, x="order_month", y="gmv", title='GMV Value in 2019', markers=True)

# Modify Title
fig.update_layout(title_font=dict(size=18, color="darkred"), title_x=0.5)

# Show Plot
fig.show()


# #### <font color='darkgreen'>C.2 Case Study 2</font>

# Tampilkan GMV dari bulan ke bulannya untuk kota-kota yang ada di provinsi Jawa Tengah & Jawa Timur

# <details><summary>Click here for the Clue</summary>
# 
# * Filter berdasarkan Provinsi Jawa tengah & Jawa Timur
# * Totalkan GMV berdasarkan bulan, buat dataframe baru
# * Plot menggunakan Multiline chart
# 
# </details>

# In[41]:


#buat dataframe baru unutk multiline chart
monthly_agg_city_df = dataset[(dataset['province'] == 'Jawa Timur') | (dataset['province'] == 'Jawa Tengah')]
monthly_agg_city_df = monthly_agg_city_df.groupby(['order_month','city'])['gmv'].sum().reset_index()
monthly_agg_city_df.head()


# In[ ]:


#create plot
fig = px.line(monthly_agg_city_df, x='order_month', y='gmv', color='city')

#Modify title 
fig.update_layout(title="GMV total per city", title_font=dict(size=25, color="yellow"), title_x=0.5)

#update X & Y label
fig.update_yaxes(title_font=dict(size=15, family='arial', color='blue'))
fig.update_xaxes(title_font=dict(size=15, family='arial', color='blue'))

#show plot
fig.show()


# ### <font color='darkred'>D. Dashboarding with Dash</font>

# #### Workflow:
# 1. Create Dash App
# 2. Design Layout
# 3. Add callback function (if needed)
# 4. Run Application

# #### <font color='darkgreen'>D.1 Basic Dash</font>

# ##### Deploy grafik multichart case ke 2 ke dalam Dash

# In[ ]:


# Create a dash application
app = dash.Dash(__name__)


# Design Layout
app.layout = html.Div(children=[html.H1('Airline Dashboard', style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),
                                html.P('Proportion of distance group (250 mile distance interval group) by flights.', style={'textAlign':'center', 'color': '#F57241'}),
                                dcc.Graph(figure=fig),

                    ])

# Run the application                   
if __name__ == '__main__':
    app.run_server()
    #app.run_server(port=8802, host='127.0.0.1', debug=True)


# #### <font color='darkgreen'>D.2 Dash With Callback</font>

# ##### Deploy grafik multichart case ke 2 ke dalam Dash

# In[ ]:


#show data
monthly_agg_city_df.head()


# In[ ]:


#create list cities
available_cities = monthly_agg_city_df['city'].unique()
available_cities


# In[ ]:


# create the app
app = dash.Dash()

# Design Layout
app.layout = html.Div(children=[html.H1('Dashboard Task 2',style={'textAlign':'center','color': '#5c0f3a','font-size':33}),
                                html.P('Merupakan dashboard menggunakan Interactive Dashboard Callback',style={'textAlign':'center'}),
                                dcc.Dropdown(
                                    id='dropdown-ku',
                                    options=[{'label': k, 'value': k} for k in available_cities],
                                    value=['Surabaya', 'Malang'],
                                    multi=True),
                                html.Hr(),
                                dcc.Graph(id='display-value'),
])

# Callback Function
@app.callback(Output('display-value',component_property='figure')
                ,Input('dropdown-ku',component_property='value'))
def update_output(value):
    dataku = monthly_agg_df_city[monthly_agg_df_city["city"].isin(value)]
    fig = px.line(dataku, x="order_month", y="gmv", color="city")
    return fig
    


# Run the Applicaton
if __name__ == '__main__':
    app.run_server()


# ### <font color='darkred'>F. FINISH !!!</font>

# ### <font color='darkblue'>DOCUMENTATION</font>
# For more information:
# * [Plotly Docs Axes](https://plotly.com/python/axes/#tick-placement-color-and-style)
# * [Plotly Docs Update traces](https://plotly.com/python/creating-and-updating-figures/)
# * [Plotly Docs Express Chart Reference](https://plotly.com/python-api-reference/plotly.express.html)
# * [Dash Docs](https://dash.plotly.com/introduction)

# ### <font color='darkblue'>FAQ</font>

# #### 1. Jupyter notebook cant show the chart of plotly
# 
# * Check the extension plotly in Jupyter with `jupyter labextension list` in terminal
# * Run `jupyter labextension install jupyterlab-plotly` if haven't
# * Restart jupyter program
# 
# #### 2. dash component & html component cant imported
# Latest doc, dash change how to import it, here are the new sytax:
# * `from dash import html`
# * `from dash import dcc`
