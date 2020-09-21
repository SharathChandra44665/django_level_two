from django.shortcuts import render
from myapp.models import Person

# Create your views here.
def get_user_name(arg):
    # myd={}
    all_persons_list=Person.objects.order_by('first_name')
    all_val={'username':'Sharathchandra','all_persons':all_persons_list}
    return render(arg,'home/home.html',all_val)
