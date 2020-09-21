#getting error like datatype mismatch... id - number expected CharField
# ValueError: Field 'id' expected a number but got 'Mckenzie LLC'

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','firstproject.settings')

import django
django.setup() #setup the above cofiguration

# fake populating script
import random
from myapp.models import TopicRead,Webpage,AccessRecord
from faker import Faker
fakegen=Faker()
topics=['Search','Social Media','Games', 'Marketplace', 'News']

def  add_topic():
    t=TopicRead.objects.get_or_create(topic_name=random.choice(topics))[0]#automatically this will return a tuple of 0 value
    t.save()
    return t

def popultate_script(n=5):
    for entry in range(n):
        # get the fake topic
        t_val=add_topic()

        #get the fake url, name, DateField
        fake_url=fakegen.url()
        fake_name=fakegen.company()
        fake_date=fakegen.date()

        # create the webpage entry
        webpg=Webpage.objects.get_or_create(topic=t_val, name=fake_name, url=fake_url)[0]

        # create fake AccessRecord
        acc_rec=AccessRecord.objects.get_or_create(access_name=fake_name,date=fake_date)[0]

if __name__=='__main__':
    print('populating script')
    popultate_script(10)
    print('populating completed!!!')
