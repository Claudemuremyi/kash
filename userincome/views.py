# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages
# from .models import UserIncome, Source
# from .forms import IncomeForm
# from django.core.paginator import Paginator
# from userpreferences.models import UserPreference
# from django.db.models import Sum
# from django.http import JsonResponse

# @login_required
# def income_list(request):
#     income = UserIncome.objects.filter(user=request.user)
#     paginator = Paginator(income, 10)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)

#     currency = UserPreference.objects.get(user=request.user).currency

#     context = {
#         'income': page_obj,
#         'currency': currency
#     }
#     return render(request, 'userincome/income_list.html', context)

# @login_required
# def add_income(request):
#     sources = Source.objects.filter(user=request.user)
#     if request.method == 'POST':
#         form = IncomeForm(request.POST)
#         if form.is_valid():
#             income = form.save(commit=False)
#             income.user = request.user
#             income.save()
#             messages.success(request, 'Income added successfully')
#             return redirect('income')
#     else:
#         form = IncomeForm()

#     context = {
#         'form': form,
#         'sources': sources
#     }
#     return render(request, 'userincome/add_income.html', context)

# @login_required
# def edit_income(request, id):
#     income = get_object_or_404(UserIncome, pk=id, user=request.user)
#     sources = Source.objects.filter(user=request.user)

#     if request.method == 'POST':
#         form = IncomeForm(request.POST, instance=income)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Income updated successfully')
#             return redirect('income')
#     else:
#         form = IncomeForm(instance=income)

#     context = {
#         'form': form,
#         'sources': sources,
#         'income': income
#     }
#     return render(request, 'userincome/edit_income.html', context)

# @login_required
# def delete_income(request, id):
#     income = get_object_or_404(UserIncome, pk=id, user=request.user)
#     if request.method == 'POST':
#         income.delete()
#         messages.success(request, 'Income deleted successfully')
#         return redirect('income')
#     return render(request, 'userincome/delete_income.html', {'income': income})

# @login_required
# def income_source_summary(request):
#     income = UserIncome.objects.filter(user=request.user)
#     source_summary = income.values('source__name').annotate(total=Sum('amount'))

#     return JsonResponse({
#         'source_summary': list(source_summary)
#     })



from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserIncome, Source, get_default_sources
from .forms import IncomeForm
from django.core.paginator import Paginator
from userpreferences.models import UserPreference
from django.db.models import Sum
from django.http import JsonResponse

# @login_required
# def income_list(request):
#     income = UserIncome.objects.filter(user=request.user)
#     paginator = Paginator(income, 10)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#
#     currency = UserPreference.objects.get(user=request.user).currency
#
#     context = {
#         'income': page_obj,
#         'currency': currency
#     }
#     return render(request, 'userincome/income_list.html', context)
#
# @login_required
# def add_income(request):
#     sources = Source.objects.filter(user=request.user)
#     if not sources:
#         for source_name in get_default_sources():
#             Source.objects.create(name=source_name, user=request.user)
#         sources = Source.objects.filter(user=request.user)
#
#     if request.method == 'POST':
#         form = IncomeForm(request.POST)
#         if form.is_valid():
#             income = form.save(commit=False)
#             income.user = request.user
#             income.save()
#             messages.success(request, 'Income added successfully')
#             return redirect('income')
#     else:
#         form = IncomeForm()
#
#     context = {
#         'form': form,
#         'sources': sources
#     }
#     return render(request, 'userincome/add_income.html', context)
#
# @login_required
# def edit_income(request, id):
#     income = get_object_or_404(UserIncome, pk=id, user=request.user)
#     sources = Source.objects.filter(user=request.user)
#
#     if request.method == 'POST':
#         form = IncomeForm(request.POST, instance=income)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Income updated successfully')
#             return redirect('income')
#     else:
#         form = IncomeForm(instance=income)
#
#     context = {
#         'form': form,
#         'sources': sources,
#         'income': income
#     }
#     return render(request, 'userincome/edit_income.html', context)
#
# @login_required
# def delete_income(request, id):
#     income = get_object_or_404(UserIncome, pk=id, user=request.user)
#     if request.method == 'POST':
#         income.delete()
#         messages.success(request, 'Income deleted successfully')
#         return redirect('income')
#     return render(request, 'userincome/delete_income.html', {'income': income})
#
# @login_required
# def income_source_summary(request):
#     income = UserIncome.objects.filter(user=request.user)
#     source_summary = income.values('source__name').annotate(total=Sum('amount'))
#
#     return JsonResponse({
#         'source_summary': list(source_summary)
#     })


# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages
# from .models import UserIncome, Source, get_default_sources
# from .forms import IncomeForm
# from django.core.paginator import Paginator
# from userpreferences.models import UserPreference
# from django.db.models import Sum
# from django.http import JsonResponse
# from django.db.models.functions import TruncMonth
#
#
# @login_required
# def income_list(request):
#     income = UserIncome.objects.filter(user=request.user)
#     paginator = Paginator(income, 10)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#
#     # Get monthly income for time series chart
#     monthly_income = UserIncome.objects.filter(user=request.user).annotate(
#         month=TruncMonth('date')
#     ).values('month').annotate(
#         total=Sum('amount')
#     ).order_by('month')
#
#     # Get source distribution
#     income_by_source = UserIncome.objects.filter(user=request.user).values(
#         'source__name'
#     ).annotate(
#         total=Sum('amount')
#     ).order_by('-total')
#
#     try:
#         currency = UserPreference.objects.get(user=request.user).currency
#     except UserPreference.DoesNotExist:
#         currency = 'USD'
#
#     context = {
#         'income': page_obj,
#         'currency': currency,
#         'dates': json.dumps([item['month'].strftime("%B %Y") for item in monthly_income]),
#         'amounts': json.dumps([float(item['total']) for item in monthly_income]),
#         'source_summary': list(income_by_source)
#     }
#     return render(request, 'userincome/income_list.html', context)
#
#
# @login_required
# def add_income(request):
#     sources = Source.objects.filter(user=request.user)
#     if not sources:
#         for source_name in get_default_sources():
#             Source.objects.create(name=source_name, user=request.user)
#         sources = Source.objects.filter(user=request.user)
#
#     if request.method == 'POST':
#         form = IncomeForm(request.POST)
#         if form.is_valid():
#             income = form.save(commit=False)
#             income.user = request.user
#             income.save()
#             messages.success(request, 'Income added successfully')
#             return redirect('income')
#     else:
#         form = IncomeForm()
#
#     context = {
#         'form': form,
#         'sources': sources
#     }
#     return render(request, 'userincome/add_income.html', context)
#
#
# @login_required
# def edit_income(request, id):
#     income = get_object_or_404(UserIncome, pk=id, user=request.user)
#     sources = Source.objects.filter(user=request.user)
#
#     if request.method == 'POST':
#         form = IncomeForm(request.POST, instance=income)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Income updated successfully')
#             return redirect('income')
#     else:
#         form = IncomeForm(instance=income)
#
#     context = {
#         'form': form,
#         'sources': sources,
#         'income': income
#     }
#     return render(request, 'userincome/edit_income.html', context)
#
#
# @login_required
# def delete_income(request, id):
#     income = get_object_or_404(UserIncome, pk=id, user=request.user)
#     if request.method == 'POST':
#         income.delete()
#         messages.success(request, 'Income deleted successfully')
#         return redirect('income')
#     return render(request, 'userincome/delete_income.html', {'income': income})
#
#
# @login_required
# def income_source_summary(request):
#     income = UserIncome.objects.filter(user=request.user)
#     monthly_income = income.annotate(
#         month=TruncMonth('date')
#     ).values('month').annotate(
#         total=Sum('amount')
#     ).order_by('month')
#
#     source_summary = income.values('source__name').annotate(total=Sum('amount'))
#
#     return JsonResponse({
#         'dates': [item['month'].strftime("%B %Y") for item in monthly_income],
#         'amounts': [float(item['total']) for item in monthly_income],
#         'source_summary': list(source_summary)
#     })


import json
from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserIncome, Source, get_default_sources
from .forms import IncomeForm
from django.core.paginator import Paginator
from userpreferences.models import UserPreference
from django.db.models import Sum
from django.http import JsonResponse
from django.db.models.functions import TruncMonth, TruncDate


