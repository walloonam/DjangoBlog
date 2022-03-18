from django.views.generic import ListView, DetailView


# Create your views here.
from .models import Post



class PostList(ListView):
    model = Post
    ordering = '-pk'

class PostDetail(DetailView):
    model = Post