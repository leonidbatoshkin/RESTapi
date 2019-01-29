from django.db import models


class OrderQuerySet(models.QuerySet):
    pass


class OrderManager(models.Manager):
    def get_queryset(self):
        return OrderQuerySet(self.model, using=self._db)


class Order(models.Model):
    slug = models.SlugField(max_length=100)
    description = models.TextField(null=True, blank=True)
    cost = models.IntegerField()

    objects = OrderManager()

    def __str__(self):
        return str(self.description)[:50]

    class Meta:
        verbose_name = "Order post"
        verbose_name_plural = "Order posts"
