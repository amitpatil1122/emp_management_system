from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login_page, name='login.html'),
    path('check_login', views.check_login, name='check_login'),
    path('index', views.index, name='index'),
    path('view_employee', views.view_employee, name='view_employee'),
    path('add_employee', views.add_employee, name='add_employee'),
    path('new_emp', views.new_emp, name='new_emp'),
    path('remove_employee', views.remove_employee, name='remove_employee'),
    path('remove_emp', views.remove_emp, name='remove_emp'),
    path('filter_employee', views.filter_employee, name='filter_employee'),
    path('filter_emp', views.filter_emp, name='filter_emp'),
    path('edit_employee', views.edit_employee, name='edit_employee'),
    path('edit_emp', views.edit_emp, name='edit_emp'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('registration', views.registration, name='registration'),
    path('signup', views.signup, name='signup'),
    path('forgot_pass', views.forgot_pass, name='forgot_pass'),
    path('forgot_password', views.forgot_password, name='forgot_password'),
    path('reset_password', views.reset_password, name='reset_password'),
    path('new_password', views.new_password, name='new_password')
]
