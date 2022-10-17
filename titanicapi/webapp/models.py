import uuid
from django.db import models


class Titanic(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable = False)
    survived = models.BooleanField()
    passenger_class = models.IntegerField()
    name = models.CharField(max_length=45)
    sex = models.CharField(max_length=6)
    age = models.IntegerField()
    siblings_spousesaboard = models.IntegerField()
    parents_childrenaboard = models.IntegerField()
    fare = models.FloatField(db_column='fare')

    class Meta:
        managed = True
        db_table = 'titanic'
