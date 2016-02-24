from django.db import models

# Create your models here.
# ref fields .. https://docs.djangoproject.com/en/1.8/ref/models/fields/
# python manage.py  makemigrations
# python manage.py migrate


class SignUP(models.Model):

    email = models.EmailField()
    fullname = models.CharField(max_length=120,blank=True,null=True)
    zipcode =  models.DecimalField(max_digits=10,decimal_places=8)
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now_add=False,auto_now=True)

    def __unicode__(self):

        return self.email


class DnsName(models.Model):

    address = models.CharField(max_length=50)
    host = models.CharField(max_length=30)

    def __unicode__(self):
        return self.host(self)
