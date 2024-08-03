from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def employee(request):
    user = request.session['user'] 
    
    
    return render(request, 'employee.html',{'user':user})
