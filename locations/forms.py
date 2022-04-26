from django import forms
from products.widgets import CustomClearableFileInput
from .models import Location


class LocationForm(forms.ModelForm):
    """ form to add location info for admin access """

    class Meta:
        """ define form fields """
        model = Location
        fields = '__all__'

    image = forms.ImageField(
        label='Image',
        required=False,
        widget=CustomClearableFileInput
    )
