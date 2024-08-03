from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def billing(request):
    user = request.session['user'] 
    return render(request, 'billing.html' ,{'user':user})
