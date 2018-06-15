from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User
import misaka

# post model
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    title = models.CharField(max_length=255)
    message = models.TextField()
    message_html = models.TextField(editable=False, default='', blank=True)
    image = models.ImageField(default='road.jpeg', blank=True, upload_to='media/')
    slug = models.SlugField(allow_unicode=True, unique=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def snippet(self):
        self.message_html = misaka.html(self.message)
        return self.message[:50]
        
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        self.message_html = misaka.html(self.message)
        super().save(*args,**kwargs)
    
    def get_absolute_url(self):
        return reverse('posts:detail', kwargs = {'slug': self.slug})

    class Meta:
        ordering = ['-created_at']


# comment on any posts, foreign key needed blahblahblah
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default='')    
    message = models.TextField(blank=True, default='')
    message_html = models.TextField(editable=False, default='', blank=True)    
    created_at = models.DateTimeField(auto_now=True)

    # add in author later

    def __str__(self):
        return self.message

    def get_absolute_url(self):
        return reverse('posts:detail', kwargs = {'slug': self.post.slug})

    def save(self, *args, **kwargs):
        self.message_html = misaka.html(self.message)
        super().save(*args,**kwargs)

