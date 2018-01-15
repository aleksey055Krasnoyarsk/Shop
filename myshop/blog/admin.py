from django.contrib import admin
from .models import Post
from .models import About_us
from .models import Glavnaya
from .models import Contacts



# Register your models here.



admin.site.register(Post)
admin.site.register(About_us)
admin.site.register(Glavnaya)
admin.site.register(Contacts)