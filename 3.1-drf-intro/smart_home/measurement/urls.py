from django.urls import path

from measurement import views

urlpatterns = [
    path("create_sensor/", views.SensorCreateView.as_view()),
    path("sensors_list/", views.SensorListView.as_view()),
    path("sensor_update/<pk>/", views.SensorUpdateView.as_view()),
    path("create_measurement/", views.MeasurementCreateView.as_view()),
    path("sensor_detail/<pk>/", views.SensorDetailListView.as_view())
    # TODO: зарегистрируйте необходимые маршруты
]
