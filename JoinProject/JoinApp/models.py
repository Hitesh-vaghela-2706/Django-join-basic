from django.db import models

class Country(models.Model):
    id = models.AutoField(primary_key=True)
    country_name = models.CharField(max_length=255, unique=True)
    country_currency = models.CharField(max_length=255)
    country_capital = models.CharField(max_length=255)

    class Meta:
       db_table = "country" 
       
          
    def __str__(self):
        return self.country_name

class State(models.Model):
    id = models.AutoField(primary_key=True)
    state_name = models.CharField(max_length=255)
    state_capital = models.CharField(max_length=255)
    state_language = models.CharField(max_length=255, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    class Meta:
        db_table = "state"

    def __str__(self):
        return self.state_name
