from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.shortcuts import reverse


# import requests


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    image_url = models.URLField(max_length=200, default="https://firebasestorage.googleapis.com/v0/b/django-blog-c1e8b.appspot.com/o/jokllpaper-hd-1080p.jpg?alt=media&token=366158cf-76a0-41fe-9d9b-e82c16fb3a46")

    def __str__(self):
        return f'{self.user.username} Profile'

    # def get_absolute_url(self):
    #     return reverse('profile')

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)  # opens the image of current instance

        if img.height > 300 and img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
