from django.urls import path
from Content import views

urlpatterns = [
    path('services/', views.ServiceView.as_view(), name='services'),
    path('services/<int:pk>/', views.SingleServiceView.as_view(), name='service-detail'),

    path('teams/', views.TeamsView.as_view(), name='teams'),
    path('teams/<int:pk>/', views.SingleTeamView.as_view(), name='team-detail'),

    path('testimonials/', views.TestimonialsView.as_view(), name='testimonials'),
    path('testimonials/<int:pk>/', views.SingleTestimonialView.as_view(), name='testimonial-detail'),

    path('blogs/', views.BlogsView.as_view(), name='blogs'),
    path('blogs/<int:pk>/', views.SingleBlogView.as_view(), name='blog-detail'),

    path('newsletters/', views.NewslettersView.as_view(), name='newsletters'),
    path('newsletters/<int:pk>/', views.SingleNewsletterView.as_view(), name='newsletter-detail'),

    path('careers/', views.CareersView.as_view(), name='careers'),
    path('careers/<int:pk>/', views.SingleCareerView.as_view(), name='career-detail'),
]
