After create project , then go to models.py
1.
from django.db import models

# Create your models here.
class hydjobs(models.Model):
    date=models.DateField();
    company=models.CharField(max_length=100);
    title=models.CharField(max_length=100);
    eligibility=models.CharField(max_length=100);
    address=models.CharField(max_length=100);
    email=models.EmailField();
    phonenumber=models.IntegerField();

class banglorejobs(models.Model):
    date=models.DateField();
    company=models.CharField(max_length=100);
    title=models.CharField(max_length=100);
    eligibility=models.CharField(max_length=100);
    address=models.CharField(max_length=100);
    email=models.EmailField();
    phonenumber=models.IntegerField();

class punejobs(models.Model):
    date=models.DateField();
    company=models.CharField(max_length=100);
    title=models.CharField(max_length=100);
    eligibility=models.CharField(max_length=100);
    address=models.CharField(max_length=100);
    email=models.EmailField();
    phonenumber=models.IntegerField();

2.  makemigrations
3.  migrate
4. register model in admin.py
from django.contrib import admin
from testApp.models import hydjobs,banglorejobs,punejobs
# Register your models here.
class hydjobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']

class banglorejobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']

class punejobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']

    admin.site.register(hydjobs,hydjobsAdmin)
    admin.site.register(punejobs,punejobsAdmin)
    admin.site.register(banglorejobs,banglorejobsAdmin)
5. createsuperuser
6. pipulate data to the model class with the help of "faker module"  , pip install faker
   then create file populate_job.py then,

   import os
   os.environ.setdefault('DJANGO_SETTING_MODULE','jobportalproject.settings')
   import django
   django.setup()

   from testApp.models import faker
   from faker import Faker
   from random import *
   fake=Faker()
   def phonenumbergen():
       d1=randint(7,9)
       num=''+str(d1)
       for i in range(9):
           num=num+str(randint(0,9))
       return int(num)
   def populate(n):
       for i in range(n):
           fdate=fake.date.order_by()
           fcompany=fake.company()
           ftitle=fake.random_element(elements=('Project Manager', 'TeamLead','Software Engineer'))
           feligibility=fake.random_element(elements=('B.Tech','M.Tech','MCA','Phd'))
           faddress=fake.address()
           femail=fake.email()
           fphonenumber=phonenumbergen()
           hydjobs_record=hydjobs.objects.get_or_create(date=fdate,company=fcompany,titile=ftitle,eligibility=feligibility,address=faddress,email=femail,phonenumber=fphonenumber)
   populate(25)

7. py populate_job.py

8. Go to hydjobs.html and then,

<!DOCTYPE html>
{% load staticfiles%}
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <link rel="stylesheet" href="{% static "css/demo.css"%}">
    <title>Hyderabad jobs</title>
  </head>
  <body>
    <h1>Hyderabad Jpbs Info</h1>

    <img src="{% static "images/hyd1.jpg"%}" alt="">
    <img src="{% static "images/hyd2.jpg"%}" alt="">
    <img src="{% static "images/hyd3.jpg"%}" alt="">
    <img src="{% static "images/hyd4.jpg"%}" alt="">
    <img src="{% static "images/hyd5.jpg"%}" alt="">
    <img src="{% static "images/hyd6.jpg"%}" alt="">
    <hr>
    {% if jobs_list %}
    <table id='tab'>
      <thead>
        <th>Date</th>
        <th>COMPANY</th>
        <th>Title</th>
        <th>Eligibility</th>
        <th>Address</th>
        <th>Email</th>
        <th>Phone Number</th>
      </thead>
      {% for job in jobs_list%}
      <tr>
        <td>{{job.date}}</td>
        <td>{{job.company}}</td>
        <td>{{job.title}}</td>
        <td>{{job.eligibility}}</td>
        <td>{{job.email}}</td>
        <td>{{job.phonenumber}}</td>
      </tr>
      {% endfor%}
   </table>
   {%else%}
   <p>No jobs found in Hyderabad</p>
   {% endif%}

  </body>
</html>
