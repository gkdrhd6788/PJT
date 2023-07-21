import json


def best_new_books(books):
    best_new_books_list = []
    for book in books: 
        id = book['id']
        book = open(f'data/books/{id}.json', encoding='utf-8')
        book_detail = json.load(book)
        published_Year = book_detail["pubDate"][:4]
        book_name = book_detail["title"]
        review_rate = book_detail["customerReviewRank"]
        if published_Year=='2023':
            best_new_books_list.append((review_rate,book_name,))  
        best_new_books_list_2 = sorted(best_new_books_list,reverse=True)
        #best_new_book = best_new_books_list_2[0] #왜 안되는데..return에서 하면 되자나
    #return best_new_books_list_2[0][1]
    return best_new_books_list_2[0][1]



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books_list = json.load(books_json)
    
    print(best_new_books(books_list))
