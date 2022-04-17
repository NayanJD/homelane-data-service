from django.db import models

class Address(models.Model):

    home = models.ForeignKey("Home", related_name="address", primary_key=True, on_delete=models.CASCADE)

    street = models.TextField()
    city = models.TextField()
    statezip = models.TextField()
    country = models.TextField()

    created_at = models.DateTimeField("created at", auto_now_add=True)
    updated_at = models.DateTimeField("updated at", auto_now=True)
    archived_at = models.DateTimeField("archived at", null=True, blank=True)

    class Meta:
        db_table = "address"