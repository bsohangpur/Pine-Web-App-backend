from rest_framework import serializers
from Content import models

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Services
        fields='__all__'

class TeamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teams
        fields = '__all__'

class TestimonialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Testimonials
        fields = '__all__'

class BlogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Blogs
        fields = '__all__'

class NewslettersSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Newsletters
        fields = '__all__'

class CareersSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Careers
        fields = '__all__'