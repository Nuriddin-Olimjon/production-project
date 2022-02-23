from django.contrib import admin
from .models import (Product, ProductGroup, MeasurementUnit, 
                     ProductOrder, ReceiveInvoice, LeaveInvoice, Storage)

admin.site.register(Product)
admin.site.register(ProductGroup)
admin.site.register(MeasurementUnit)
admin.site.register(Storage)
admin.site.register(ProductOrder)
admin.site.register(ReceiveInvoice)
admin.site.register(LeaveInvoice)
