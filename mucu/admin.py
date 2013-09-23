from django.contrib import admin
from mucu.models import *

class StaffAdmin(admin.ModelAdmin):
    list_display = ('l_name', 'f_name', 'position', 'contact')


class MemberAdmin(admin.ModelAdmin):
    list_display = ('f_name', 'f_name', 'course', 'flag')


admin.site.register(Member, MemberAdmin)
admin.site.register(Pertner)
admin.site.register(News_letter)
admin.site.register(Staff, StaffAdmin)
