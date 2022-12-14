from django.core.mail import send_mail


def send_confirmation_email(email, code):
    full_link = f'http://3.87.153.165//api/v1/accounts/activate/{code}/'
    send_mail(
        'Здравствуйте активируйте ваш аккаунт!',
        f'Чтобы активировать ваш аккаунт нужно перейти по ссылке: {full_link}',
        'bekkeldievsuiun18@gmail.com',
        [email],
        fail_silently=False)


def send_code_password_reset(user):
    code = user.activation_code
    email = user.email
    send_mail(
        'Письмо с кодом для сброса пароля!',
        f'Ваш код для того, чтобы восстановить пароль: {code}\nНикому не передавайте этот код!',
        'bekkeldievsuiun18@gmail.com',
        [email],
        fail_silently=False
    )
