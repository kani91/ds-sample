attribute_set=['title','weeks_on_list','primary_isbn13','publisher','author','rank','book_image_height','book_image_width','price','isbns','buy_links','book_image','amazon_product_url']

start_date = date(2018, 12, 31)
end_date = date(2019, 12, 31)

query_bk_type="hardcover-nonfiction"


books=Get_best_selling_books_multiple(start_date,query_date_end=end_date ,query_bk_type="hardcover-nonfiction")

full_list=pd.concat(books)

import sqlite3
conn =sqlite3.connect('Nyt.db')


sql_file=full_list.to_sql('bestsellers',conn)

cursor=conn.cursor()
cursor.execute('SELECT name from sqlite_master where type= "table"')
cursor.fetchall()
