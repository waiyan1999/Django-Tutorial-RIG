from django.contrib import admin
from .models import Post,Customer,myfriends


# Register your models here.

admin.site.register(Post)
admin.site.register(Customer)
# admin.site.register(Product)
admin.site.register(myfriends)


