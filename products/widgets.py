from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInput(ClearableFileInput):
    """ custom image input widget for admin controls """
    clear_checkbox_label = _('Remove')
    initial_text = _('Current image')
    input_text = _('')
    template_name = 'products/custom_widget_templates/custom_clearbale_file_input.html'
