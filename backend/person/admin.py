from django.contrib import admin
from .models import Person

class PersonAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "email", "phone", "created_at"]  # 添加 id
    readonly_fields = ("id",)  # 让 id 在详情页可见但不可修改

admin.site.register(Person, PersonAdmin)
