from Account.models import Account
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save, post_delete
from crawler import get_values

@receiver(post_save,sender=Account)
def launching_crawler(sender,instance:Account,created,**kwargs):
    if created:
        data = get_values(instance.account_url)
        print(data)
        instance.profile_image_url = data["image_url"]
        instance.name = data["heading"]
        instance.followers = data["followers"]
        instance.bio = data["description"]