from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Field
from .models import Contact

class ContactForm(forms.ModelForm):
    """Formulaire de contact"""
    
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Votre nom complet'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'votre.email@example.com'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Sujet de votre message'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Votre message...',
                'rows': 6
            }),
        }
        labels = {
            'name': 'Nom complet',
            'email': 'Adresse email',
            'subject': 'Sujet',
            'message': 'Message',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-6 mb-3'),
                Column('email', css_class='form-group col-md-6 mb-3'),
                css_class='form-row'
            ),
            Field('subject', css_class='form-group mb-3'),
            Field('message', css_class='form-group mb-3'),
            Submit('submit', 'Envoyer le message', css_class='btn btn-primary btn-lg')
        )
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            # Validation supplémentaire de l'email si nécessaire
            pass
        return email
    
    def clean_message(self):
        message = self.cleaned_data.get('message')
        if message and len(message) < 10:
            raise forms.ValidationError('Le message doit contenir au moins 10 caractères.')
        return message