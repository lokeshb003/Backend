from django.contrib.auth.models import Group
from django.db import models

new_group, created = Group.objects.get_or_create(name='user_admin')
new_group, created = Group.objects.get_or_create(name='per_user')
new_group, created = Group.objects.get_or_create(name='plumber')
new_group, created = Group.objects.get_or_create(name='prime')


class AdminProduct(models.Model):
    pro_name = models.CharField(max_length=32)
    pro_description = models.TextField()
    pro_image = models.TextField(default="")
    pro_code = models.CharField(max_length=32, primary_key=True)
    pro_range = models.CharField(max_length=32)
    pro_features = models.TextField(default="")
    pro_price = models.IntegerField()
    pro_price_per_user = models.IntegerField()
    pro_price_plumber = models.IntegerField()
    pro_price_prime = models.IntegerField()