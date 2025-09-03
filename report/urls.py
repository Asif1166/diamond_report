from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('report/', views.report, name='report'),
    path('contact/', views.contact, name='contact'),

    path('get-report-data/', views.get_report_data, name='get_report_data'),



]