# # from django.shortcuts import render, redirect, get_object_or_404
# # from django.contrib.auth.decorators import login_required
# # from django.contrib import messages
# # from .models import Category, Expense
# # from .forms import ExpenseForm
# # from django.core.paginator import Paginator
# # from django.db.models import Sum
# # from userpreferences.models import UserPreference
# # import json
# # from django.http import JsonResponse

# # @login_required
# # def expense_list(request):
# #     expenses = Expense.objects.filter(user=request.user)
# #     paginator = Paginator(expenses, 10)
# #     page_number = request.GET.get('page')
# #     page_obj = paginator.get_page(page_number)
    
# #     currency = UserPreference.objects.get(user=request.user).currency
    
# #     context = {
# #         'expenses': page_obj,
# #         'currency': currency
# #     }
# #     return render(request, 'expenses/expense_list.html')

# # @login_required
# # def add_expense(request):
# #     categories = Category.objects.filter(user=request.user)
# #     if request.method == 'POST':
# #         form = ExpenseForm(request.POST)
# #         if form.is_valid():
# #             expense = form.save(commit=False)
# #             expense.user = request.user
# #             expense.save()
# #             messages.success(request, 'Expense added successfully')
# #             return redirect('expenses')
# #     else:
# #         form = ExpenseForm()
    
# #     context = {
# #         'form': form,
# #         'categories': categories
# #     }
# #     return render(request, 'expenses/add_expense.html', context)

# # @login_required
# # def edit_expense(request, id):
# #     expense = get_object_or_404(Expense, pk=id, user=request.user)
# #     categories = Category.objects.filter(user=request.user)
    
# #     if request.method == 'POST':
# #         form = ExpenseForm(request.POST, instance=expense)
# #         if form.is_valid():
# #             form.save()
# #             messages.success(request, 'Expense updated successfully')
# #             return redirect('expenses')
# #     else:
# #         form = ExpenseForm(instance=expense)
    
# #     context = {
# #         'form': form,
# #         'categories': categories,
# #         'expense': expense
# #     }
# #     return render(request, 'expenses/edit_expense.html', context)

# # @login_required
# # def delete_expense(request, id):
# #     expense = get_object_or_404(Expense, pk=id, user=request.user)
# #     if request.method == 'POST':
# #         expense.delete()
# #         messages.success(request, 'Expense deleted successfully')
# #         return redirect('expenses')
# #     return render(request, 'expenses/delete_expense.html', {'expense': expense})

# # @login_required
# # def expense_category_summary(request):
# #     expenses = Expense.objects.filter(user=request.user)
# #     category_summary = expenses.values('category__name').annotate(total=Sum('amount'))
    
# #     return JsonResponse({
# #         'category_summary': list(category_summary)
# #     })



# # from django.shortcuts import render, redirect, get_object_or_404
# # from django.contrib.auth.decorators import login_required
# # from django.contrib import messages
# # from .models import Category, Expense, get_default_categories
# # from .forms import ExpenseForm
# # from django.core.paginator import Paginator
# # from django.db.models import Sum
# # from userpreferences.models import UserPreference
# # import json
# # from django.http import JsonResponse

# # @login_required
# # def expense_list(request):
# #     expenses = Expense.objects.filter(user=request.user)
# #     paginator = Paginator(expenses, 10)
# #     page_number = request.GET.get('page')
# #     page_obj = paginator.get_page(page_number)
    
# #     currency = UserPreference.objects.get(user=request.user).currency
    
# #     context = {
# #         'expenses': page_obj,
# #         'currency': currency
# #     }
# #     return render(request, 'expenses/expense_list.html', context)

# # @login_required
# # def add_expense(request):
# #     categories = Category.objects.filter(user=request.user)
# #     if not categories:
# #         for category_name in get_default_categories():
# #             Category.objects.create(name=category_name, user=request.user)
# #         categories = Category.objects.filter(user=request.user)
    
# #     if request.method == 'POST':
# #         form = ExpenseForm(request.POST)
# #         if form.is_valid():
# #             expense = form.save(commit=False)
# #             expense.user = request.user
# #             expense.save()
# #             messages.success(request, 'Expense added successfully')
# #             return redirect('expenses')
# #     else:
# #         form = ExpenseForm()
    
# #     context = {
# #         'form': form,
# #         'categories': categories
# #     }
# #     return render(request, 'expenses/add_expense.html', context)

# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages
# from .models import Category, Expense, get_default_categories
# from .forms import ExpenseForm
# from django.core.paginator import Paginator
# from django.db.models import Sum
# from userpreferences.models import UserPreference
# import json
# from django.http import JsonResponse

# @login_required
# def expense_list(request):
#     expenses = Expense.objects.filter(user=request.user)
#     paginator = Paginator(expenses, 10)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
    
#     currency = UserPreference.objects.get(user=request.user).currency
    
#     context = {
#         'expenses': page_obj,
#         'currency': currency
#     }
#     return render(request, 'expenses/expense_list.html', context)

# @login_required
# def add_expense(request):
#     categories = Category.objects.filter(user=request.user)
#     if not categories:
#         for category_name in get_default_categories():
#             Category.objects.create(name=category_name, user=request.user)
#         categories = Category.objects.filter(user=request.user)
    
#     if request.method == 'POST':
#         form = ExpenseForm(request.POST)
#         if form.is_valid():
#             expense = form.save(commit=False)
#             expense.user = request.user
#             expense.save()
#             messages.success(request, 'Expense added successfully')
#             return redirect('expenses')
#     else:
#         form = ExpenseForm()
    
#     context = {
#         'form': form,
#         'categories': categories
#     }
#     return render(request, 'expenses/add_expense.html', context)

# @login_required
# def edit_expense(request, id):
#     expense = get_object_or_404(Expense, pk=id, user=request.user)
#     categories = Category.objects.filter(user=request.user)
    
#     if request.method == 'POST':
#         form = ExpenseForm(request.POST, instance=expense)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Expense updated successfully')
#             return redirect('expenses')
#     else:
#         form = ExpenseForm(instance=expense)
    
#     context = {
#         'form': form,
#         'categories': categories,
#         'expense': expense
#     }
#     return render(request, 'expenses/edit_expense.html', context)

# @login_required
# def delete_expense(request, id):
#     expense = get_object_or_404(Expense, pk=id, user=request.user)
#     if request.method == 'POST':
#         expense.delete()
#         messages.success(request, 'Expense deleted successfully')
#         return redirect('expenses')
#     return render(request, 'expenses/delete_expense.html', {'expense': expense})

# @login_required
# def expense_category_summary(request):
#     expenses = Expense.objects.filter(user=request.user)
#     category_summary = expenses.values('category__name').annotate(total=Sum('amount'))
    
#     return JsonResponse({
#         'category_summary': list(category_summary)
#     })


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Category, Expense, get_default_categories
from .forms import ExpenseForm
from django.core.paginator import Paginator
from django.db.models import Sum
from userpreferences.models import UserPreference
import json
from django.http import JsonResponse
from .utils import export_expense_report_csv
from django.utils.dateparse import parse_date

# @login_required
# def expense_list(request):
#     expenses = Expense.objects.filter(user=request.user)
#     paginator = Paginator(expenses, 10)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#
#     currency = UserPreference.objects.get(user=request.user).currency
#
#     context = {
#         'expenses': page_obj,
#         'currency': currency
#     }
#     return render(request, 'expenses/expense_list.html', context)
#
# @login_required
# def add_expense(request):
#     categories = Category.objects.filter(user=request.user)
#     if not categories:
#         for category_name in get_default_categories():
#             Category.objects.create(name=category_name, user=request.user)
#         categories = Category.objects.filter(user=request.user)
#
#     if request.method == 'POST':
#         form = ExpenseForm(request.POST)
#         if form.is_valid():
#             expense = form.save(commit=False)
#             expense.user = request.user
#             expense.save()
#             messages.success(request, 'Expense added successfully')
#             return redirect('expenses')
#     else:
#         form = ExpenseForm()
#
#     context = {
#         'form': form,
#         'categories': categories
#     }
#     return render(request, 'expenses/add_expense.html', context)
#
# @login_required
# def edit_expense(request, id):
#     expense = get_object_or_404(Expense, pk=id, user=request.user)
#     categories = Category.objects.filter(user=request.user)
#
#     if request.method == 'POST':
#         form = ExpenseForm(request.POST, instance=expense)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Expense updated successfully')
#             return redirect('expenses')
#     else:
#         form = ExpenseForm(instance=expense)
#
#     context = {
#         'form': form,
#         'categories': categories,
#         'expense': expense
#     }
#     return render(request, 'expenses/edit_expense.html', context)
#
# @login_required
# def delete_expense(request, id):
#     expense = get_object_or_404(Expense, pk=id, user=request.user)
#     if request.method == 'POST':
#         expense.delete()
#         messages.success(request, 'Expense deleted successfully')
#         return redirect('expenses')
#     return render(request, 'expenses/delete_expense.html', {'expense': expense})
#
# @login_required
# def expense_category_summary(request):
#     expenses = Expense.objects.filter(user=request.user)
#     category_summary = expenses.values('category__name').annotate(total=Sum('amount'))
#
#     return JsonResponse({
#         'category_summary': list(category_summary)
#     })
#
# @login_required
# def generate_report(request):
#     if request.method == 'POST':
#         start_date = parse_date(request.POST.get('start_date'))
#         end_date = parse_date(request.POST.get('end_date'))
#
#         if start_date and end_date:
#             return export_expense_report_csv(request.user, start_date, end_date)
#
#     return render(request, 'expenses/generate_report.html')


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Category, Expense, get_default_categories
from .forms import ExpenseForm
from django.core.paginator import Paginator
from django.db.models import Sum
from userpreferences.models import UserPreference
import json
from django.http import JsonResponse
from .utils import export_expense_report_csv
from django.utils.dateparse import parse_date
from django.db.models.functions import TruncMonth


