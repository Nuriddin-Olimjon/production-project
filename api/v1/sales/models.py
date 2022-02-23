from django.db import models
from api.v1.user.models import DateTimeMixinModel
from api.v1.user.models import phone_regex


class Client(DateTimeMixinModel):
    title = models.CharField(
        max_length=255, unique=True, verbose_name='Firma nomi')
        
    fullname = models.CharField(max_length=255, verbose_name='Direktor FIO')

    phone_number = models.CharField(
        max_length=15, blank=True, validators=(phone_regex,), verbose_name='Telefon raqami')

    city = models.ForeignKey(
        'City', on_delete=models.CASCADE, verbose_name="Shahar")

    address = models.CharField(
        max_length=255, blank=True, verbose_name='Manzil')

    bank_mfo = models.CharField(max_length=50, blank=True, verbose_name="Bank MFO")
    bank_inn = models.CharField(max_length=50, blank=True, verbose_name="Bank INN")
    bank_account = models.CharField(max_length=50, blank=True, verbose_name="Hisob raqami")

    description = models.TextField(blank=True, verbose_name='Izoh')

    class Meta:
        verbose_name = 'Mijoz'
        verbose_name_plural = 'Mijozlar'

    def __str__(self):
        return self.title


class City(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name='Shahar nomi')

    class Meta:
        verbose_name = 'Shahar'
        verbose_name_plural = "Shaharlar"

    def __str__(self):
        return self.title


# class Plan(models.Model):
#     TYPE = (
#         ('summa', 'summa'),
#         ('count', 'count')
#     )
#     type = models.CharField(max_length=5, choices=TYPE, default='summa')
#     seller = models.ForeignKey(
#         'user.User', on_delete=models.CASCADE, related_name='seller_plan')
#     client = models.ManyToManyField(Client)
#     city = models.ManyToManyField(City)
#     product = models.ManyToManyField(
#         'storage.Product', related_name='seller_plan')
#     summa = models.PositiveIntegerField(default=0)
#     success_sum = models.PositiveIntegerField(default=0)
#     count = models.PositiveIntegerField(default=0)
#     success_count = models.PositiveIntegerField(default=0)
#     currency = models.ForeignKey(
#         'storage.Currency', on_delete=models.CASCADE, default=1)
#     deadline = models.DateField()
#     active = models.BooleanField(default=True)
#     created_at = models.DateField(auto_now_add=True)
#     updated_at = models.DateField(auto_now=True)

#     class Meta:
#         verbose_name = 'Sotuv reja'
#         verbose_name_plural = 'Sotuv rejalar'

#     def __str__(self):
#         return f"{self.id} {self.seller.first_name} {self.seller.last_name}"
