from django.shortcuts import render

# Create your views here.
def get_username(request):
    mdict={'username': 'Sharathchandra'}
    return render(request,'landingPage/index.html',mdict)
