import pandas as pd 
from datetime import datetime
import sqlite3
from datetime import timedelta
from datetime import date


def Get_best_selling_books_multiple(query_date_start,query_date_end,query_bk_type):
    list_of_books=[]
    delta = timedelta(days=7)
        
    while query_date_start <= query_date_end:
        date=query_date_start 
        query_bk_type=query_bk_type
        large_list_of_books=Get_best_selling_books_for_single_DateAndType(query_date=date,query_bk_type=query_bk_type)
        small_list=Limit_list_attributes(large_list_of_books)
        list_of_books.append(Add_meta_details(small_list,query_date=date,query_bk_type=query_bk_type))
        query_date_start+= delta
        time.sleep(6)
        
    return list_of_books
        

def Get_best_selling_books_for_single_DateAndType(query_date,query_bk_type):
    # for a single date and type, function returns the list of results from the nytimes website to get best sellers for that week/type
    
    root_url="https://api.nytimes.com/svc/books/v3/lists"
    auth_key=Auth_key()
    print(f"{root_url}/{query_date}/{query_bk_type}.json?api-key={auth_key}")
    raw_data_file=pd.read_json(f"{root_url}/{query_date}/{query_bk_type}.json?api-key={auth_key}")
    return raw_data_file.to_dict('records')[1]['results']

def Auth_key():
    #assigns the authorization key
    auth_key="QslaLf6TwiaqpJUKKi1GVUBDdl5MrIo2"
    return auth_key

def Limit_list_attributes(large_list_of_books):
     #transform a large list to a limited set of attributes 
    small_list_of_books=[]
    for large_book in large_list_of_books:
        small_list_of_books.append(Get_limited_attribute(large_book))
    return small_list_of_books

def Get_limited_attribute(book):
    #given a book with a large set of dictionaries, get a book with a small set of attributes
    limited_attribute_set=Assign_limit_attributes()
    limited_listed_book={k:v for k, v in book.items() if k in limited_attribute_set}
    return limited_listed_book



def Add_meta_details(small_list,query_date,query_bk_type):
    #for a given list, append query details of type and date
    df_listed_books=pd.DataFrame(small_list)
    df_listed_books['date']=query_date
    df_listed_books['book_type']=query_bk_type
    return df_listed_books


def Assign_limit_attributes():
    #assign a limited set of attributes 
     limited_attribute_set=['title','weeks_on_list','primary_isbn13','publisher','author','rank','book_image_height','book_image_width','price','isbns','buy_links','book_image','amazon_product_url']
        return limited_attribute_set

        

    

                 