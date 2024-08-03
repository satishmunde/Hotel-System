from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def inventory(request):
    user = request.session['user'] 
    return render(request, 'inventory.html' ,{'user':user})
