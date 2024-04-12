from django.shortcuts import render
from django.views import generic
from .models import Post


# Create your views here.


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1) # 1 is published, this will stop drafts from being shown
    template_name = "blog/index.html"
    paginate_by = 6