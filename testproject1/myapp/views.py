from django.shortcuts import render

# Create your views here.
def get_home_page(arg):

    udict={'username':'Sharathchandra'}
    return render(arg,'landingPage/index.html',udict)
