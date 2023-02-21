from django.db import models

# Create your models here.
class Trade(models.Model):
    trade_id = models.AutoField(primary_key=True)
    trade_name = models.CharField(max_length=100, null=True, blank=True)
    trade_description = models.TextField(max_length=5000,null=True, blank=True)
    trade_image = models.ImageField(upload_to="product/")

    def __str__(self):
        return f'{self.trade_name}'

class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    contact_name = models.CharField(max_length=100, null=True, blank=True)
    contact_surname = models.CharField(max_length=100, null=True, blank=True)
    contact_email = models.EmailField(max_length=100, null=True, blank=True)
    contact_textarea = models.TextField(max_length=5000,null=True, blank=True)
    contact_number = models.TextField(max_length=5000,null=True, blank=True)
    def __str__(self):
        return f'{self.contact_name}  {self.contact_surname}'