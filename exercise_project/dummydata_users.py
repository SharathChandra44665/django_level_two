import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'exercise_project.settings')
import django
django.setup()
from ex_app.models import UserAccount
from faker import Faker
fgen=Faker()
def set_dummy_data(arg=5):

    for entry in range(arg) :
        name=fgen.name().split()
        f_name=name[0]
        l_name=name[1]
        users=UserAccount.objects.get_or_create(first_name=f_name,last_name=l_name,user_mail=fgen.email())[0]

if __name__ == '__main__':
    print('populating dummy data')
    set_dummy_data(15)
    print('completed!!!')
