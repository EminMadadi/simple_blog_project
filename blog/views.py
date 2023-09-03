from django.shortcuts import render

from .models import Post


def post_list_view(request):
    posts_list = Post.objects.filter(status=Post.STATUS_CHOICES[1][0])
    return render(request, 'blog/posts_list.html', {'posts_list': posts_list})


def post_detail_view(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
