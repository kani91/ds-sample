import requests 
from datetime import date
import sqlite3
import pandas as pd
#from Functions import get_best_selling_books_multiple
#

conn =sqlite3.connect('Nyt.db')
query="""SELECT distinct primary_isbn13 FROM NYT_BS_2009to2019"""
cursor=conn.cursor()
listofisbns=list(cursor.execute(query).fetchall())
listofcleanisbn=[listofisbn[0] for listofisbn in listofisbns]



def get_googledata(isbn):
    auth_key="AIzaSyAtorQoSBP-6j7LawCVrcCjEyYMe27QJm8"
    #print(requests.get(f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}&key:{auth_key}").text)
    
    try:
        raw_data_file=pd.read_json(f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}&key:{auth_key}")
        list_of_attributes=['title','subtitle','authors','publishedDate','publisher','description','pageCount','printType','categories', 'averageRating']
        google_info={k:v for k,v in raw_data_file['items'][0]['volumeInfo'].items() if k in list_of_attributes}
        google_info['isbn'] = isbn
        google_info['isfound']=1
        
        print(f"added this - {google_info['isbn']}")
        return google_info
    
    except:
#         google_info['isbn'] = isbn
#         google_info['isfound']=0
        google_info={}
        google_info['isbn'] = isbn
        google_info['isfound']=0
        print(f"did not add this - {google_info['isbn']}")
        return None

    
def get_googledata_for_all_isbns(listofcleanisbn):
    
    google_isbn_data=[]
    for i in range(len(listofcleanisbn)):
        google_isbn_data.append(get_googledata(str(listofcleanisbn[i])))
 
    return google_isbn_data




