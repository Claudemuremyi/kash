# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.expense_list, name='expenses'),
#     path('add/', views.add_expense, name='add_expense'),
#     path('edit/<int:id>/', views.edit_expense, name='edit_expense'),
#     path('delete/<int:id>/', views.delete_expense, name='delete_expense'),
#     path('category-summary/', views.expense_category_summary, name='expense_category_summary'),
# ]

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.expense_list, name='expenses'),
#     path('add/', views.add_expense, name='add_expense'),
#     path('edit/<int:id>/', views.edit_expense, name='edit_expense'),
#     path('delete/<int:id>/', views.delete_expense, name='delete_expense'),
#     path('category-summary/', views.expense_category_summary, name='expense_category_summary'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.expense_list, name='expenses'),
    path('add/', views.add_expense, name='add_expense'),
    path('edit/<int:id>/', views.edit_expense, name='edit_expense'),
    path('delete/<int:id>/', views.delete_expense, name='delete_expense'),
    path('category-summary/', views.expense_category_summary, name='expense_category_summary'),
    path('generate-report/', views.generate_report, name='generate_report'),
]


