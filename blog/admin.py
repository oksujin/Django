from django.contrib import admin
from .models import Post
# post의 models를 가져와서 admin에 등록하겠다.

admin.site.register(Post)