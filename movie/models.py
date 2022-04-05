from django.db import models





class Movie(models.Model):
    mid = models.AutoField(primary_key=True)
    mname = models.CharField(unique=True, max_length=100)
    mdesc = models.TextField(blank=True, null=True)
    mimg = models.CharField(max_length=120)
    mlink = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'movie'
