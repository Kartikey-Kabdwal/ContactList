from django.urls import path
from contactlist import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.user_signup, name='signup'),
    path('contact_list/', views.contact_list, name='contact_list'),
    path('contact/add/', views.add_contact, name='add_contact'),
    path('contact/edit/<int:pk>/', views.edit_contact, name='edit_contact'),
    path('contact/delete/<int:pk>/', views.delete_contact, name='delete_contact'),
]
