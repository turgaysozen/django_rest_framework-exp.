from django.urls import path, include
from .views import add_operation, list_operation, list_bin

urlpatterns = [
    path('add-operation/', add_operation, name='add_operation'),
    path('list-operation/', list_operation, name='list_operation'),
    path('list-bin/', list_bin, name='list_bin'),

]
