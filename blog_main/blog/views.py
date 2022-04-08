from django.views.generic import ListView, DetailView
from django.shortcuts import render

# Create your views here.
from .models import Post, Category, Tag


class PostList(ListView):
    model = Post
    ordering = '-pk'

    def get_context_data(self, object_list=None, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context

class PostDetail(DetailView):
    model = Post

    def get_context_data(self, object_list=None, **kwargs):
        context = super(PostDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context


def categories_page(request, slug):
    if slug == 'no_category':
        category = '미분류'
        post_list = Post.objects.filter(category=None)
    else :
        category = Category.objects.get(slug=slug)
        post_list = Post.objects.filter(category=category)


    context = {
        'categories' : Category.objects.all(),
        'no_category_post_count' : Post.objects.filter(category=None).count(),
        'category' : category,
        'post_list' : post_list
    }

    return render(request, 'blog/post_list.html', context)


def show_tag_posts(request, slug):
    tag = Tag.objects.get(slug=slug)
    post_list = tag.post_set.all()

    context = {
        'categories' : Category.objects.all(),
        'no_category_post_count' : Post.objects.filter(category=None).count(),
        'tag': tag,
        'post_list' : post_list
    }
    return render(request, 'blog/post_list.html', context)