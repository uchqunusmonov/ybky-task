from rest_framework import generics
from rest_framework.views import APIView
from .pagination import CustomPagination
from . import serializers
from .models import Room, Resident, Availability
from rest_framework.response import Response
import datetime


class RoomListView(generics.ListAPIView):
    queryset = Room.objects.all()
    pagination_class = CustomPagination
    serializer_class = serializers.RoomSerializer


class RoomDetailView(APIView):
    def get(self, request, pk: int) -> Room:
        try:
            room = Room.objects.get(id=pk)
        except Room.DoesNotExist:
            return Response(
                {"error": "topilmadi"}
            )
        serializer = serializers.RoomSerializer(room)
        return Response(serializer.data)


class RoomAvailabilityView(APIView):
    def get(self, request, pk: int) -> Availability:
        try:
            room = Room.objects.get(id=pk)
        except Room.DoesNotExist:
            return Response(
                {'error': 'topilmadi'}
            )
        date = request.query_params.get('date', None)
        if not date:
            date = datetime.date.today()

        availabilities = Availability.objects.filter(room=room, start__date=date)
        serializer = serializers.AvailabilitySerializer(availabilities, many=True)

        return Response(serializer.data)


class RoomReservation(APIView):
    def post(self, request, pk):
        try:
            room = Room.objects.get(id=pk)
        except Room.DoesNotExist:
            return Response(
                {'error': 'topilmadi'}
            )
        resident_data = request.data.get('resident', None)
        start_time = request.data.get('start', None)
        end_time = request.data.get('end', None)

        if not resident_data or not start_time or not end_time:
            return Response({'error': "Malumotlar to'liq kiritilmadi"})

        try:
            start_datetime = datetime.datetime.strptime(start_time, '%d-%m-%Y %H:%M:%S')
            end_datetime = datetime.datetime.strptime(end_time, '%d-%m-%Y %H:%M:%S')
        except ValueError:
            return Response({'error': "Noto'g'ri vaqt formati"})

        if Availability.objects.filter(room=room, start__lt=end_datetime, end__gt=start_datetime).exists():
            return Response({'error': "uzr, siz tanlagan vaqtda xona band"})

        resident_serializer = serializers.ResidentSerializer(data=resident_data)
        if resident_serializer.is_valid():
            resident = resident_serializer.save()
            room.resident = resident
            room.save()

            availability = Availability(room=room, start=start_datetime, end=end_datetime)
            availability.save()

            return Response({'message': 'Xona muvaffaqiyatli band qilindi'})
        else:
            return Response(resident_serializer.errors)