@login_required
def expense_list(request):
    expenses = Expense.objects.filter(user=request.user)
    paginator = Paginator(expenses, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Get monthly expenses for time series chart
    monthly_expenses = Expense.objects.filter(user=request.user).annotate(
        month=TruncMonth('date')
    ).values('month').annotate(
        total=Sum('amount')
    ).order_by('month')

    # Get category distribution
    expense_by_category = Expense.objects.filter(user=request.user).values(
        'category__name'
    ).annotate(
        total=Sum('amount')
    ).order_by('-total')

    try:
        currency = UserPreference.objects.get(user=request.user).currency
    except UserPreference.DoesNotExist:
        currency = 'USD'

    context = {
        'expenses': page_obj,
        'currency': currency,
        'dates': json.dumps([item['month'].strftime("%B %Y") for item in monthly_expenses]),
        'amounts': json.dumps([float(item['total']) for item in monthly_expenses]),
        'category_summary': list(expense_by_category)
    }
    return render(request, 'expenses/expense_list.html', context)


@login_required
def add_expense(request):
    categories = Category.objects.filter(user=request.user)
    if not categories:
        for category_name in get_default_categories():
            Category.objects.create(name=category_name, user=request.user)
        categories = Category.objects.filter(user=request.user)

    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            messages.success(request, 'Expense added successfully')
            return redirect('expenses')
    else:
        form = ExpenseForm()

    context = {
        'form': form,
        'categories': categories
    }
    return render(request, 'expenses/add_expense.html', context)


@login_required
def edit_expense(request, id):
    expense = get_object_or_404(Expense, pk=id, user=request.user)
    categories = Category.objects.filter(user=request.user)

    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            messages.success(request, 'Expense updated successfully')
            return redirect('expenses')
    else:
        form = ExpenseForm(instance=expense)

    context = {
        'form': form,
        'categories': categories,
        'expense': expense
    }
    return render(request, 'expenses/edit_expense.html', context)


@login_required
def delete_expense(request, id):
    expense = get_object_or_404(Expense, pk=id, user=request.user)
    if request.method == 'POST':
        expense.delete()
        messages.success(request, 'Expense deleted successfully')
        return redirect('expenses')
    return render(request, 'expenses/delete_expense.html', {'expense': expense})


@login_required
def expense_category_summary(request):
    expenses = Expense.objects.filter(user=request.user)
    monthly_expenses = expenses.annotate(
        month=TruncMonth('date')
    ).values('month').annotate(
        total=Sum('amount')
    ).order_by('month')

    category_summary = expenses.values('category__name').annotate(total=Sum('amount'))

    return JsonResponse({
        'dates': [item['month'].strftime("%B %Y") for item in monthly_expenses],
        'amounts': [float(item['total']) for item in monthly_expenses],
        'category_summary': list(category_summary)
    })


@login_required
def generate_report(request):
    if request.method == 'POST':
        start_date = parse_date(request.POST.get('start_date'))
        end_date = parse_date(request.POST.get('end_date'))

        if start_date and end_date:
            return export_expense_report_csv(request.user, start_date, end_date)

    return render(request, 'expenses/generate_report.html')


