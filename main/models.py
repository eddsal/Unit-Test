from django.db import models
from datetime import datetime

# Create your models here.


class UserAccount(models.Model):
    email = models.EmailField("Email address", blank=True, null=True, default=None, unique=True)
    first_name = models.CharField(max_length=100, blank=True, null=True, default=None, help_text="UserAccount first name")
    last_name = models.CharField(max_length=100, blank=True, null=True, default=None, help_text="UserAccount last name")
    password = models.CharField(max_length=40,  blank=True, default="")
    age = models.IntegerField('age')
    listt = models.ForeignKey('List', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):

        super(UserAccount, self).save()


class List(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True, default=None)


class Items(models.Model):
    can_create = False
    name = models.CharField(max_length=100, blank=True, null=True, default=None, unique=True)
    content = models.TextField(max_length=1000)
    created = models.DateTimeField(default=datetime.now(), auto_now=False)
    list_to_do = models.ForeignKey(List, on_delete=models.CASCADE)

    # def save(self, *args, **kwargs):
    #     if self.created > datetime.timedelta(minutes=30):
    #         can_create = True
    #     if self.name:
    #         self.name = self.name.title()
    #     return super(List, self).save(*args, **kwargs)
