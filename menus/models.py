from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=45)

    # Representação em string
    def __str__(self):
        return f"[Restaurant] name: {self.name}"

class MenuItem(models.Model):
    category = models.CharField(max_length=45)
    description = models.CharField(max_length=256)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE) # Foreign Key de Restaurant

    def __str__(self):
        return f"[MenuItem] description: {self.description[:50]}"