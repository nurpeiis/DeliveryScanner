from django.db import models

# Create your models here.
#model to save the data about delivery from different restaurants to different food
class Pricedata(models.Model):
    dishname = models.TextField(db_column='DishName', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    price = models.FloatField(db_column='Price', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    restaurant = models.TextField(db_column='Restaurant', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    foodurl = models.URLField(db_column='foodURL', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    deliveryapp = models.TextField(db_column='DeliveryApp', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    imageurl = models.URLField(db_column='imageURL', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    class Meta:
        db_table = 'PriceData'
    