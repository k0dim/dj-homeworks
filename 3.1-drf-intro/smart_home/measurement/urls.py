from django.urls import path

from measurement.views import SensorViewList, SensorViewOne, MeasurementViewList

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorViewList.as_view()),
    path('sensors/<pk>/', SensorViewOne.as_view()),
    path('measurements/', MeasurementViewList.as_view()),
]
