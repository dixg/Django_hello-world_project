from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def index(reqest):
    today = datetime.datetime.now()
    return render(reqest, "birthday/index.html",
    {"birthday": today.day == 25 and today.month == 9
    })