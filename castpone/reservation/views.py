from django.shortcuts import render

# Create your views here.
from .serializer import MenuSerializer
from rest_framework import generics
from .models import menu_table

def index(request):
    return render(request, 'index.html', {})

class menuitemview(generics.ListCreateAPIView):
    queryset = menu_table.objects.all()
    serializer_class = MenuSerializer



class singleitemview(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = menu_table.objects.all()
    serializer_class = MenuSerializer