# Django-Tutorial-RIG
RIG Internship Learn

Hello world

#startproject
django-admin startproject mysite

#django-admin error occur
#creating virtualenv
pip install virtualenv
python -m virtualenv ven //venfolder

#show installed packages,modules
pip freeze

#start app
python manage.py startapp myblog

#runserver
python manage.py runserver

#migrate
python manage.py migrate

#create user
python manage.py createsuperuser


# after create table always make
python manage.py makemigrations
python manage.py migrate

##### model #############
created tabel in database as model



#### Day 7 #########
##### view #########
fromm myapp.models import table(modle)

#for templates in setting.py
'DIRS': [BASE_DIR/'templates'],

{% load static %}

#external css
<link rel="stylesheet" href="{% static 'mycss.css' %}">

#img
<img src="{% static 'Image/img2.jpg' %}" alt="img1">
<img src="{% static 'Image/img1.jpg' %}">


#in setting.py
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

#########################
##### model > view > template
def postdata(request): #come fromm contorller 
    post_data = Post.objects.all()
    context = {'post_data': post_data}
    return render(request,'posts.html',context)

 {% for i in post_data %}
           <h2>{{ i }}</h2> 
           <h3>{{ i.title }}</h3> 
            <h4>{{ i.body }}</h4>
        {% endfor %}


#new model
class myfriends(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    address = models.TextField(max_length=30)
    email = models.EmailField()
    photo = models.ImageField(upload_to='photo')
    created = models.DateField()
    
    def __str__(self):
        return self.name


######### media note #####
photo = models.ImageField(upload_to='photo')
<img id="mm" src="{{ i.photo.url }}" alt="photo">

setting.py

STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'static_a'

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'


urls.py

from django.conf import settings
from django.conf.urls.static import static


....

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


######################
model > view > control > template

