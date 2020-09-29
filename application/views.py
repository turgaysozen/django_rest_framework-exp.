from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


# api_overview
@api_view(['GET'])
def api_overview(request):
    api_overview = {
        "All Navigation List": "/navigation/navigation-list",
        "Single Navigation Data": "/navigation/navigation/<int:id>",
        "Add Operation": "/collection/add-operation",
        "List Operation": "/collection/list-operation",
        "List Bin": "/collection/list-bin"

    }
    return Response(api_overview)
