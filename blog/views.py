from django.shortcuts import render
from django.views import generic

from .models import Link, Post

# Create your views here.


class NavBarView(generic.DetailView):
    model = Link
    template_name = "blog/navbar.html"


class PostsView(generic.ListView):
    queryset = Post.objects.order_by('-created_on')
    template_name = "blog/layout.html"
