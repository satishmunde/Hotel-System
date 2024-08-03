from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def token(request):
    user = request.session['user'] 
    return render(request, 'token.html' ,{'user':user})
