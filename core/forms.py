from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class signupform(UserCreationForm):
    class meta:
        model =User
        fields =['username','first_name',"last_name","email"]


