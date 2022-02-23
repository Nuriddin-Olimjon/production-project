from django.contrib import admin
from .models import Currency, Cashbox, CostType, SubCostType


admin.site.register(Currency)
admin.site.register(Cashbox)
admin.site.register(CostType)
admin.site.register(SubCostType)
