#from .views import Tasks
from django.urls import path, include
from .views import navigation_record_list, navigation_record

urlpatterns = [
    path('navigation-list/', navigation_record_list, name='all_navigation-record-list'),
    path('navigation/<int:id>/', navigation_record, name='navigation-record-list')
]
