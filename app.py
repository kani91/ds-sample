import streamlit as st 
import sqlite3 
import pandas as pd

st.title('best selling books')

conn =sqlite3.connect('Nyt.db')
cursor=conn.cursor()

st.header('select dates')
st.slider('slider')



titles = pd.read_sql("""Select distinct g.title from google_data g join NYT_BS_2009to2019 nyt on g.isbn=nyt.primary_isbn13 order by g.title""", conn).to_dict('records')
    books = titles # fill in here
    return books

books=all_title()
st.write(books[0])

st.multiselect('pick a title',books)

#getting the scatter plot 

#1. define sql 
record_scatter=pd.read_sql("""Select 
                                primary_isbn13, g.title,author,categories,
                                min(rank),
                                count(distinct date),
                                g.ratingsCount,averageRating
                            FROM  NYT_BS_2009to2019 nyt 
                            join g_data g 
                            on g.isbn=nyt.primary_isbn13
                            group by primary_isbn13, g.title,author,categories""", conn).to_dict('records')

#2. get lists
ranks=[record['min(rank)'] for record in record_scatter]
length=[record['count(distinct date)'] for record in record_scatter]
title=[record['title'] for record in record_scatter]
author=[record['author'] for record in record_scatter]
categories=[record['categories'] for record in record_scatter]

#3. create plot
fig = px.scatter(x=ranks, y=length,hover_data=[title,author,categories])
fig.show()