from django.db import models


class Item(models.Model):
    number = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=255)

    width = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    height = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    depth = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    style = models.CharField(max_length=255, blank=True, null=True)
    material = models.CharField(max_length=255, blank=True, null=True)
    year_created = models.PositiveIntegerField(blank=True, null=True)
    origin = models.CharField(max_length=255, blank=True, null=True)
    condition = models.CharField(max_length=255, blank=True, null=True)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    is_available_for_sale = models.BooleanField(default=True)  # Pole True/False

    image = models.ImageField(upload_to='items/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    status = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=350, blank=True, null=True)

    def __str__(self):
        return f"{self.number} - {self.name}"
