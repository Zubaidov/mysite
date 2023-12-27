from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.http import Http404

from django.views.generic import ListView
from .forms import CommentForm
from django.views.decorators.http import require_POST

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
    
    comments = post.comments.filter(active=True)
    form = CommentForm()

    context = {
        'post':post,
        'comments':comments,
        'form':form,
    }
    return render(request, 'blog/post/detail.html', context)


@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(Post,
                             id=post_id,
                             status = Post.Status.PUBLISHED)
    comment = None

    form = CommentForm(request.POST)
    
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()

    context = {
        'post':post,
        'form':form,
        'comment':comment
    }
    
    return render(request, 'blog/post/comment.html', context)
