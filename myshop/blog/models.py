from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Post(models.Model):
    autor = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = RichTextUploadingField(blank=True, default='')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    class Meta:
        verbose_name = 'Новости'           


    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def __str__(self):
        return self.title



class About_us(models.Model):
    autor = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = RichTextUploadingField(blank=True, default='')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    class Meta:
        verbose_name = 'О нас'           


    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def __str__(self):
        return self.title



class Glavnaya(models.Model):
    autor = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = RichTextUploadingField(blank=True, default='')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    class Meta:
        verbose_name = 'Главная'           


    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def __str__(self):
        return self.title




class Contacts(models.Model):
    autor = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = RichTextUploadingField(blank=True, default='')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    class Meta:
        verbose_name = 'Контакты'           


    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def __str__(self):
        return self.title
