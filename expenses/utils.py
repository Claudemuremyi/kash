from django.db.models import Sum
from django.utils import timezone
from .models import Expense
import csv
from django.http import HttpResponse

def generate_expense_report(user, start_date, end_date):
    expenses = Expense.objects.filter(
        user=user,
        date__range=[start_date, end_date]
    ).values('category__name').annotate(total=Sum('amount'))
    
    return expenses

def export_expense_report_csv(user, start_date, end_date):
    expenses = generate_expense_report(user, start_date, end_date)
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="expense_report_{start_date}_{end_date}.csv"'
    
    writer = csv.writer(response)
    writer.writerow(['Category', 'Total Amount'])
    
    for expense in expenses:
        writer.writerow([expense['category__name'], expense['total']])
    
    return response

