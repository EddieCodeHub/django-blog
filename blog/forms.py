from django import forms
from .models import Comment



class CommentForm(forms.ModelForm):
    """
    A form for users to comment on a post

    **Fields**
    - body: the comment body
    """
    class Meta:
        model = Comment
        fields = ('body',)