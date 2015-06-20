from django.db import models
from django.template.defaultfilters import slugify
from django.db.models import permalink

class Photo(models.Model):
    widthfield=500	
    title=models.CharField(max_length=128)
    pic=models.ImageField(upload_to='images/',height_field=None,width_field='widthfield',max_length=100)
    slug=models.SlugField(unique=True)	
     
    def save(self,*args,**kwargs):
	    self.slug=slugify(self.title)
	    super(Photo,self).save(*args,**kwargs) 	

    def __unicode__(self):
        return self.title
    
    @permalink
    def get_absolute_url(self):
	return ('photo',None,{'slug':self.slug})

# Create your models here.
