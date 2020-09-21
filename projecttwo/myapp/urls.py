from django.urls import path
from myapp import views
urlpatterns=[
    path('',views.get_all_persons,name='get_all_persons'),
]
