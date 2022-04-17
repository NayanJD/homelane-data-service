from django.db import models
from uuid import uuid4

class Home(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    
    date = models.DateTimeField("date")
    price = models.FloatField()
    bedrooms = models.IntegerField()
    bathrooms = models.FloatField()
    sqft_living = models.FloatField()
    sqft_lot = models.FloatField()
    floors = models.IntegerField()
    waterfront = models.BooleanField()
    view = models.IntegerField()
    condition = models.IntegerField()
    sqft_above = models.FloatField()
    sqft_basement = models.FloatField()
    yr_built = models.FloatField("year built")
    yr_renovated = models.FloatField("year renovated")

    created_at = models.DateTimeField("created at", auto_now_add=True)
    updated_at = models.DateTimeField("updated at", auto_now=True)
    archived_at = models.DateTimeField("archived at", null=True, blank=True)

    class Meta:
        db_table = "home"