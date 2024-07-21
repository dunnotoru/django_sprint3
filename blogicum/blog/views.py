from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from django.utils import timezone


def index(request):
    post_list = Post.objects.all()\
        .select_related('category')\
        .select_related('author')\
        .filter(is_published=True,
                pub_date__lte=timezone.now(),
                category__is_published=True)\
        .order_by('id')[:5]

    context = {
        'post_list': post_list
    }

    return render(request, 'blog/index.html', context)


def category_posts(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    if not category.is_published:
        return HttpResponseNotFound()

    post_list = Post.objects.all()\
        .select_related('category')\
        .filter(category__slug=category_slug,
                is_published=True,
                pub_date__lte=timezone.now())\

    context = {
        'post_list': post_list
    }

    return render(request, 'blog/category.html', context)


def post_detail(request, id):
    post = get_object_or_404(Post, pk=id)

    if post.pub_date > timezone.now():
        return HttpResponseNotFound()
    if not post.is_published:
        return HttpResponseNotFound()
    if not post.category.is_published:
        return HttpResponseNotFound()

    context = {
        'post': post
    }
    return render(request, 'blog/detail.html', context)


