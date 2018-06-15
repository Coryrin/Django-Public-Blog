from django.shortcuts import render, redirect, get_object_or_404
# Class Based Views
from django.views import generic
from django.views.generic.edit import UpdateView, DeleteView, FormMixin, FormView
from django.urls import reverse_lazy, reverse
# get login required/mixins
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.http import Http404, HttpResponseRedirect

from .models import Post
from . import forms
from datetime import datetime


# list view of all posts
class PostList(generic.ListView):
    model = Post
    template_name = 'posts/post_list.html'

# detail view.
def post_detail(request, slug):
    post = Post.objects.get(slug=slug)

    if request.method == 'POST':
        form = forms.CommentForm(request.POST)
        comment = form.save(commit=False)
        comment.post = post
        comment.author = request.user
        comment.save()
        form = forms.CommentForm()
    else:
        form = forms.CommentForm

    context = {
        'title': post.title,
        'form': form,
        'post': post
    }

    return render(request, 'posts/post_detail.html', context)
    
# create post 
class CreatePostView(LoginRequiredMixin, generic.CreateView):
    model = Post
    form_class = forms.CreatePost

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = self.request.user
            post.save()

        # return a HttpResponseRedirect to the newly made post
        # CreateView was throwing a tantrum without it.
        return HttpResponseRedirect(reverse_lazy('posts:detail', kwargs={'slug': post.slug}))


class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ('message',)
    template_name = 'posts/post_update.html'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()

        # check if author of a post is the same as the current user
        # if not, raise a 404 error
        if obj.author != self.request.user:
            raise Http404("You are not allowed to edit this post")

        return super(PostUpdate, self).dispatch(request, *args, **kwargs)
        
# Delete View
class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()

        if obj.author != self.request.user:
            raise Http404("You are not allowed to delete this post!")

        return super(PostDelete, self).dispatch(request, *args, **kwargs)