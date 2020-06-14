from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from Insta.models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from Insta.forms import CustomUserCreationForm
from django.urls import reverse_lazy
# Create your views here.

class HelloWorld(TemplateView):
    template_name = 'test.html'

class PostsListView(ListView):
    model = Post
    template_name = "index.html"


class PostsDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"


class PostsCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "posts_create.html"
    fields = '__all__'##autofield 不包含
    login_url = 'login'##LoginRequiredMixin 如果没login 跳转到那个页面
    
class PostsUpdateView(UpdateView):
    model = Post
    template_name = "post_update.html"
    fields = "__all__"

class PostsDeleteView(DeleteView):
    model = Post
    template_name ="post_delete.html"
    success_url =reverse_lazy("posts")

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name="signup.html"
    success_url=reverse_lazy("login")