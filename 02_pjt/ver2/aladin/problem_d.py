import requests
from pprint import pprint
import json  #import 안해도 될듯? 

 
ttbkey = 'ttbgkdrhd67881158001'
#query = title
#query_type = 'Title'
max_results = 20
start = 1
search_target = 'Book'
output = 'js'
version = 20131101


'''
def author_other_works(title):  
    query = title   #여기서 선언해줘야겠지?밑도?
    query_type = 'Title'
    URL = f"http://www.aladin.co.kr/ttb/api/ItemSearch.aspx?ttbkey={ttbkey}&Query={query}&QueryType={query_type}&MaxResults={max_results}&start={start}&SearchTarget={search_target}&output={output}&Version={version}"
    response = requests.get(URL)
    response_json = response.json()
    result = response_json.get('item')

    if result :
        first_author=result[0].get('author').split(',')[0]
        query = first_author
        query_type = 'Author'
        response = requests.get(URL)
        response_json = response.json()
        result = response_json.get('item')
        
        five_book_list = []
        isbn_list=[]
        i=0
        while len(five_book_list) < 5 :
            if result[i].get('isbn') not in isbn_list:
                five_book_list.append(result[i].get('title'))
                isbn_list.append(result[i].get('isbn'))
                                 
            i += 1
            
        return five_book_list #결과값이 같은게 3개. ISBN이 다른 3개인가?

    else:
        return None  #이렇게 안하고 None받는 

'''

def author_other_works(title):     
    query = title   #여기서 선언해줘야겠지?밑도?
    query_type = 'Title'
    URL = f"http://www.aladin.co.kr/ttb/api/ItemSearch.aspx?ttbkey={ttbkey}&Query={query}&QueryType={query_type}&MaxResults={max_results}&start={start}&SearchTarget={search_target}&output={output}&Version={version}"
    response = requests.get(URL)
    response_json = response.json()
    result = response_json.get('item')

    if not result :     #강사님이 말씀해주신 꿀팁(코드가 depth가 깊어지지 않게)
        return None
    
    first_author=result[0].get('author').split(',')[0]
    query = first_author
    query_type = 'Author'
    response = requests.get(URL)
    response_json = response.json()
    result = response_json.get('item')
    
    five_book_list = []
    isbn_list=[]
    i=0
    while len(five_book_list) < 5 :
        if result[i].get('isbn') not in isbn_list:
            five_book_list.append(result[i].get('title'))
            isbn_list.append(result[i].get('isbn'))
                             
        i += 1
            
    return five_book_list #결과값이 같은게 3개. ISBN이 다른 3개인가?



    
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':

    pprint(author_other_works('베니스의 상인'))

    pprint(author_other_works('개미'))

    pprint(author_other_works('*'))

