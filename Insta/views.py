from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from django.views.generic import DetailView
from Insta.models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class HelloWorld(TemplateView):
    template_name = 'test.html'

class PostsListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "index.html"


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = "post_detail.html"
