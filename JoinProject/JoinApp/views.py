from rest_framework.views import APIView
from rest_framework.response import Response
from .models import State, Country
from .serializers import StateSerializer, CountrySerializer
from rest_framework import status

# join query 

class StateListView(APIView):
    def get(self, request):
        states = State.objects.prefetch_related('country').all()
        serializer = StateSerializer(states, many=True)
        return Response(serializer.data)
