from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
# Create your models here.
class UserContact(models.Model):
    user = models.OneToOneField(User)
    user_contact = models.CharField(max_length=255)

    def get_absolute_url(self):
        return reverse("contacts_detail",kwargs={'pk':self.pk})


    def __str__(self):
        return self.user.username
