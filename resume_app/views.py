from django.shortcuts import render
# Module for sending mails
# from django.core.mail import send_mail
from .models import ContactMe
from django.http import HttpResponse

# Create your views here.
def index(request):
    if request.method == 'POST':
        contact=ContactMe()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact.name=name
        contact.email=email
        contact.subject=subject
        contact.message=message
        contact.save()
        return HttpResponse("<h1> THANKS FOR CONTACT US </H1>")


    #     data = {
    #         'name': name,
    #         'email': email,
    #         'subject':  subject,
    #         'message': message

    #     }

    #     message = '''
    #     New message: {}

    #     From: {}
    #     '''.format(data['message'], data['email'])
    #     send_mail(data['subject'], message, '', ['ogtconsult21@gmail.com'])
    
    # else:
    return render(request, 'index.html')
