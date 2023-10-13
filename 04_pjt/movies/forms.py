from django import forms 
from .models import Movie,Comment

class MovieForm(forms.ModelForm):
    score = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                'min':0,
                'max':5,
                'step':0.5,
            }
        )
    )
    genre = forms.ChoiceField(
        choices=[
            ('comedy','comedy'),
            ('fantasy','fantasy'),
            ('romance','romance'),
        ]
    )
    class Meta:
        model = Movie
        fields = '__all__'
        exclude = ('user',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)