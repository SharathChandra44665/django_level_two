from django.contrib import admin
from myapp.models import TopicRead, Webpage, AccessRecord
# Register your models here.

admin.site.register(TopicRead)
admin.site.register(Webpage)
admin.site.register(AccessRecord)
