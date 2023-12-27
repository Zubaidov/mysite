from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import Http404

def post_list(request):
    posts = Post.published.all()
    context = {
        'posts' : posts
    }
    return render(request, 'blog/post/list.html', context)


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,
                             slug=post,
                             publish__year = year,
                             publish__month = month,
                             publish__day = day,
                             status=Post.Status.PUBLISHED)
    context = {
        'post':post
    }
    return render(request, 'blog/post/detail.html', context)
