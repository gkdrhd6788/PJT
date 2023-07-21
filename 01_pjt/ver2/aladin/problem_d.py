import json


def best_book(books_list):
    best_books_list = []  # set사용가능할듯?
    for book in books_list: 
        id = book['id']
        book = open(f'data/books/{id}.json', encoding='utf-8')
        book_detail = json.load(book)
        book_set =( book_detail["title"],book_detail["customerReviewRank"] )
        '''#딕셔너리 사용 시도
        book_set ={
        'book_name' : book_detail["title"],
        'review_rate' : book_detail["customerReviewRank"]
        }'''
        best_books_list.append(book_set)
        best_books_list.sort(key=lambda x:x[1],reverse=True)  #tuple을 사용해야 하는가?dict은 평점이 중복되면 어떻게 되지??
        #sorted(best_books_list,key=lambda x:x[1])
        best_book_set = best_books_list[0]
        best_book_name = best_book_set[0]
    return best_book_name
    


               
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books_list = json.load(books_json)
    
    print(best_book(books_list))


    # open 및 json 모듈 사용예시



