
from .models import Comment
from django import forms

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = '__all__'

        widgets = {
            'publish_date' : forms.SelectDateWidget(attrs={'class':'form-control'})
        }