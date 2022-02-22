import email
from django import forms

# https://docs.djangoproject.com/en/1.11/ref/forms/fields/#built-in-field-classes
class ContactForm(forms.Form):
    fullname    =   forms.CharField(
                        widget=forms.TextInput(
                            attrs={
                                "class": "form-control", 
                                "placeholder": "Your full name"}))
    email       =   forms.EmailField(
                        widget=forms.EmailInput(
                            attrs={
                                "class": "form-control", 
                                "placeholder": "Your Email"}))
    content     =   forms.CharField(
                        widget=forms.Textarea(
                            attrs={
                                "class": "form-control", 
                                "placeholder": "Your message"}))

    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("Email has to be gmail.com")
        return email