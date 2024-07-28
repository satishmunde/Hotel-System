from django.shortcuts import render,redirect
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.conf import settings
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth import authenticate
from rest_framework import status
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from django.contrib.auth import authenticate, login as auth_login

# from django.contrib.auth.forms import PasswordResetForm
# from django.contrib.auth.tokens import default_token_generator
# from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# from django.template.loader import render_to_string
# from django.core.mail import send_mail
# from django.conf import settings
# from django.http import HttpResponse
# from django.shortcuts import render
# from django.utils.encoding import force_bytes, force_text

@login_required
def home(request):
    return render(request, 'index.html')




def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            # Log in the user
            auth_login(request, user)
            refresh = RefreshToken.for_user(user)
            data = {
                'access': str(refresh.access_token),
                'refresh': str(refresh),
            }
            print(data)
            # return Response(data, status=status.HTTP_200_OK)
            request.session['access_token'] = str(refresh.access_token)
            request.session['refresh_token'] = str(refresh)
            request.session['success_message'] = 'Login successful!'


            # next_url = request.GET.get('next', '')
            return redirect('/')
        else:
            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')




def forget_password(request):
    pass
    # if request.method == 'POST':
    #     form = PasswordResetForm(request.POST)
    #     if form.is_valid():
    #         email = form.cleaned_data['email']
    #         users = User.objects.filter(email=email)
    #         for user in users:
    #             subject = "Password Reset Requested"
    #             email_template_name = "password_reset_email.html"
    #             c = {
    #                 "email": user.email,
    #                 "domain": request.META['HTTP_HOST'],
    #                 "site_name": "Your Site",
    #                 "uid": urlsafe_base64_encode(force_bytes(user.pk)),
    #                 "user": user,
    #                 "token": default_token_generator.make_token(user),
    #                 "protocol": request.scheme,
    #             }
    #             email_body = render_to_string(email_template_name, c)
    #             send_mail(subject, email_body, settings.DEFAULT_FROM_EMAIL, [user.email], fail_silently=False)
    #         return HttpResponse("Password reset email sent")
    # else:
    #     form = PasswordResetForm()
    # return render(request, 'forget_password.html', {'form': form})



def email():
    print('calling')

    subject = 'Django Server Testing'
    message = 'This is the testing mail'
    recipient_email = 'mundesatish2002@gmail.com'

    # Render email templates
    context = {'subject': subject, 'message': message}
    html_message = render_to_string('email_template.html', context)


    try:
        email = EmailMultiAlternatives(
            subject,
            html_message,  # Plain text version of the email
            settings.EMAIL_HOST_USER,  # From email
            [recipient_email]  # To email
        )
        email.attach_alternative(html_message, "text/html")  # Attach HTML version of the email
        email.send()
        print('done')
        return HttpResponse("Email sent successfully!")  # Return a success message
    except Exception as e:
        print({'error_message': str(e)})
        return HttpResponse(f"Error sending email: {str(e)}")
