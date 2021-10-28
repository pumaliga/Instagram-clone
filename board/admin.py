from django.contrib import admin
from board.models import Post, CustomUser


admin.site.register(Post)
admin.site.register(CustomUser)
