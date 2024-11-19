from django.contrib import admin
from django.urls import path,include
from .views import indexview,create_book,update_book,delete_book,login_view,logout_view,signup_view
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('',indexview,name='home'),
    path('create/',create_book,name='create'),
    path('update/<int:id>',update_book,name='update'),
    path('delete/<int:id>',delete_book,name='delete'),
    path('login/',login_view,name='login'),
    path('logout/',logout_view,name='logout'),
    path('signup/',signup_view,name='signup'),

    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset_done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('password_reset_complete/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete')
]   