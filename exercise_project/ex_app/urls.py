from django.urls import path
from ex_app import views

urlpatterns=[
    path('',views.get_all_user_page, name='get_all_user_page'),
]
