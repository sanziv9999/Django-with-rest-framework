from django.db import models

class Tours(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/assets/', default='static/assets/default.jpg')  # Required with default
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    afterDiscount = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.DecimalField(max_digits=5,decimal_places=1)
    reviews = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title


class TourDetails(models.Model):
    title = models.OneToOneField(Tours, on_delete=models.CASCADE)
    mapURL= models.TextField()
    des = models.TextField()
    tourInfo = models.TextField()
    PlacesCovered = models.CharField(max_length=200)
    Duration= models.CharField(max_length=100)
    SrartPoint= models.CharField(max_length=100)
    EndPoint = models.CharField(max_length=100)
    highlights = models.TextField()
    itinerary = models.TextField()

    def __str__(self):
        return self.title.title


