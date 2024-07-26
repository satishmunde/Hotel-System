from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model

class EmployeeIDBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        User = get_user_model()
        
        print('backend get called')
        print(username)
        try:
            user = User.objects.get(emp_id=username)
            if user.check_password(password):
                print(user)
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        User = get_user_model()
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
