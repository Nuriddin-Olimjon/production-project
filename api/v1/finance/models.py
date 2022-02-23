from tabnanny import verbose
from django.db import models
from api.v1.user.models import DateTimeMixinModel


class Income(DateTimeMixinModel):
    PAYMENT_TYPE = (
        ('cash', 'cash'),
        ('card', 'card'),
        ('bank', 'bank')
    )
    TYPE = (
        ('client', 'client'),
        ('extra', 'extra')
    )

    cashbox = models.ForeignKey(
        'Cashbox', on_delete=models.CASCADE, verbose_name="Kassa nomi")

    type = models.CharField(max_length=255, choices=TYPE,
                            verbose_name="Kirim turi")

    client = models.ForeignKey(
        'sales.Client', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Mijoz")

    extra_income_title = models.CharField(
        max_length=255, blank=True, verbose_name="Extra kirim nomi")

    payment_type = models.CharField(
        max_length=50, choices=PAYMENT_TYPE, verbose_name="To'lov turi")

    total_sum = models.PositiveIntegerField(verbose_name="Summa miqdori")

    currency = models.ForeignKey(
        'Currency', on_delete=models.CASCADE, verbose_name="Valyuta")

    description = models.TextField(blank=True, verbose_name='Izoh')

    created_by = models.ForeignKey(
        'user.User', on_delete=models.CASCADE, verbose_name='Kassir')

    class Meta:
        verbose_name = 'Kirim'
        verbose_name_plural = 'Kirim'

    def __str__(self) -> str:
        return f"Kirim {self.id}"


class Payment(DateTimeMixinModel):
    PAYMENT_TYPE = (
        ('cash', 'cash'),
        ('card', 'card'),
        ('bank', 'bank')
    )
    cost_type = models.ForeignKey(
        'CostType', on_delete=models.CASCADE, verbose_name="Chiqim turi")

    cashbox = models.ForeignKey(
        'Cashbox', on_delete=models.CASCADE, verbose_name="Kassa")

    to_where = models.CharField(
        max_length=255, verbose_name="Qayerga (kimga)?")

    supplier = models.ForeignKey(
        'supplier.Supplier', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Ta'minotchi")

    employee = models.ForeignKey(
        'user.User', on_delete=models.SET_NULL, null=True, blank=True, related_name='payments', verbose_name="Hodim")

    sub_cost_type = models.ForeignKey('SubCostType', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Sub kategoriya")

    bonus = models.PositiveIntegerField(
        blank=True, null=True, verbose_name="Bonus")

    bonus_reason = models.CharField(
        max_length=255, blank=True, verbose_name="Bonus sababi")

    fine = models.PositiveIntegerField(
        blank=True, null=True, verbose_name="Jarima")

    fine_reason = models.CharField(
        max_length=255, blank=True, verbose_name="Jarima sababi")

    payment_type = models.CharField(
        max_length=50, choices=PAYMENT_TYPE, verbose_name="To'lov turi")

    total_sum = models.PositiveIntegerField(verbose_name="Summa miqdori")

    currency = models.ForeignKey(
        'Currency', on_delete=models.CASCADE, verbose_name="Valyuta")

    description = models.TextField(blank=True, verbose_name="Izoh")

    created_by = models.ForeignKey(
        'user.User', on_delete=models.CASCADE, verbose_name="Kassir")

    class Meta:
        verbose_name = "Chiqim"
        verbose_name_plural = "Chiqim"

    def __str__(self) -> str:
        return f"Chiqim {self.id}: {self.to_where}"


class CostType(models.Model):
    title = models.CharField(max_length=50, unique=True,
                             verbose_name="Chiqim turi nomi")
    to_supplier = models.BooleanField(
        default=False, verbose_name="Ta'minotchiga")
    to_employee = models.BooleanField(
        default=False, verbose_name="Hodim uchun maosh")

    class Meta:
        verbose_name = "Chiqim turi"
        verbose_name_plural = "Chiqim turlari"

    def __str__(self):
        return self.title


class SubCostType(models.Model):
    type = models.ForeignKey(
        CostType, on_delete=models.CASCADE, verbose_name="Chiqim turi")
    title = models.CharField(max_length=255, verbose_name="Subkategoriya nomi")

    class Meta:
        verbose_name = "Chiqim subkategoriya"
        verbose_name_plural = "Chiqim subkategoriya"
        unique_together = ('type', 'title')

    def __str__(self):
        return f"{self.type.title}: {self.title}"


class Cashbox(models.Model):
    title = models.CharField(
        max_length=255, unique=True, verbose_name="Kassa nomi")
    cashier = models.OneToOneField('user.User', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Kassa"
        verbose_name_plural = "Kassalar"

    def __str__(self) -> str:
        return self.title


class Currency(models.Model):
    title = models.CharField(max_length=30, unique=True,
                             verbose_name="Valyuta nomi")

    class Meta:
        verbose_name = "Valyuta"
        verbose_name_plural = "Valyutalar"

    def __str__(self):
        return self.title
