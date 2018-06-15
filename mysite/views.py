from django.views.generic import TemplateView, ListView
from django.shortcuts import render

from posts.models import Post

def home_view(request):
    posts = Post.objects.all()

    # check if there are no posts. if there are none, set latest to an empty string.
    if not posts:
        latest = ''
    else:
        latest = Post.objects.latest('created_at')

    context = {
        'title':'Public Django Blog',
        'posts': posts,
        'latest': latest
    }

    return render(request, 'index.html', context)

def sidebar(request):
    posts = Post.objects.all()[:5]

    context = {
        'posts': posts
    }

    return render(request, '_sidebar.html', context)

class LoggedOut(TemplateView):
    template_name = 'thanks.html'
    