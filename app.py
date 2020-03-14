import streamlit as st 
import sqlite3 

st.title('best selling books')
conn =sqlite3.connect('Nyt.db')

cursor=conn.cursor()
st.slider('slider')


import pandas as pd
def all_title():
    titles = pd.read_sql("""Select distinct g.title from google_data g join NYT_BS_2009to2019 nyt on g.isbn=nyt.primary_isbn13 order by g.title""", conn).to_dict('records')
    books = titles # fill in here
    return books

books=all_title()
st.write(books[0])

st.multiselect('pick a title',books)