from datetime import date
import sqlite3
import pandas as pd
from Functions import Get_best_selling_books_multiple

conn =sqlite3.connect('Nyt.db')

start_date = date(2009, 12, 31)
end_date = date(2009, 12, 31)
query_bk_type="hardcover-nonfiction"


def store_books(start_date, query_date_end, query_bk_type):
    books=Get_best_selling_books_multiple(query_date_start = start_date,query_date_end=end_date ,query_bk_type=query_bk_type)
    full_list_df =pd.concat(books)
    return full_list_df
    


# full_list.to_sql('bestsellers',conn)