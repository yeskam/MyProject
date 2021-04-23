from django.core.mail import send_mail


def send_activation_code(email, activation_code):
    activation_url = f'http://localhost:8000/v1/api/account/activate/{activation_code}/'
    message = f"""Please, Activate Account. Here is the link:{activation_url}"""
    send_mail(
        'Activation Code',
        message,
        'test@test.com',
        [email, ],
        fail_silently=False
    )


