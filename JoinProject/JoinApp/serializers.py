from rest_framework import serializers
from .models import Country, State

class CountrySerializer(serializers.ModelSerializer):
  class Meta:
    model = Country
    fields = [ "country_name","country_currency","country_capital"]  # Include all fields

class StateSerializer(serializers.ModelSerializer):
  country = CountrySerializer(read_only=True)  # Nested serializer for Country

  class Meta:
    model = State
    fields = ['id', 'state_name', 'state_capital', 'state_language', 'country_id','country']
