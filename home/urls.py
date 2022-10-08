from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
    path('login/',views.LoginInterfaceView.as_view(),name='login'),
    path('logout/',views.LogoutInterfaceView.as_view(),name='logout'),
    path('signup/',views.SignupCreateView.as_view(),name='signup'),
    path('dash/',views.DoctorListView.as_view(),name='dash'),
    path('details/<int:pk>/',views.PatientDetailView.as_view(),name='details'),

]
