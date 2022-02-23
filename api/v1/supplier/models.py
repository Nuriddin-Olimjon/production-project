from django.db import models
from api.v1.user.models import DateTimeMixinModel
from api.v1.user.models import phone_regex


class Supplier(DateTimeMixinModel):
    title = models.CharField(
        max_length=255, unique=True, verbose_name="Firma nomi")
    fullname = models.CharField(
        max_length=255, blank=True, verbose_name="Direktor FIO")

    phone_number1 = models.CharField(max_length=15, blank=True, validators=(
        phone_regex,), verbose_name="Asosiy telefon raqami")
    phone_number2 = models.CharField(max_length=15, blank=True, validators=(
        phone_regex,), verbose_name="Qo'shimcha telefon raqami")

    responsible = models.CharField(max_length=255, blank=True, verbose_name="Mas'ul shaxs")
    address = models.CharField(max_length=255, blank=True, verbose_name="Manzil")
    
    bank_mfo = models.CharField(max_length=50, blank=True, verbose_name="Bank MFO")
    bank_inn = models.CharField(max_length=50, blank=True, verbose_name="Bank INN")
    bank_account = models.CharField(max_length=50, blank=True, verbose_name='Hisob raqami')

    description = models.TextField(blank=True, verbose_name='Izoh')

    class Meta:
        verbose_name = "Ta'minotchi"
        verbose_name_plural = "Ta'minotchilar"

    def __str__(self):
        return self.title
