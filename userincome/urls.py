# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.income_list, name='income'),
#     path('add/', views.add_income, name='add_income'),
#     path('edit/<int:id>/', views.edit_income, name='edit_income'),
#     path('delete/<int:id>/', views.delete_income, name='delete_income'),
#     path('source-summary/', views.income_source_summary, name='income_source_summary'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.income_list, name='income'),
    path('add/', views.add_income, name='add_income'),
    path('edit/<int:id>/', views.edit_income, name='edit_income'),
    path('delete/<int:id>/', views.delete_income, name='delete_income'),
    path('source-summary/', views.income_source_summary, name='income_source_summary'),
]

