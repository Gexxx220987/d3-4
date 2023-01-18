from .models import Post

from django.shortcuts import render, get_object_or_404

from django.conf import settings




def index(request):
    posts = (Post
             .objects
             .prefetch_related()
             [:settings.COUNT_POSTS])
    return render(request, 'posts/index.html', {'posts': posts})



def news_list(request):
    posts = (Post
             .objects
             .prefetch_related()
    [:settings.COUNT_POSTS])
    return render(request, 'posts/news_list.html', {'posts': posts})


def news_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'posts/news_detail.html', {'post': post})

