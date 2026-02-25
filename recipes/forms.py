from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['comment', 'cooked_status']
        widgets = {
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'What did you think?'}),
            'cooked_status': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }