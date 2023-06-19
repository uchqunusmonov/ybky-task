from rest_framework import generics
from rest_framework.views import APIView
from .pagination import CustomPagination
from . import serializers
from .models import Room, Resident, Availability
from rest_framework.response import Response


class RoomListView(generics.ListAPIView):
    queryset = Room.objects.all()
    pagination_class = CustomPagination
    serializer_class = serializers.RoomListSerializer


class RoomDetailView(APIView):
    def get(self, request, pk: int) -> Room:
        try:
            room = Room.objects.get(id=pk)
        except Room.DoesNotExist:
            return Response(
                {"error": "topilmadi"}
            )
        serializer = serializers.RoomDetailSerializer(room)
        return Response(serializer.data)
