from django.db.models import Manager, Sum


class ProductManager(Manager):
    def with_quantity(self):
        return self.annotate(quantity=Sum("receiveinvoiceorder__quantity")-Sum("leaveinvoiceorder__quantity"))
