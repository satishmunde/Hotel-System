from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def id_generator(request):
    user = request.session['user'] 
    return render(request, 'id_generator.html' ,{'user':user})
