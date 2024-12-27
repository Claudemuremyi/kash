# from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
# from django.db.models import Sum
# from django.db.models.functions import TruncMonth
# from expenses.models import Expense
# from userincome.models import UserIncome
# import json
#
# @login_required
# def dashboard(request):
#     # Get monthly expenses
#     monthly_expenses = Expense.objects.filter(user=request.user).annotate(
#         month=TruncMonth('date')
#     ).values('month').annotate(
#         total=Sum('amount')
#     ).order_by('month')
#
#     # Get monthly income
#     monthly_income = UserIncome.objects.filter(user=request.user).annotate(
#         month=TruncMonth('date')
#     ).values('month').annotate(
#         total=Sum('amount')
#     ).order_by('month')
#
#     # Get category distributions
#     expense_by_category = Expense.objects.filter(user=request.user).values(
#         'category__name'
#     ).annotate(
#         total=Sum('amount')
#     ).order_by('-total')
#
#     income_by_source = UserIncome.objects.filter(user=request.user).values(
#         'source__name'
#     ).annotate(
#         total=Sum('amount')
#     ).order_by('-total')
#
#     # Calculate totals
#     total_income = sum(item['total'] for item in income_by_source)
#     total_expenses = sum(item['total'] for item in expense_by_category)
#     net_balance = total_income - total_expenses
#
#     context = {
#         'monthly_expenses': json.dumps([{
#             'month': item['month'].strftime("%B %Y"),
#             'total': float(item['total'])
#         } for item in monthly_expenses]),
#         'monthly_income': json.dumps([{
#             'month': item['month'].strftime("%B %Y"),
#             'total': float(item['total'])
#         } for item in monthly_income]),
#         'expense_categories': json.dumps([{
#             'category': item['category__name'],
#             'total': float(item['total'])
#         } for item in expense_by_category]),
#         'income_sources': json.dumps([{
#             'source': item['source__name'],
#             'total': float(item['total'])
#         } for item in income_by_source]),
#         'total_income': total_income,
#         'total_expenses': total_expenses,
#         'net_balance': net_balance
#     }
#     return render(request, 'dashboard.html', context)
#


from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.db.models.functions import TruncMonth
from expenses.models import Expense
from userincome.models import UserIncome
import json

def home(request):
    """
    View for the home page
    """
    return render(request, 'home.html')

@login_required
def dashboard(request):
    """
    View for the dashboard page showing financial statistics
    """
    # Get monthly expenses
    monthly_expenses = Expense.objects.filter(user=request.user).annotate(
        month=TruncMonth('date')
    ).values('month').annotate(
        total=Sum('amount')
    ).order_by('month')

    # Get monthly income
    monthly_income = UserIncome.objects.filter(user=request.user).annotate(
        month=TruncMonth('date')
    ).values('month').annotate(
        total=Sum('amount')
    ).order_by('month')

    # Get category distributions
    expense_by_category = Expense.objects.filter(user=request.user).values(
        'category__name'
    ).annotate(
        total=Sum('amount')
    ).order_by('-total')

    income_by_source = UserIncome.objects.filter(user=request.user).values(
        'source__name'
    ).annotate(
        total=Sum('amount')
    ).order_by('-total')

    # Calculate totals
    total_income = UserIncome.objects.filter(user=request.user).aggregate(
        total=Sum('amount'))['total'] or 0
    total_expenses = Expense.objects.filter(user=request.user).aggregate(
        total=Sum('amount'))['total'] or 0
    net_balance = total_income - total_expenses

    context = {
        'monthly_expenses': json.dumps([{
            'month': item['month'].strftime("%B %Y"),
            'total': float(item['total'])
        } for item in monthly_expenses]),
        'monthly_income': json.dumps([{
            'month': item['month'].strftime("%B %Y"),
            'total': float(item['total'])
        } for item in monthly_income]),
        'expense_categories': json.dumps([{
            'category': item['category__name'],
            'total': float(item['total'])
        } for item in expense_by_category]),
        'income_sources': json.dumps([{
            'source': item['source__name'],
            'total': float(item['total'])
        } for item in income_by_source]),
        'total_income': total_income,
        'total_expenses': total_expenses,
        'net_balance': net_balance
    }
    return render(request, 'dashboard.html', context)

