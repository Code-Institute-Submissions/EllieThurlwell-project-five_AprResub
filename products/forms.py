from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category
from locations.models import Location


class ProductForm(forms.ModelForm):
    """ form to add product info for admin access """

    class Meta:
        """ define form fields """

        model = Product
        fields = '__all__'

    image = forms.ImageField(
        label='Image',
        required=False,
        widget=CustomClearableFileInput
    )

    def __init__(self, *args, **kwargs):
        """ set category friendly name as field name """
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        # set attributes to all field elements


# class LocationForm(forms.ModelForm):
#     """ form to add location info for admin access """

#     class Meta:
#         """ define form fields """
#         model = Location
#         fields = '__all__'

#     # image = forms.ImageField(
#     #     label='Image',
#     #     required=False,
#     #     widget=CustomClearableFileInput
#     # )
