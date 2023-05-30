from django.shortcuts import render
from Content import models, serializers
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly, AllowAny, IsAuthenticated
from django.template.loader import render_to_string
from django.core.mail import EmailMessage


# Create your views here.


class ServiceView(generics.ListCreateAPIView):
    queryset = models.Services.objects.all()
    serializer_class = serializers.ServiceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class TeamsView(generics.ListCreateAPIView):
    queryset = models.Teams.objects.all()
    serializer_class = serializers.TeamsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class TestimonialsView(generics.ListCreateAPIView):
    queryset = models.Testimonials.objects.all()
    serializer_class = serializers.TestimonialsSerializer


class BlogsView(generics.ListCreateAPIView):
    queryset = models.Blogs.objects.all()
    serializer_class = serializers.BlogsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class NewslettersView(generics.ListCreateAPIView):
    queryset = models.Newsletters.objects.all()
    serializer_class = serializers.NewslettersSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = [AllowAny]
        elif self.request.method == 'GET':
            self.permission_classes = [IsAuthenticated, IsAdminUser]

        return super().get_permissions()


class CareersView(generics.ListCreateAPIView):
    queryset = models.Careers.objects.all()
    serializer_class = serializers.CareersSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = [AllowAny]
        elif self.request.method == 'GET':
            self.permission_classes = [IsAuthenticated, IsAdminUser]

        return super().get_permissions()

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        valid_data = serializer.validated_data

        html_mail = render_to_string('career_html_mail.html', valid_data)

        message = f"New Career Submission:\n\n"
        for key, value in valid_data.items():
            message += f"{key}: {value}\n"

        if 'resume' in request.FILES:
            file = request.FILES['resume']
            attachment = (file.name, file.read(), file.content_type)
        else:
            attachment = None

        email = EmailMessage(
            from_email='mail@domain.com',
            to=['mail@domain.com'],
            subject=f"New Career Submission By: {valid_data['name']}",
            body=html_mail
        )

        if attachment:
            email.attach(*attachment)
        email.content_subtype = 'html'
        email.send(fail_silently=False)

        return self.create(request, *args, *kwargs)


# single view
class SingleServiceView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Services.objects.all()
    serializer_class = serializers.ServiceSerializer
    permission_classes = [IsAdminUser]


class SingleTeamView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Teams.objects.all()
    serializer_class = serializers.TeamsSerializer
    permission_classes = [IsAdminUser]


class SingleTestimonialView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Testimonials.objects.all()
    serializer_class = serializers.TestimonialsSerializer


class SingleBlogView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Blogs.objects.all()
    serializer_class = serializers.BlogsSerializer
    permission_classes = [IsAdminUser]


class SingleNewsletterView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Newsletters.objects.all()
    serializer_class = serializers.NewslettersSerializer
    permission_classes = [IsAdminUser]


class SingleCareerView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Careers.objects.all()
    serializer_class = serializers.CareersSerializer
    permission_classes = [IsAdminUser]
