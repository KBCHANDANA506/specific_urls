from app1.views import *
from django.urls import path
app_name='something'
urlpatterns=[
    path('dhoni/',dhoni,name='dhoni'),
    path('pandya/',pandya,name='pandya'),

]