import requests
from pprint import pprint
# 
OptResult='ebookList'
ttbkey = 'ttbgkdrhd67881158001'
max_results = 20
start = 1
search_target = 'Book'
output = 'js'
version = 20131101


def ebook_list(title):
    query = title   
    query_type = 'Title'
    URL = f"http://www.aladin.co.kr/ttb/api/ItemSearch.aspx?ttbkey={ttbkey}&OptResult={OptResult}&Query={query}&QueryType={query_type}&MaxResults={max_results}&start={start}&SearchTarget={search_target}&output={output}&Version={version}"
    response = requests.get(URL)
    response_json = response.json()
    result = response_json.get('item')
        
    if not result :     #강사님이 말씀해주신 꿀팁(코드가 depth가 깊어지지 않게)
        return None
    #pprint(result)  #result구조 파
    #book,ebook가격 할당
    book_price= result[0].get('priceSales')
    ebook_price=result[0].get('subInfo').get('ebookList')[0].get('priceSales')

    
    if ebook_price <= book_price*0.9:
        cheap_book_dict={
        'isbn' : result[0].get('subInfo').get('ebookList')[0].get('isbn'),
        'itemId' : result[0].get('subInfo').get('ebookList')[0].get('itemId'),
        'link' : result[0].get('subInfo').get('ebookList')[0].get('link'),
        'priceSales' : result[0].get('subInfo').get('ebookList')[0].get('priceSales')
        }
        
        
        
    return cheap_book_dict 



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':

    pprint(ebook_list('베니스의 상인'))
    pprint(ebook_list('총균쇠'))
    pprint(ebook_list('*'))
