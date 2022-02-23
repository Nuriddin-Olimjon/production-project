from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from .managers import CustomUserManager


phone_regex = RegexValidator(
    regex=r"^((\+998)|(998))\d{9}$",
    message="Telefon raqami mana bunday bo'lishi kerak: `998901234567`",
)


class DateTimeMixinModel(models.Model):
    time_created = models.DateTimeField(
        auto_now_add=True, verbose_name="Qo'shilgan sana")
    time_updated = models.DateTimeField(
        auto_now=True, verbose_name="Yangilangan sana")

    class Meta:
        abstract = True


class User(DateTimeMixinModel, AbstractUser):
    ROLES = (
        ("director", "director"),
        ("sales-director", "sales-director"),
        ("sales-manager", "sales-manager"),
        ("stockman", "stockman"),
        ("supplier", "supplier"),
        ("technolog", "technolog"),
        ("production-director", "production-director"),
        ("controller", "controller"),
        ("cashier", "cashier"),
    )

    role = models.CharField(
        max_length=255, choices=ROLES, verbose_name="Lavozim")

    first_name = models.CharField(max_length=255, verbose_name="Ism")
    last_name = models.CharField(max_length=255, verbose_name="Familiya")
    second_name = models.CharField(
        max_length=255, blank=True, verbose_name="Otasining ismi")

    phone_number = models.CharField(
        max_length=15, blank=True, validators=(phone_regex,), verbose_name="Telefon raqami")
    address = models.CharField(
        max_length=255, blank=True, verbose_name="Yashash manzili")

    salary = models.PositiveIntegerField(default=0, verbose_name="Maosh")
    currency = models.ForeignKey(
        'finance.Currency', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Valyuta")

    image = models.ImageField(
        upload_to='photos/%y/%m/%d', null=True, blank=True, verbose_name="Rasmi")

    storages = models.ManyToManyField(
        'storage.Storage', blank=True, verbose_name="Omborlar")

    objects = CustomUserManager()

    class Meta:
        verbose_name = "Foydalanuvchi"
        verbose_name_plural = "Foydalanuvchilar"

    def __str__(self):
        return f"{self.role}. {self.first_name} {self.last_name}"
