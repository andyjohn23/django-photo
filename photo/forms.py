from django import forms


class ImageSearchForm(forms.Form):
    q = forms.CharField()
    
