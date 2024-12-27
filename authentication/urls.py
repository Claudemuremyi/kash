# from django.urls import path
# from . import views
# from django.contrib.auth.views import LogoutView

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('register/', views.register, name='register'),
#     path('login/', views.login_view, name='login'),
#     path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
#     path('verify/<str:token>/', views.verify_email, name='verify_email'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]

