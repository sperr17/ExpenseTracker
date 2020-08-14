from django.urls import path

from . import views


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('expenses/', views.expenses, name='expenses'),
    path('expense-chart/', views.expense_chart, name='expense-chart')
]


