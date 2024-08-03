from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def order(request):
    user = request.session['user'] 
    return render(request, 'order.html' ,{'user':user})
