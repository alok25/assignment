from validate_email import validate_email

from assignment import error_conf
from user_auth import utils
from user_auth.models import User


def check_for_login_input_error(data):
    ###
    ## Error Handling For Login API
    ###

    if not data.get('email'):
        return error_conf.EMAIL_NOT_PROVIDED

    elif not data.get('password'):
        return error_conf.PASSWORD_NOT_PROVIDED

    if data.get('email'):
        email_valid = validate_email(data.get('email'))
        if not email_valid:
            return error_conf.INVALID_EMAIL

    if len(User.objects.filter(email=data.get('email'))) == 0:
        return error_conf.USER_DOES_NOT_EXIST
    return False


def check_for_registration_input_error(data):
    ###
    ## Error Handling For Registration API
    ###

    if not data.get('email'):
        return error_conf.EMAIL_NOT_PROVIDED

    elif not data.get('password'):
        return error_conf.PASSWORD_NOT_PROVIDED

    elif not data.get('confirm_password'):
        return error_conf.CONFIRM_PASSWORD_NOT_PROVIDED

    if data.get('email'):
        email_valid = validate_email(data.get('email'))
        if not email_valid:
            return error_conf.INVALID_EMAIL

    if data.get('password'):
        if len(data.get('password')) < 8:
            return error_conf.INSUFFICIENT_PASSWORD_LENGTH

    if (data.get('password') != data.get('confirm_password')):
        return error_conf.PASSWORDS_DOES_NOT_MATCH

    return False


def check_audetemi_created_user(user_obj):
    filtering_kwargs = {
        "provider": "Audetemi",
        "provider_id": user_obj.id,
        "user": user_obj,
        "is_primary": True
    }
    if len(UserSocialDetails.objects.filter(**filtering_kwargs)):
        return True


def check_for_update_password_input_error(request):
    data = request.data

    if not data.get('old_password'):
        return error_conf.OLD_PASSWORD_NOT_PROVIDED

    elif not data.get('new_password'):
        return error_conf.PASSWORD_NOT_PROVIDED

    elif not data.get('confirm_new_password'):
        return error_conf.CONFIRM_PASSWORD_NOT_PROVIDED

    if data.get('new_password'):
        if len(data.get('new_password')) < 8:
            return error_conf.INSUFFICIENT_PASSWORD_LENGTH

    if (data.get('new_password') != data.get('confirm_new_password')):
        return error_conf.PASSWORDS_DOES_NOT_MATCH

    user_obj = request.user

    if user_obj.check_password(data.get('old_password')):
        return error_conf.OLD_PASSWORD_INCORRECT

    audetemi_login = check_audetemi_created_user(user_obj)
    if not audetemi_login:
        return error_conf.USER_CREATED_THROUGH_SOCIAL_LOGIN

    return False


def check_for_forgot_password_input_error(request):
    data = request.data

    if not data.get('email'):
        return error_conf.EMAIL_NOT_PROVIDED

    user_obj = User.objects.filter(email=data.get('email'), is_active=True)

    if not user_obj:
        return error_conf.USER_DOES_NOT_EXIST

    audetemi_login = check_audetemi_created_user(user_obj[0])
    if not audetemi_login:
        return error_conf.USER_CREATED_THROUGH_SOCIAL_LOGIN


def check_for_social_registration_input_error(data):
    ###
    ## Error Handling For Registration API
    ###
    user_data = data.get('user_data', None)
    user_social_data = data.get('social_details', None)

    if not user_data or not user_social_data:
        return error_conf.NO_INPUT_DATA

    elif not user_social_data.get('access_token'):
        return error_conf.ACCESS_TOKEN_NOT_PROVIDED

    elif not user_social_data.get('provider'):
        return error_conf.PROVIDER_NOT_PROVIDED

    elif not user_social_data.get('provider_id'):
        return error_conf.PROVIDER_ID_NOT_PROVIDED

    elif not user_data.get('email'):
        return error_conf.EMAIL_NOT_PROVIDED

    elif not user_data.get('first_name'):
        return error_conf.FULLNAME_NOT_PROVIDED

    elif not data.get('source'):
        return error_conf.SOURCE_NOT_PROVIDED

    elif data.get('source') != "USER_APP":
        return error_conf.INVALID_SOURCE_PROVIDED

    if user_data.get('email'):
        email_valid = validate_email(user_data.get('email'))
        if not email_valid:
            return error_conf.INVALID_EMAIL

    return False
