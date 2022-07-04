from django import forms
from posts.models import Post
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput, ImageField

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['name', 'image']

        widgets = {
            "name": TextInput(attrs={
                'placeholder': 'Name of meme'
            }),
        }