from django import forms
from marksapp.models import marks

class marksform(forms.ModelForm):
    class Meta:
        model=marks
        fields='__all__'
