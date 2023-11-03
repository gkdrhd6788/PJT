# 개발 도구

*  VScode
* Django
* AJAX



#  배운 점

```javascript
{% if request.user in person.followers.all %}
  <input type="submit" value="Unfollow">
{% else %}
  <input type="submit" value="Follow">
      
//위 코드에서 if-else구문이 불필요한지 알고 input태그 한줄만 작성했었다. ajax로 비동기화기능으로 unfollow, follow 로 클릭시마다 바뀌었지만, 새로고침하면 그 이전 상태를 저장하지 않고 초기화되는 문제가 있었다. if-else 구문의 필요성을 알게 되었다. 
```



# 느낀 점

* 이전에 해왔던 것과 비슷한 작업이었지만, javascript를 쓰는 것이 새로웠다. 