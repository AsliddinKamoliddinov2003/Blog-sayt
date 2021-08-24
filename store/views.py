from django.views.generic import ListView, DeleteView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Post


class BlogListView(ListView):
    model = Post   
    template_name = "home.html"


class BlogDetailView(DeleteView):
    model = Post
    template_name = "post_detail.html"


class BlogCreateView(CreateView):
    model = Post
    template_name = "create_post.html"
    fields = ['title', 'author', 'description']


class BlogUpdateView(UpdateView):
    model = Post
    template_name = "update_post.html"
    fields = ['title', 'description']


class BlogDeleteView(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy('home')
    
