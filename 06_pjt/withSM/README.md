# 많이 하는 실수

* form 태그에서 method 적지 않는 것
* form태그에서 action= 다음에 url주소만 적고 url자체태그?을 적지 않는 것
* save(commit=False) 하고 다시 save() 하지 않는 것
* models.py 변경하고 migrations과 migrate하지 않는 것
* movie.pk와 movie_pk 쓸 곳 구분하는 것





# 어려웠던 부분

* url 이름 네이밍하는것
  * variable routing 순서(문자가 뒤에오는게 편하다)
  * 복수형.단수형



# 배운 점 

* is_valid가 False일때 return값 

```python
def comments_create(request,movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.movie = movie
        comment_form.save()
        return redirect('movies:detail',movie_pk)
    context = {
        'movie':movie,
       'comment_form':comment_form, 
    }
    return render(request,'movies/detail.html',context)
```





# 느낀 점

### 첫 팀프로젝트

관통프로젝트는 계속 혼자해오다가, 처음으로 2명이 한 조가 되어서 작업을 해보았다. 혼자 할 때보다는 생각해야 하는 것들이 많아졌다. 예를 들자면 다음과 같은 것들이다.

1. 통일성 -  혼자 할 때는 변수이름, 함수이름 등을 네이밍 할 때,편한대로 작성하면 되었지만, 이제는 다른 사람과 같이 해야하니 서로 소통하며 작업해야 했다. 

2. 시간관리 - 처음에는 드라이버와 네비게이터의  역할을 바꿔가며 작업을 했다. 기존에 작성해둔 코드를 보지 않고 생각해내며 서로 얘기를 하며 코딩을 하다보니 시간이 훌쩍 지나버렸다. 결국 실습시간 내에 끝내지 못하여서 일과시간 후에 각자 집에서 완성할 수 있었다. 다음에는 기존에 작성해둔 코드를 네비게이터가 참고하면서 작업하면 좋을 듯하다. 

3. 코딩순서 - 서로 구현할 부분을 나눠서 작업을 할 때는 한 사람이 맡은 html이 작성되어야 다른 사람이 이어서 작업을 할 수 있는 등 소통이 필요한 부분이있었다. 각자 만든 코드가 병합이 되어서 잘 작동 될지에 대한 두려움이 있었다.

4. 깃 사용법- 혼자 할 땐 git clon,add,commit,push만 알고 있으면 되었지만, 이제는 branch, merge등 배워야 할 것이 많다.

   

혼자*2로 두명이서 같이 하니 더 재미있었고, 앞으로 더 큰 프로젝트를  할 수 있겠다는 생각도 들었다. 혼자 코딩하는 것이 아직은 더 익숙하지만, 앞서 서술한 어려움들을 해결해나가며 함께 코딩하는 법을 잘 배워가야겠다.



# 보충해야 할 점

### 추가적으로 작업해야 하는 것

* FOLLOW버튼 만들 화면

### 추가적으로 작업하면 좋은 것

* 보충과제 1,2,3