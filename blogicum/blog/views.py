from django.http import HttpResponseNotFound
from django.shortcuts import render


def post_detail(request, id):
    if not any(post['id'] == id for post in posts):
        return HttpResponseNotFound(f'Поста с id {id} не существует.')

    for p in posts:
        if p['id'] == id:
            required_post = p

    context = {
        'post': required_post
    }
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    context = {
        'category_slug': category_slug
    }
    return render(request, 'blog/category.html', context)
