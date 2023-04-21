from django import forms
from .models import ReviewRating

class ReviewForm(forms.ModelForm):
    rating = forms.FloatField(label='Rating (1-5)', max_value=5, min_value=1)
    class Meta:
        model = ReviewRating
        fields = ['subject', 'review', 'rating']
        
    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        if rating < 0 or rating > 5:
            raise forms.ValidationError("Rating value must be between 0 and 5.")
        return rating