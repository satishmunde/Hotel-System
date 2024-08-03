from django.shortcuts import render
from django.contrib.auth.decorators import login_required



@login_required
def erp(request):
    user = request.session['user'] 
    
    return render(request, 'erp.html',{'user':user})
