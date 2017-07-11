import json

from django.http import HttpResponse
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from user_auth import system_error
from assignment import error_conf
from user_auth import utils
from user_auth.models import User
from user_auth.serializers import (
    UserSerializer
)


class CreateUserView(CreateAPIView):
    """
    Creating API for User creation which takes user
    details(email, password, confirm_password, first_name
    last_name, phone_number) as input validates the user details and
    creates a user account.
    """
    model = User
    serializer_class = UserSerializer

    def post(self, request):

        user_data = request.data

        error_checks = system_error.check_for_registration_input_error(user_data)
        if error_checks:
            return Response(error_checks,
                            status=status.HTTP_412_PRECONDITION_FAILED)

        user_data['role'] = "User"
        serializer = UserSerializer(data=user_data)

        if serializer.is_valid():
            user = serializer.save()

            """
            This generates the OTP for the registered email
            and send the OTP to the users email.
            """
            validated_otp_num = utils.opt_generator(user)

            utils.send_otp_to_mail(user_data, validated_otp_num, user)

            token = utils.generate_oauth_token(
                self, user.email,
                user_data.get('confirm_password'))

            if token.status_code != 200:
                return Response({'msg': 'Username or password is incorrect'},
                                status=status.HTTP_412_PRECONDITION_FAILED)

            return Response({
                'success': True,
                'msg': 'Registration Successfully Please Verify Email',
                'token': json.loads(token._content)})

        return Response(error_conf.GENERIC_API_FALIURE,
                        status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    """
    Creating API for User Authentication
    Based On roles and UserName and Passwords

    Note:-
    Checks whether the request is from audetemi user
    by checking the provider name in UserSocialDetails
    Table and if that entry is primary.
    """

    def post(self, request, format=None):
        """
        Return a Valid token if username and password
        is valid for a given client
        """

        if request.data:
            data = request.data

            error_checks = system_error.check_for_login_input_error(data)

            if (error_checks and error_checks.get('error_code') != 7):
                return Response(error_checks,
                                status=status.HTTP_412_PRECONDITION_FAILED)

            email = data.get('email')
            password = data.get('password')

            user = User.objects.get(email=email)
            username = user.username



            login_success_data = utils.generate_oauth_token(self, username, password)
            if login_success_data.status_code != 200:
                return Response(error_conf.INVALID_PASSWORD,
                                status=status.HTTP_412_PRECONDITION_FAILED)

            responce_dict = json.loads(login_success_data._content)

            if (error_checks and error_checks.get('error_code') == 7):
                responce_dict['is_email_verified'] = False
            else:
                responce_dict['is_email_verified'] = True

            return HttpResponse(json.dumps(responce_dict),
                                content_type='application/json')
        return HttpResponse(status=status.HTTP_412_PRECONDITION_FAILED)