@login_required
def income_list(request):
    """
    View to display list of income entries with charts
    """
    # Get all income entries for the current user
    income_entries = UserIncome.objects.filter(user=request.user).order_by('-date')

    # Setup pagination
    paginator = Paginator(income_entries, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Get monthly income data for charts
    monthly_income = UserIncome.objects.filter(user=request.user).annotate(
        month=TruncMonth('date')
    ).values('month').annotate(
        total=Sum('amount')
    ).order_by('month')

    # Get income distribution by source
    income_by_source = UserIncome.objects.filter(user=request.user).values(
        'source__name'
    ).annotate(
        total=Sum('amount')
    ).order_by('-total')

    # Get user's preferred currency
    try:
        currency = UserPreference.objects.get(user=request.user).currency
    except UserPreference.DoesNotExist:
        currency = 'USD'  # Default currency if preference not set

    # Calculate total income
    total_income = UserIncome.objects.filter(user=request.user).aggregate(
        total=Sum('amount'))['total'] or 0

    context = {
        'income_list': page_obj,
        'currency': currency,
        'total_income': total_income,
        'dates': json.dumps([item['month'].strftime("%B %Y") for item in monthly_income]),
        'amounts': json.dumps([float(item['total']) for item in monthly_income]),
        'source_summary': list(income_by_source)
    }
    return render(request, 'userincome/income_list.html', context)


@login_required
def add_income(request):
    """
    View to add new income entry
    """
    # Check for existing sources or create defaults
    sources = Source.objects.filter(user=request.user)
    if not sources:
        for source_name in get_default_sources():
            Source.objects.create(name=source_name, user=request.user)
        sources = Source.objects.filter(user=request.user)

    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            income = form.save(commit=False)
            income.user = request.user
            income.save()
            messages.success(request, 'Income added successfully')
            return redirect('income')
    else:
        form = IncomeForm()

    context = {
        'form': form,
        'sources': sources
    }
    return render(request, 'userincome/add_income.html', context)


@login_required
def edit_income(request, id):
    """
    View to edit existing income entry
    """
    income = get_object_or_404(UserIncome, pk=id, user=request.user)
    sources = Source.objects.filter(user=request.user)

    if request.method == 'POST':
        form = IncomeForm(request.POST, instance=income)
        if form.is_valid():
            form.save()
            messages.success(request, 'Income updated successfully')
            return redirect('income')
    else:
        form = IncomeForm(instance=income)

    context = {
        'form': form,
        'sources': sources,
        'income': income
    }
    return render(request, 'userincome/edit_income.html', context)


@login_required
def delete_income(request, id):
    """
    View to delete income entry
    """
    income = get_object_or_404(UserIncome, pk=id, user=request.user)
    if request.method == 'POST':
        income.delete()
        messages.success(request, 'Income deleted successfully')
        return redirect('income')
    return render(request, 'userincome/delete_income.html', {'income': income})

@login_required
def income_source_summary(request):
    """
    API view to get income summary data for charts
    """
    try:
        # Get income data for the current user
        income = UserIncome.objects.filter(user=request.user)

        # Get monthly aggregated data
        monthly_income = income.annotate(
            month=TruncMonth('date')
        ).values('month').annotate(
            total=Sum('amount')
        ).order_by('month')

        # Get source distribution
        source_summary = income.values('source__name').annotate(
            total=Sum('amount')
        ).order_by('-total')

        # Prepare the response data
        response_data = {
            'success': True,
            'dates': [item['month'].strftime("%B %Y") for item in monthly_income],
            'amounts': [float(item['total']) for item in monthly_income],
            'source_summary': [
                {
                    'name': item['source__name'],
                    'amount': float(item['total'])
                }
                for item in source_summary
            ]
        }

        return JsonResponse(response_data)
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        })

@login_required
def add_income_source(request):
    """
    View to add new income source
    """
    if request.method == 'POST':
        source_name = request.POST.get('name')
        if source_name:
            Source.objects.create(name=source_name, user=request.user)
            messages.success(request, 'Income source added successfully')
        else:
            messages.error(request, 'Source name is required')
        return redirect('income')
    return render(request, 'userincome/add_source.html')


@login_required
def delete_income_source(request, id):
    """
    View to delete income source
    """
    source = get_object_or_404(Source, pk=id, user=request.user)
    if request.method == 'POST':
        if UserIncome.objects.filter(source=source).exists():
            messages.error(request, 'Cannot delete source with associated income entries')
        else:
            source.delete()
            messages.success(request, 'Income source deleted successfully')
        return redirect('income')
    return render(request, 'userincome/delete_source.html', {'source': source})



