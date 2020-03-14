from django import forms
from .models import Post, Comment

class PostForms(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'contents')

class CommentForms(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)