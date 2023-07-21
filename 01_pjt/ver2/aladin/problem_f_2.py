import json


def sorted_cs_books_by_price(books, categories):
    cs_books_list = []
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
        
        return
    
    
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
    books_json = open('data/books.json', encoding='utf-8')
    books = json.load(books_json)

    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)

    print(sorted_cs_books_by_price(books, categories_list))
