from django import forms
from .models import Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'description', 'feedback']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': "Leave blank to submit anonymous"}),
            'description': forms.TextInput(attrs={'placeholder': "Under 50 characters"}),
            'feedback': forms.TextInput(attrs={'placeholder': "Kindly elaborate on your feedback"}),
        }
        labels = {
        "name": "Name:",
        'description': "Brief description:",
        'feedback': "Feedback:",
    }