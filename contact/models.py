from django.db import models


# Create your models here.
class Contact(models.Model):
    class Meta:
        """ set display name in admin page """
        verbose_name_plural = 'Contact messages'

    """ schema for contact model  """
    name = models.CharField(max_length=75, null=False, blank=False)
    email = models.EmailField(max_length=256, null=False, blank=False)
    subject = models.CharField(max_length=256, null=True, blank=True)
    message = models.TextField(null=False, blank=False)

    def __str__(self):
        return f'Message from {self.email}'
