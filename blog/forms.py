from django import forms 
from .models import Comment


class CommentForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': "form-control",
        'id': 'message',
        'placeholder': "Message",
        'rows': '10',
        'cols': '30'
    }), label=False)

    class Meta:
        model = Comment
        fields = ('content', )