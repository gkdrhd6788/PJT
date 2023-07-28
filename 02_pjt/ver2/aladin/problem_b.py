import requests
from pprint import pprint
import json

ttbkey = 'ttbgkdrhd67881158001'
query = '파울로 코엘료'
query_type = 'Author'
max_results = 20
start = 1
search_target = 'Book'
output = 'js'
version = 20131101

URL = f"http://www.aladin.co.kr/ttb/api/ItemSearch.aspx?ttbkey={ttbkey}&Query={query}&QueryType={query_type}&MaxResults={max_results}&start={start}&SearchTarget={search_target}&output={output}&Version={version}"

#request 보내기
response = requests.get(URL)

#받은 response를 json 타입으로 바뀌주기
response_json = response.json()

result = response_json.get('item')


def best_review_books():
    #index_books_list=[]
    best_review_books_list=[]
    for index_book in range(len(result)):
        if int(result[index_book].get('customerReviewRank')) >=  9 :
            best_review_books_list.append(result[index_book])
            
    return best_review_books_list
        
        



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':

    pprint(best_review_books())
