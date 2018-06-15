from django import forms
from .models import Post, Comment

class CreatePost(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'message', 'image')

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        
        fields = ['message']

        message = forms.Textarea(attrs={'class':'my-comment-form'})