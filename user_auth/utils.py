import requests
from assignment.conf import OTP_LENGTH
from random import randint
from user_auth.models import OTPGenerator

from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import get_template


def generate_otp_number():
    range_start = 10 ** (OTP_LENGTH - 1)
    range_end = (10 ** OTP_LENGTH) - 1
    return randint(range_start, range_end)


def validate_otp_number(otp_no, otp_data):
    otp_obj = OTPGenerator.objects.filter(**{
        'otp_number': otp_no})
    if otp_obj.count() == 0:
        return otp_no
    else:
        otp_no = generate_otp_number()
        validate_otp_number(otp_no, otp_data)


def opt_generator(user):
    prev_otp_obj = OTPGenerator.objects.filter(
        **{'email': user.email})
    if prev_otp_obj.count() > 0:
        [obj.delete() for obj in prev_otp_obj]

    otp_no = generate_otp_number()
    validated_otp_num = validate_otp_number(
        otp_no, user.email)

    OTPGenerator.objects.create(
        otp_number=validated_otp_num,
        email=user.email, is_active=True)

    return validated_otp_num


def send_otp_to_mail(user_data, validated_otp_num, user):
    ## Sending Email to User
    subject = "Email - Verification"

    html_template = get_template('user_auth/registration_email.html')
    html_context = {}
    html_context['full_name'] = user_data.get('email')
    if user_data.get('full_name'):
        html_context['full_name'] = user_data.get('full_name')
    html_context['passcode'] = validated_otp_num
    html_content = html_template.render(html_context)

    email_to = user.email
    send_mail(subject, None, settings.EMAIL_HOST_USER, [
        email_to, ], html_message=html_content, fail_silently=False)
    ## Sending Email to User FInish


def generate_oauth_token(self, username, password):
    client_id = settings.CLIENT_ID
    client_secret = settings.CLIENT_SECRET

    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {'grant_type': 'password',
               'username': username,
               'password': password,
               'client_id': client_id,
               'client_secret': client_secret}

    host = self.request.get_host()
    return (requests.post(
        settings.SERVER_PROTOCOLS + host + "/o/token/",
        data=payload,
        headers=headers))
