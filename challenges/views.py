from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

monthly_challenges = {
    "january": "Eat no vegetables!",
    "february": "Exercise!",
    "march": "Do something in March",
    "april": "Nahh",
    "may": "Nahh",
    "june": "Nahh",
    "july": "Nahh",
    "august": "Nahh",
    "september": "Nahh",
    "october": "Nahh",
    "november": "Nahh",
    "december": "Nahh",
}

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    
    redirect_month = months[month - 1]
    redirect_path = reverse("monthly_challenge", args=[redirect_month]) # e.g. challenges/january
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound('This month is not supported')