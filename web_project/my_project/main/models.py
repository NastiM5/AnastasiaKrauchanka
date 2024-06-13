from django.db import models


# Create your models here.

class Author(models.Model):

    name = models.CharField(blank=False, max_length=100)
    email = models.EmailField(primary_key=True)



class Review(models.Model):
    
    title = models.CharField(max_length=100)
    comment = models.TextField(max_length=100)
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    image = models.ImageField(upload_to='uploads')
    date = models.DateTimeField(auto_now_add=True)
      
    
    def __str__(self):
        return self.title



















class Price(models.Model):

    Service = [("Training", "Training"), ("Walking", "Walking"), ("Hotel", "Hotel")]
    Type = [("Individual", "Individual"), ("Group", "Group")]

    service = models.CharField(choices=Service, max_length=50)
    type = models.CharField(choices=Type, max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Bot (models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    