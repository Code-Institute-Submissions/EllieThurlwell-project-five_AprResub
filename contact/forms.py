from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """ contact form """

    class Meta:
        """ define form fields """

        model = Contact
        fields = ('name', 'email', 'subject', 'message',)

    def __init__(self, *args, **kwargs):
        """ add placeholders to form fields and autofocus fullname """

        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Full Name',
            'email': 'Email Address',
            'subject': 'Subject',
            'message': 'Message',
        }

        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
