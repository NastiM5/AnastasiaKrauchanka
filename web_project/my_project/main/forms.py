from django import forms
from .models import Review
from .models import Bot



class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'comment', 'rating', 'image']



class BotForm(forms.ModelForm):
    class Meta:
        model = Bot
        fields = ['name', 'phone']