from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def menu(request):
    user = request.session['user'] 

    return render(request, 'menu.html',{'user':user})
