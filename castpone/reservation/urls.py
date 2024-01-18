from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.menuitemview.as_view()),
    path('menu/<int:pk>', views.singleitemview.as_view()),
]