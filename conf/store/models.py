from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

# Create your models here.
class books(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
#     # Добавьте другие поля на ваш выбор
    def __str__(self):
        return self.name

from django.db import models
from django.contrib.auth import get_user_model

class Order(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    book = models.ForeignKey(books, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    # Добавьте другие поля для заказа, если необходимо

    def save(self, *args, **kwargs):
        # Вычислите общую стоимость заказа на основе цены книги и количества
        self.total_price = self.book.price * self.quantity
        super().save(*args, **kwargs)
    # Добавьте другие поля для заказа, такие как количество, дата и т.д.

    def __str__(self):
        return f"Order #{self.id}"


#
#
# class Order(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders')
#     product = models.ForeignKey(books, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)
#     total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
#     ordered_at = models.DateTimeField(auto_now_add=True)

