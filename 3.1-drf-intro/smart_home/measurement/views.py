from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.response import Response
from .models import Sensor
from .serializers import SensorDetailSerializer, MeasurementSerializer

class SensorsView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            obj = serializer.save()
            return Response(serializer.data)

class SensorView(RetrieveUpdateDestroyAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def post(self, request, pk):
        Sensor = self.get_object(pk)
        serializer = SensorDetailSerializer(Sensor, data=request.data,
                                         partial=True)
        if serializer.is_valid():
            obj = serializer.save()
            return Response(serializer.data)

class MeasurementView(ListCreateAPIView):
    serializer_class = MeasurementSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            obj = serializer.save()
            return Response(serializer.data)