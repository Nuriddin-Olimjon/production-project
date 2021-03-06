from django.db import models
from api.v1.user.models import DateTimeMixinModel
from .managers import ProductManager


class Product(DateTimeMixinModel):
    PRODUCT_TYPE = (
        ('raw', 'raw'),
        ('semi-finished', 'semi-finished'),
        ('finished', 'finished'),
        ('inventory', 'inventory'),
    )

    title = models.CharField(max_length=255, unique=True, verbose_name='Nomi')
    model = models.CharField(max_length=50, unique=True, verbose_name='Model')
    code = models.CharField(max_length=50, unique=True, verbose_name='Kod')
    type = models.CharField(
        max_length=255, choices=PRODUCT_TYPE, verbose_name="Turi")
    group = models.ForeignKey(
        'ProductGroup', on_delete=models.CASCADE, verbose_name="Guruhi")

    measurement_unit = models.ForeignKey(
        'MeasurementUnit', on_delete=models.CASCADE, verbose_name="O'lchov birligi")

    arrival_price = models.PositiveIntegerField(
        default=0, verbose_name='Tan narxi')
    selling_price = models.PositiveIntegerField(
        default=0, verbose_name='Sotish narxi')
    currency = models.ForeignKey(
        'finance.Currency', on_delete=models.CASCADE, verbose_name='Valyuta')

    shelf_life = models.CharField(
        max_length=50, verbose_name='Yaroqlilik muddati')

    critical_quantity = models.FloatField(
        default=0.0, verbose_name="Kritik miqdori")

    description = models.TextField(blank=True, verbose_name="Izoh")
    further = models.TextField(blank=True, verbose_name="Qo'shimcha izoh")

    objects = ProductManager()

    class Meta:
        verbose_name = 'Mahsulot'
        verbose_name_plural = 'Mahsulotlar'

    def __str__(self):
        return self.title


class ProductGroup(models.Model):
    title = models.CharField(
        max_length=255, unique=True, verbose_name="Guruh nomi")

    class Meta:
        verbose_name = 'Mahsulot guruhi'
        verbose_name_plural = 'Mahsulot guruhlari'

    def __str__(self):
        return self.title


class MeasurementUnit(models.Model):
    title = models.CharField(max_length=30, unique=True,
                             verbose_name="O'lchov birligi nomi")

    class Meta:
        verbose_name = "O'lchov birligi"
        verbose_name_plural = "O'lchov birliklari"

    def __str__(self):
        return self.title


class Storage(DateTimeMixinModel):
    title = models.CharField(
        max_length=255, unique=True, verbose_name='Ombor nomi')
    address = models.CharField(
        max_length=255, blank=True, verbose_name='Manzil')

    class Meta:
        verbose_name = 'Ombor'
        verbose_name_plural = 'Omborlar'

    def __str__(self):
        return self.title


class ProductOrder(DateTimeMixinModel):
    TYPE = (
        ('receive', 'receive'),
        ('leave', 'leave'),
        ('plan', 'plan')
    )
    type = models.CharField(
        max_length=50, choices=TYPE, verbose_name="Turi")
    
    receive_invoice = models.ForeignKey(
        'ReceiveInvoice', on_delete=models.SET_NULL, null=True, verbose_name="Kirish faktura")
    
    leave_invoice = models.ForeignKey(
        'LeaveInvoice', on_delete=models.SET_NULL, null=True, verbose_name="Chiqish faktura")

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name="Mahsulot")

    storage = models.ForeignKey(
        Storage, on_delete=models.CASCADE, verbose_name="Ombor")

    quantity = models.FloatField(verbose_name="Miqdori")
    price = models.PositiveIntegerField(verbose_name='Narxi')
    currency = models.ForeignKey(
        'finance.Currency', on_delete=models.CASCADE, verbose_name='Valyuta')

    saved = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.product.title


class ReceiveInvoice(DateTimeMixinModel):
    STATUS = (
        ('waiting', 'waiting'),
        ('saved', 'saved'),
        ('cancelled', 'cancelled'),
    )
    supplier = models.ForeignKey(
        'supplier.Supplier', on_delete=models.CASCADE, verbose_name="Ta'minotchi")
    storage = models.ForeignKey(
        Storage, on_delete=models.CASCADE, verbose_name='Ombor')
    responsible = models.CharField(
        max_length=50, blank=True, verbose_name="Mas'ul shaxs")
    status = models.CharField(
        max_length=30, choices=STATUS, default='Waiting', verbose_name="Status")
    description = models.TextField(blank=True, verbose_name='Izoh')
    further = models.TextField(blank=True, verbose_name="Qo'shimcha izoh")

    class Meta:
        verbose_name = "Qabul faktura"
        verbose_name_plural = "Qabul fakturalar"

    def __str__(self):
        return f"Kirim {self.id}"


class LeaveInvoice(DateTimeMixinModel):
    STATUS = (
        ('in-progress', 'in-progress'),
        ('waiting', 'waiting'),
        ('saved', 'saved'),
        ('cancelled', 'cancelled'),
    )
    storage = models.ForeignKey(
        Storage, on_delete=models.CASCADE, verbose_name='Ombor')
    client = models.ForeignKey(
        'sales.Client', on_delete=models.CASCADE, verbose_name='Mijoz')
    deadline = models.DateField(null=True, blank=True, verbose_name='Muddati')
    responsible = models.CharField(
        max_length=50, blank=True, verbose_name="Mas'ul shaxs")
    status = models.CharField(max_length=30, choices=STATUS, default='Waiting')
    created_by = models.ForeignKey(
        'user.User', on_delete=models.CASCADE, related_name='invoices', verbose_name='Hodim')
    description = models.TextField(blank=True, verbose_name='Izoh')
    further = models.TextField(blank=True, verbose_name="Qo'shimcha izoh")

    class Meta:
        verbose_name = "Chiqish faktura"
        verbose_name_plural = "Chiqish fakturalar"

    def __str__(self):
        return f"Chiqish {self.id}"


class DefectiveProduct(DateTimeMixinModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name="defective_products", verbose_name="Mahsulot nomi")
    quantity = models.FloatField(verbose_name="Miqdori")
    valid_status = models.BooleanField(verbose_name="Qayta ishlashga yaroqlik")
    returned_status = models.BooleanField(verbose_name="Sotuvdan qaytgan")
    storage = models.ForeignKey(Storage, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Buzilgan mahsulot'
        verbose_name_plural = 'Buzilgan mahsulotlar'

    def __str__(self) -> str:
        return self.product.name
