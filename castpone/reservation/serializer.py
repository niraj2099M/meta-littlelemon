from rest_framework import serializers
from . models import menu_table

class MenuSerializer (serializers.ModelSerializer): 
    class Meta:
        model = menu_table
        fields = '__all__'


