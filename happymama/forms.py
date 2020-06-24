from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    fonetic = forms.CharField()
    email = forms.EmailField(required=True)
    phone = forms.CharField()
    message = forms.CharField(required=True)
