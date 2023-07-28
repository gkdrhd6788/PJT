import requests
from pprint import pprint
import json  #import 안해도 될듯? 

 
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

#pprint(result)

def bestseller_book():
    sales_point_dict={}
    for i in range(len(result)): #for문 안쓰고 할 수 없나?
        sales_point_dict[i]=result[i].get('salesPoint')
    sorted_list = sorted(sales_point_dict.items(), key = lambda x:x[1],reverse=True) #dict sort를 배웠던가? #list가 됨, 튜플인가 세트가 됨 
    book_list=[]
    for i in range(5):
        book_list.append(result[sorted_list[i][0]].get('title'))
    return book_list
    




# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':

    print(bestseller_book())

