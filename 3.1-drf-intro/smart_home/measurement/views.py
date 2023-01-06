from rest_framework.generics import RetrieveAPIView, UpdateAPIView, ListCreateAPIView

from .models import Sensor, Measurement
from .serializers import SensorDetaidSerializer, SensorSerializer, MeasurementOneSerializer


# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

# Один датчик - просмотр/редактировать
class SensorViewOne(RetrieveAPIView, UpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetaidSerializer

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


# Список датчиков -просмотр/добавить
class SensorViewList(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# Список температуры -просмотр/добавить
class MeasurementViewList(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementOneSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
