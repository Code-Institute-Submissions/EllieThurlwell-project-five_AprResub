from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):
    """ form of product info for admin access """

    class Meta:
        """ define form fields """

        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        """ set category friendly name as field name """
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        # set attributes to all field elements
