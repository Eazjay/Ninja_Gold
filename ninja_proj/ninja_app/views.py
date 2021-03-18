from django.shortcuts import render, redirect
import random
from datetime import datetime

def index(request):
    if 'total_gold' not in request.session or 'activities' not in request.session:
        request.session['total_gold'] = 0
        request.session['activities'] = []
    return render(request, 'ninja.html')

def process_money(request):
    if request.method == "POST":
        if request.POST['building'] == 'farm':
            gold = random.randint(10, 20)
            request.session['activities'].append(f"You earned {str(gold)} golds from the {request.POST['building']} ({str(datetime.now().strftime('%Y/%m/%d, %I:%M %p, %a'))})")
        elif request.POST['building'] == 'cave':
            gold = random.randint(5, 10)
            request.session['activities'].append(f"You earned {str(gold)} golds from the {request.POST['building']} ({str(datetime.now().strftime('%Y/%m/%d, %I:%M %p, %a'))})")
        elif request.POST['building'] == 'house':
            gold = random.randint(2, 5)
            request.session['activities'].append(f"You earned {str(gold)} golds from the {request.POST['building']} ({str(datetime.now().strftime('%Y/%m/%d, %I:%M %p, %a'))})")
        elif request.POST['building'] == 'casino':
            gold = random.randint(-50, 50)
            if gold > 0:
                request.session['activities'].append(f"Entered a casino and earned {str(gold)} golds ({str(datetime.now().strftime('%Y/%m/%d, %I:%M %p, %a'))})")
            elif gold < 0:
                request.session['activities'].append(f"Entered a casino and lost {abs(gold)} golds ({str(datetime.now().strftime('%Y/%m/%d, %I:%M %p, %a'))})")
        request.session['total_gold'] += gold
    return redirect('/')

def reset(request):
    if request.method == "POST":
        request.session['total_gold'] = 0
        request.session['activities'] = []
    return redirect('/')