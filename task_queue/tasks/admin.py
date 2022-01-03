from django.contrib import admin

from tasks.models import Task, Foo

admin.site.register(Task)
admin.site.register(Foo)
