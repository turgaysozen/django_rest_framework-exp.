from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serialziers import OperationSerializer, BinSerializer
from .models import Operation, Bin


# get all operations
@api_view(['GET'])
def list_operation(request):
    operations = Operation.objects.all()
    serializer = OperationSerializer(operations, many=True)
    return Response(serializer.data)


# post operation and update collection_frequency and last_collection of bin model.
@api_view(['POST'])
def add_operation(request):
    serializer = OperationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    # to find collection_frequency: filter operation object and find days gap of last 2 data
    operation_list = Operation.objects.filter(bin=request.data["bin"]).order_by('-id')
    collection_frequency = 0
    if len(operation_list) >= 2:
        collection_frequency = (operation_list[0].operation_date - operation_list[1].operation_date).days

    # and update current bind by actual data
    current_bin = Bin.objects.filter(id=request.data["bin"]).first()

    bin = {
        "id": request.data["bin"],
        "latitude": current_bin.latitude,
        "longitude": current_bin.longitude,
        "collection_frequency": collection_frequency,
        "last_collection": request.data["operation_date"]
    }

    bin_serializer = BinSerializer(instance=current_bin, data=bin)
    if bin_serializer.is_valid():
        bin_serializer.save()

    return Response(serializer.data)


# get all Bin
@api_view(['GET'])
def list_bin(request):
    operations = Bin.objects.all()
    serializer = BinSerializer(operations, many=True)
    return Response(serializer.data)
