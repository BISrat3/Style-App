from django.db import models

# Create your models here.
class ShirtHome(models.Model):
    # template_name = "home.html"
    name = models.CharField(max_length =200)
    img = models.CharField(max_length=250)
    price =models.IntegerField()
    def __str__(self):
        # return HttpResponse("Product Home")
        return self.name
    class Meta:
        ordering =['name']