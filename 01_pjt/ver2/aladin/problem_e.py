import json


def new_books(books):
    new_books_list = []  # set사용가능할듯?
    for book in books: 
        id = book['id']
        book = open(f'data/books/{id}.json', encoding='utf-8')
        book_detail = json.load(book)
        published_Year = book_detail["pubDate"][:4]
        book_name = book_detail["title"]
        if published_Year=='2023':
            new_books_list.append(book_name)
    return new_books_list




# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books_list = json.load(books_json)
    
    print(new_books(books_list))
