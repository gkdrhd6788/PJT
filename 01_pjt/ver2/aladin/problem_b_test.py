import json
from pprint import pprint

def book_info(book, categories):
    '''
    book_dict = {                         #굳이 안써도 되는 듯?
        'author': book ['author'],
        'categoryId' : book ['categoryId'],
        'cover': book ['cover'],
        'description' : book ['description'],
        'id' : book['id'],
        'priceSales' : book ['priceSales'],
        'title' : book ['title']
    } 
    '''
    #print(book ['categoryId'][0])
    
    catename=[]
    for category in categories:
        if category["id"] == book ['categoryId'][0]:
            catename.append(category["name"])
            

        if category["id"] == book ['categoryId'][1]:
            catename.append(category["name"])

    
    new_book_dict = {
        'author': book ['author'],
        'categoryName' : catename,
        'cover': book ['cover'],
        'description' : book ['description'],
        'id' : book['id'],
        'priceSales' : book ['priceSales'],
        'title' : book ['title']
    } 
    return new_book_dict

if __name__ == '__main__':
    book_json = open('data/book.json', encoding='utf-8')
    book = json.load(book_json)

    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)

    pprint(book_info(book, categories_list))