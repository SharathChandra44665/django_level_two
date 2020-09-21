from django.shortcuts import render
from ex_app.models import UserAccount

# Create your views here.
def get_home_page(arg):
    return render(arg,"pages/home.html",)

def get_all_user_page(arg):
    user_list=UserAccount.objects.order_by('first_name')
    myusers={'all_user':user_list}
    return render(arg,'pages/allusers.html',myusers)
