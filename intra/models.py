import hashlib
import pathlib
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.html import mark_safe
from django.urls import reverse

class User(AbstractUser):
    ''' User extends the default django user with several 
    attributes that are needed in context of an intranet-application'''

    def user_image_path(self, filename):
        ''' Returns the a unique image name in form of a hash '''
        extension   = pathlib.Path(filename).suffix
        hashed_name = hashlib.sha256(\
            filename.lower().encode('utf-8')).hexdigest();
        return 'intra/static/intra/userimages/{0}{1}'\
            .format(hashed_name, extension)

    def image_tag(self):
        ''' Returns an image tag to show in the admin backend '''
        return mark_safe('<img src="/%s" width="150" height="150" />' \
            % (self.image))

    image_tag.short_description = 'Image preview'
    image_tag.allow_tags = True

    department  = models.CharField(max_length=100, null=True)
    jobtitle    = models.CharField(max_length=100, null=True)
    telefon     = models.CharField(max_length=40, null=True)
    age         = models.IntegerField(null=True)
    image       = models.ImageField(upload_to=user_image_path, \
        default='intra/static/intra/userimages/default.png')

class Announcement(models.Model):
    ''' An announcement holds information to be shown 
    to the members of the intranet'''
    
    title       = models.CharField(max_length=100)
    description = models.TextField()
    author      = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    created_at  = models.DateTimeField(auto_now_add=True)
    pinned      = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('announcement-detail', kwargs={'pk': self.pk})

    def __str__(self) -> str:
        return self.title