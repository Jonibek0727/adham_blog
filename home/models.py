from django.db import models
from django.urls import reverse


# Create your models here.
class HomePage(models.Model):
    aboutme = models.CharField(max_length=300)
    aboutme2 = models.CharField(max_length=300)
    PYTHON1 = models.CharField(max_length=20)
    PYTHON = models.CharField(max_length=300)
    BRAND_IDENTITY1 = models.CharField(max_length=20)
    BRAND_IDENTITY = models.CharField(max_length=300)
    Admin1 = models.CharField(max_length=20)
    Admin22 = models.CharField(max_length=300)
    TELEGRAM_BOt1 = models.CharField(max_length=20)
    TELEGRAM_BOt = models.CharField(max_length=300)
    DATABASE1 = models.CharField(max_length=20)
    DATABASE = models.CharField(max_length=300)
    Github1 = models.CharField(max_length=20)
    Github = models.CharField(max_length=300)
    GETINTOUCH = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    number = models.CharField(max_length=50)
    gmail = models.CharField(max_length=50)
    copyright = models.CharField(max_length=50)
    design = models.CharField(max_length=50)
    adham = models.CharField(max_length=50)
    source = models.CharField(max_length=50)
    django = models.CharField(max_length=50)
    djangorestapi = models.CharField(max_length=50)
    documentation = models.CharField(max_length=50)
    pythoncoding = models.CharField(max_length=50)
    telegram = models.CharField(max_length=50)
    telegramchanel = models.CharField(max_length=50)
    telegrambot = models.CharField(max_length=50)
    fullbot = models.CharField(max_length=50)


class NEWS(models.Model):
    photo = models.ImageField(upload_to='img/')
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=True)
    description = models.TextField()

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    user = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(NEWS, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return f'{self.user}-{self.post} - {self.date}'

    def get_absolute_url(self):
        return reverse('blog-single', args=[str(self.pk)])




