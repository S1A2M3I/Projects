from django import forms

class ReviewForm(forms.Form):
    text = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'Enter your review'}),
        label='Customer Review'
    )
