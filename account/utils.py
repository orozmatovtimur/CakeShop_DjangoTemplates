from django.core.mail import send_mail

def send_welcome_email(email):
    url = 'http://localhost:8000/'
    message = f'You have succesfully registered on Cake Shop!: {url}'
    send_mail(
        'Pyshop 12 Welcome!!!',
        message,
        'pyshopadmin@gmail.com',
        [email,],
        fail_silently=False
    )