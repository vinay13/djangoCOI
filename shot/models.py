from django.db import models
from django.db.models import permalink
from django.template.defaultfilters import slugify

class Category(models.Model):
        name = models.CharField(max_length=128, unique=True)
        views = models.IntegerField(default=0)
        likes = models.IntegerField(default=0)
        slug = models.SlugField(unique=True)

        def save(self, *args, **kwargs):
                self.slug = slugify(self.name)
                super(Category, self).save(*args, **kwargs)

        def __unicode__(self):
                return self.name

class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    limit_body=models.TextField()
    body = models.TextField()
#   url = models.URLField()
    image=models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100)
    views = models.IntegerField(default=0)
    
       
  
    def __unicode__(self):      #For Python 2, use __str__ on Python 3
        return self.image.url

    @permalink
    def get_absolute_url(self):
        return ('page', None, { 'slug': self.slug })

# Create your models here.
