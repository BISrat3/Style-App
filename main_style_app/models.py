from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ShirtHome(models.Model):
    # template_name = "home.html"
    name = models.CharField(max_length =200)
    img = models.CharField(max_length=250)
    price =models.IntegerField()

    user = models.ForeignKey(User, on_delete = models.CASCADE, default=1)
    def __str__(self):
        # return HttpResponse("Product Home")
        return self.name
    class Meta:
        ordering =['name']