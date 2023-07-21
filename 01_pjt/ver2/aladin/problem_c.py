import json
from pprint import pprint


def books_info(books, categories):
    books_list = []
    for book in books:
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
        books_list.append(new_book_dict)
    return books_list
        



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books = json.load(books_json)

    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)

    pprint(books_info(books, categories_list))