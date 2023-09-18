from Account.models import Account
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save, post_delete
from crawler import get_values
import threading

def set_values_inside_model(account_object: Account):
    data = get_values(account_object.account_url)
    print(data)
    account_object.profile_image_url = data["image_url"]
    account_object.name = data["heading"]
    account_object.followers = data["followers"]
    account_object.bio = data["description"]
    account_object.save()

@receiver(post_save,sender=Account)
def launching_crawler(sender,instance:Account,created,**kwargs):
    if created:
        threading.Thread(target=set_values_inside_model,args=(instance,)).start()