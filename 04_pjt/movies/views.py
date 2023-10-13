from django.shortcuts import render,redirect
from .models import Movie,Comment
from .forms import MovieForm,CommentForm
from django.contrib.auth import update_session_auth_hash
from django.views.decorators.http import require_http_methods,require_POST,require_safe
# Create your views here.
@require_safe
def index(request):
    movies = Movie.objects.all()
    context ={
        'movies':movies,
    }
    return render(request,'movies/index.html',context)

@require_http_methods(["GET", "POST"])
def create(request):
    if request.method=="POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.user=request.user
            form.save()
            return redirect('movies:index')   

    else:
        form = MovieForm()
    context = {
        'form':form,
    }
    return render(request,'movies/create.html',context)

@require_safe
def detail(request,pk):
    movie= Movie.objects.get(pk=pk)
    comment_form = CommentForm()
    comments = movie.comment_set.all() 
    context={
        'movie':movie,
        'comment_form':comment_form,
        'comments':comments,
    }
    return render(request,'movies/detail.html',context)    

@require_http_methods(["GET", "POST"])
# 본인이 작성한 것만 수정 가능하게 만들기!!
def update(request,pk):
    movie = Movie.objects.get(pk=pk)
    if request.user != movie.user: return redirect('movies:detail',movie.pk)
    if request.method == "POST":
        form = MovieForm(request.POST,instance = movie)
        if form.is_valid():
            form.save()
            return redirect('movies:detail',movie.pk)
    else:
        form=MovieForm(instance=movie)
    context = {
        'form':form,
        'movie':movie,
    }
    return render(request,'movies/update.html',context)

@require_POST
def delete(request,pk):
    movie= Movie.objects.get(pk=pk)
    if request.user != movie.user:return redirect('movies:detail',pk)
    movie.delete()
    return redirect('movies:index')

def comment_create(request,movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.user = request.user
        comment.movie = movie
        comment_form.save()
        return redirect('movies:detail',movie_pk)
    context = {
        'movie':movie,
        'comment_form':comment_form,
    }
    return render(request,'movies/detail.html',context)

def comment_delete(request,movie_pk,comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('movies:detail',movie_pk)