from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Kuxnya(models.Model):
    name = models.CharField(max_length=225)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
# Модель для поиска статей
class Zavedeniye(models.Model):
    name = models.CharField(max_length=225)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=200)
    contact_info = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos', blank=True)  # Фото ресторана
    menu = models.ManyToManyField('Menu', related_name='restaurants', blank=True)  # Связь с блюдами
    kuxnya = models.ForeignKey(Kuxnya, on_delete=models.CASCADE)
    zavedeniye = models.ForeignKey(Zavedeniye, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    menu_photo = models.ImageField(upload_to='photos', blank=True)  # Фото пункта меню
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
class Review(models.Model):
    user_name = models.CharField(max_length=100)
    text = models.TextField()
    date_published = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return f'Review by {self.user_name} for {self.restaurant.name}'
class Menu(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    menu_photo = models.ImageField(upload_to='photos', blank=True)


    def __str__(self):
        return self.name
class Reservation(models.Model):
    user = models.CharField(max_length=100)
    time = models.DateTimeField(max_length=100)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    desired_table = models.CharField(max_length=100)




