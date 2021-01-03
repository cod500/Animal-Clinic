from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.


def home(request):
    return render(request, 'home.html', {})


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        my_email = 'baledodge@mail.com'
        email = request.POST['email']
        message = request.POST['message']

        # send email
        send_mail(
            f'Message from {name}',
            message,
            my_email,
            [email],
        )

        return render(request, 'contact.html', {'name': name})
    else:
        return render(request, 'contact.html', {})


def about(request):
    return render(request, 'about.html', {})


def services(request):
    return render(request, 'services.html', {})


def appointment(request):
    return render(request, 'appointment.html', {})


def success(request):
    if request.method == "POST":
        my_email = 'baledodge@mail.com'
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        service = request.POST['service']
        doctor = request.POST['doctor']
        date = request.POST['date']

        # send email
        send_mail(
            f'Appointment for {name}',
            f'An appointment has been set for {name} at {date} with {doctor} for {service}. Our office will contact you at {phone} to confirm',
            my_email,
            [email],
        )

        return render(request, 'success.html', {
            'name': name,
            'email': email,
            'phone': phone,
            'service': service,
            'doctor': doctor,
            'date': date,
        })
    else:
        return render(request, 'home.html', {})


def subscribe(request):
    if request.method == "POST":
        my_email = 'baledodge@mail.com'
        email = request.POST['email']

        # send email
        send_mail(
            f'Newsletter Subcription',
            f'You are now subscribed to the COD PETS newsletter',
            my_email,
            [email],
        )

        return render(request, 'subscribe.html', {
            'email': email,
        })
    else:
        return render(request, 'home.html', {})
