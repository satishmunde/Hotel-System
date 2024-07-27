from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse


def home(request):
    return render(request,'index.html')


# def email(request):
#     print('calling')

#     subject = 'Django Server Testing'
#     message = 'This is the testing mail'
#     recipient_email = 'mundesatish2002@gmail.com'

#     try:
#         send_mail(
#                 subject,
#                 message,
#                 'satishmh26@gmail.com',  # Replace with your sender email
#                 [recipient_email]
#         )
#         print('done')
#         return HttpResponse("Email sent successfully!")  # Return a success message
#     except Exception as e:
#         print({'error_message': str(e)})
#         return HttpResponse(f"Error sending email: {str(e)}") 


from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.conf import settings

def email(request):
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
