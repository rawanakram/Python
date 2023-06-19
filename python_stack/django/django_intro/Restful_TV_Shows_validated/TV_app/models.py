from django.db import models


# Create your models here.
class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors["title"] = "A show's title should be at least 2 characters"
        if len(postData['desc']) < 10:
            errors["desc"] = "A show's description should be at least 10 characters"
        if len(postData['network']) < 3:
            errors["network"] = "A show's network should be at least 3 characters"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=45)
    desc = models.TextField(default="cool film")
    release_date = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ShowManager()
   



