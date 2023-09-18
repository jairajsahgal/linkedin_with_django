from django.db import models
import uuid
# Create your models here.
class Account(models.Model):
    account = models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4())
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    platform = models.CharField(max_length=100)
    account_url = models.URLField(unique=True,null=True)
    name = models.CharField(max_length=200,unique=True,blank=True,null=True)
    followers = models.BigIntegerField(blank=True,null=True)
    profile_image_url = models.TextField(max_length=5000,blank=True,null=True)
    bio = models.TextField(max_length=5000,blank=True,null=True)

    class Meta:
        db_table = "social_account_info"