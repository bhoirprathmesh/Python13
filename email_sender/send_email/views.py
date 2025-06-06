from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

# Create your views here.

def index(request):
    return render(request, 'index.html')

def send_email(request):
    if request.method == 'POST':
        sender_email = request.POST.get('sender')
        recipient_email = request.POST.get('recipient')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Sending the email
        try:
            send_mail(
                subject,
                message,
                sender_email,
                [recipient_email],
                fail_silently=False,
            )
            return HttpResponse('Email sent successfully!')
        except Exception as e:
            return HttpResponse(f'An error occurred: {e}')
    else:
        # Render the form template
        return render(request, 'email_form.html')