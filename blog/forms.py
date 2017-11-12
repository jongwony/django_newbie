from django import forms

from .models import Post, Comment, Upload


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text', )


class FileForm(forms.ModelForm):
    class Meta:
        model = Upload
        fields = ('file', )
