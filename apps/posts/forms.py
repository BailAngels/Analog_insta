from django import forms

from apps.posts.models import Post, Images


class ImagesForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = ('image', )
        widgets = {'image': forms.ClearableFileInput(attrs={
            'class': 'form-control-file'
        })}


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('description', 'location', 'tags')
