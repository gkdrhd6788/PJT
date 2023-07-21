import json
from pprint import pprint

def book_info(book, categories):
    book_dict = {
        'author': book ['author'],
        'categoryId' : book ['categoryId'],
        'cover': book ['cover'],
        'description' : book ['description'],
        'id' : book['id'],
        'priceSales' : book ['priceSales'],
        'title' : book ['title']
    } 
    catename=[]
    for category in categories:
        if category["id"] == book_dict['categoryId'][0]:
            catename.append(category["name"])

        if category["id"] == book_dict['categoryId'][1]:
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
        




# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    book_json = open('data/book.json', encoding='utf-8')
    book = json.load(book_json)

    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)

    pprint(book_info(book, categories_list))
