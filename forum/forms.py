from django import forms
from .models import Answer

class AnswerForm(forms.ModelForm):
    class meta:
        model = Answer
        fields = ['answer']