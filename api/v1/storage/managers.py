from django.db.models import Manager, Sum, Q


class ProductManager(Manager):

    def with_quantity(self, storage=None):

        if storage is None:
            queryset = self.annotate(
                quantity=Sum("productorder__quantity")
            ).order_by('id')

        if storage is not None:
            queryset = self.annotate(
                quantity=Sum(
                    "productorder__quantity", filter=Q(productorder__storage_id=storage)
                )
            ).order_by('id')

        return queryset
