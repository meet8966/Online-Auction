import datetime
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.utils import timezone


class Product(models.Model):

    name = models.CharField(max_length=50, blank=False)
#   desp = models.TextField(max_length=500, blank=True)
#   image = models.FileField(upload_to=)
#   category = models.CharField(max_length=50, blank=True)
#   minimum_price = models.IntegerField(blank=True, validators=[MinValueValidator(1)])
#   start = models.DateTimeField()
#   end_date = models.DateField(default=None)
#   end_time = models.TimeField(default=None)
#   current_bid = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.name

    # def was_published_recently(self):
    #
    #     return self.start >= timezone.now() - datetime.timedelta(days=1)

# class buyer(models.Model):
#
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     bid_amount = models.IntegerField(validators=[MinValueValidator(1)])
#
#     def __str__(self):
#         return self.user.username


# class Bidsmade(models.Model):
#
#     product = models.ForeignKey(Product,on_delete=models.CASCADE)
#     bidder_name = models.CharField(max_length=30, blank=False)
#     bid_time = models.TimeField(timezone.now())
#     bid_amount = models.DecimalField(max_digits=10,decimal_places=2)
#
#     def __str__(self):
#         return self.product.name


# class seller(models.Model):
#
#     created = models.DateTimeField(auto_now_add=True)
#
#     user_name = models.ForeignKey(User,on_delete=models.CASCADE)
#     product_name = models.ForeignKey(Product,on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.




