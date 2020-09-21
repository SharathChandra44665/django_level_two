import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','testproject1.settings')

import django
django.setup()

# fake script populate
# import random
from myapp.models import Person
from faker import Faker
#
fgen=Faker()
def add_persons(n=5):
    for x in range(n):
        f_name=fgen.first_name()
        l_name=fgen.last_name()
        e_mail=fgen.email()

        p_nos=Person.objects.get_or_create(first_name=f_name,last_name=l_name,email=e_mail)[0]

if __name__=='__main__':
    print('poulating scripts !!!')
    add_persons(10)
    print('its complete!!!')
