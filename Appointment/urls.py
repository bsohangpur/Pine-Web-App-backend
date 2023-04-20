from django.urls import path
from Appointment import views

urlpatterns = [
    path('appointments/', views.AppointmentView.as_view(), name='appointment_form'),
    path('appointments/<int:pk>', views.SingleAppointmentView.as_view(),
         name='single_appointment_form')
]
