from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serialziers import NavigationRecordSerializer
from .models import NavigationRecord
from datetime import datetime, timedelta
from django.utils.timezone import make_aware


# get all records in the last 48 hours
@api_view(['GET'])
def navigation_record_list(request):
    nav_record_list = NavigationRecord.objects.all().order_by('-vehicle').reverse()
    time_gap = datetime.now() - timedelta(hours=48)
    aware_datetime = make_aware(time_gap)
    filtered_records = nav_record_list.filter(nav_record_time__gte=aware_datetime) # activate timezone
    serializer = NavigationRecordSerializer(filtered_records, many=True)
    return Response(serializer.data)


# all records by vehicle in the last 48 hours
@api_view(['GET'])
def navigation_record(request, id):
    nav_record_list = NavigationRecord.objects.filter(vehicle=id)
    time_gap = datetime.now() - timedelta(hours=48)
    aware_datetime = make_aware(time_gap)
    filtered_records = nav_record_list.filter(nav_record_time__gte=aware_datetime) # activate timezone
    serializer = NavigationRecordSerializer(filtered_records, many=True)
    return Response(serializer.data)

