from django.contrib import admin
from .models import Video, Comment

# admin.site.register(Video)
# admin.site.register(Comment)
admin.site.register([Video, Comment])


# Register your models here.
