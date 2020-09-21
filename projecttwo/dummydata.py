from faker import Faker
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','projecttwo.settings')
import django
django.setup()
from myapp.models import Person


fgen=Faker()
def populate_dummy_data(arg=5):
    for entry in range(arg):
        person_detail=Person.objects.get_or_create(first_name=fgen.first_name(), last_name=fgen.last_name(), person_mail=fgen.email())[0]


if __name__=='__main__':
    print('populating dummy data')
    populate_dummy_data(15)
    print('complete!!!')
