from django.db import models

# Create your models here.
class Actionmovies(models.Model):
    moviename = models.CharField(max_length=45, blank=True, null=True)
    countryid = models.ForeignKey('Countries', models.DO_NOTHING, db_column='countryid', blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'actionmovies'


class Countries(models.Model):
    countryname = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'countries'