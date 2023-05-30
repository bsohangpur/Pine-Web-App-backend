from django.shortcuts import render
from rest_framework import generics, response, status
from .models import Appointment
from .serializers import AppointmentSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from django.template.loader import render_to_string
from django.core.mail import EmailMessage


# Create your views here.

class AppointmentView(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = [AllowAny]
        elif self.request.method == 'GET':
            self.permission_classes = [IsAuthenticated, IsAdminUser]

        return super().get_permissions()

    def post(self, request, *args, **kwargs):
        data = self.serializer_class(data=request.data)
        data.is_valid(raise_exception=True)
        data.save()
        validated_data = data.validated_data

        html_mail = render_to_string('appointment_html_mail.html', validated_data)
        email = EmailMessage(
            subject=f"New Appointment Submission By: {validated_data['first_name']} {validated_data['last_name']}",
            from_email='mail@domain.com',
            to=['mail@domain.com'],
            body=html_mail
        )

        email.content_subtype = 'html'
        email.send(fail_silently=False)

        return self.create(request, *args, *kwargs)


class SingleAppointmentView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
