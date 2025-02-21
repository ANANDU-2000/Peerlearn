from django import forms
from .models import Learner, Mentor

class LearnerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Learner
        fields = '__all__'  # Include all fields from the Learner model

class MentorRegistrationForm(forms.ModelForm):
    class Meta:
        model = Mentor
        fields = '__all__'  # Include all fields from the Mentor model