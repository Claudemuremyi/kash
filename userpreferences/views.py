# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages
# from .models import UserPreference
# import json
# import os
# from django.conf import settings

# @login_required
# def preferences(request):
#     user_preference, created = UserPreference.objects.get_or_create(user=request.user)
#     currencies = {}
    
#     file_path = os.path.join(settings.BASE_DIR, 'currencies.json')
#     try:
#         with open(file_path, 'r', encoding='utf-8') as file:
#             currencies = json.load(file)
#     except FileNotFoundError:
#         messages.error(request, "Currency file not found. Please contact the administrator.")
#         currencies = {"USD": "United States Dollar"}  # Fallback option
#     except json.JSONDecodeError:
#         messages.error(request, "Error parsing the currency file. Please contact the administrator.")
#         currencies = {"USD": "United States Dollar"}  # Fallback option
#     except Exception as e:
#         messages.error(request, f"An error occurred: {str(e)}. Please contact the administrator.")
#         currencies = {"USD": "United States Dollar"}  # Fallback option
    
#     if request.method == 'POST':
#         currency = request.POST['currency']
#         user_preference.currency = currency
#         user_preference.save()
#         messages.success(request, 'Preferences updated successfully')
#         return redirect('preferences')
        
#     context = {
#         'currencies': currencies,
#         'user_preference': user_preference
#     }
#     return render(request, 'userpreferences/preferences.html', context)

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserPreference
import json
import os
from django.conf import settings

@login_required
def preferences(request):
    user_preference, created = UserPreference.objects.get_or_create(user=request.user)
    currencies = {}
    
    file_path = os.path.join(settings.BASE_DIR, 'currencies.json')
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            currencies = json.load(file)
    except FileNotFoundError:
        messages.error(request, "Currency file not found. Please contact the administrator.")
        currencies = {"USD": "United States Dollar"}  # Fallback option
    except json.JSONDecodeError:
        messages.error(request, "Error parsing the currency file. Please contact the administrator.")
        currencies = {"USD": "United States Dollar"}  # Fallback option
    except Exception as e:
        messages.error(request, f"An error occurred: {str(e)}. Please contact the administrator.")
        currencies = {"USD": "United States Dollar"}  # Fallback option
    
    if request.method == 'POST':
        currency = request.POST['currency']
        user_preference.currency = currency
        user_preference.save()
        messages.success(request, 'Preferences updated successfully')
        return redirect('preferences')
        
    context = {
        'currencies': currencies,
        'user_preference': user_preference
    }
    return render(request, 'userpreferences/preferences.html', context)

