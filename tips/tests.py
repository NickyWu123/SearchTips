#coding:utf-8
from django.test import TestCase
from tips.models import *
import os
from Search_Tips.wsgi import application
# Create your tests here.


entires=Entries.objects.filter(word__startswith='诗人').order_by('datetime')
print entires


